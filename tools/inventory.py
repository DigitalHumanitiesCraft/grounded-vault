"""Generate the source inventory of a Grounded Vault from its file state.

The inventory used to be kept by hand and checked by the validator, which made
it a second record of what the vault holds and let it drift away from the files.
The files are the record; this script reads them and writes the table.

One row per source, in the shape `knowledge/state.md` declares:
Source | Type | Channel | Markdown representation | Distillate | Coverage | Status.
The processing status follows from what is present: an original without a
Markdown representation is `new`, a representation without a distillate is
`ingested`, and a distillate makes the source `distilled`. Type and channel come
from the frontmatter of the representation; a publication has no representation,
so its row is built from the CSL record in `references/` and carries the import
channel. Coverage counts, for a document representation, the blocks some
distillate statement anchors against the blocks the file carries, so that a
source the distillates left mostly unread is visible in the register.

`00_sources/` is gitignored and may be absent on a clone. It is read when it is
there, so an original that has not been ingested yet shows up as a `new` row, and
skipped when it is not, in which case that state is simply invisible.

Documents are parsed by the loader of tools/validate.py. A file whose frontmatter
does not parse has no row, and its finding is printed as a WARN line, so that the
table never loses a source without saying so.

Usage:
    python tools/inventory.py <vault-root> [--write]

Without `--write` the table goes to stdout. With `--write` it replaces the block
between the `<!-- inventory:begin -->` and `<!-- inventory:end -->` markers in
knowledge/state.md.
"""

from __future__ import annotations

import argparse
import sys
from dataclasses import dataclass
from pathlib import Path

from validate import (
    DATA_FOLDER,
    DISTILLATE_LAYER,
    DOCUMENTS_FOLDER,
    REPRESENTATION_LAYER,
    SOURCE_LAYER,
    Doc,
    anchored_blocks,
    field_links,
    load_docs,
    load_references,
    utf8_console,
    write_text_atomic,
)

STATE = "knowledge/state.md"
BEGIN = "<!-- inventory:begin -->"
END = "<!-- inventory:end -->"

COLUMNS = (
    "Source",
    "Type",
    "Channel",
    "Markdown representation",
    "Distillate",
    "Coverage",
    "Status",
)
EMPTY = "—"


@dataclass
class Row:
    source: str
    type: str
    channel: str
    representation: str
    distillate: str
    status: str
    coverage: str = EMPTY

    def cells(self) -> tuple[str, ...]:
        return (
            self.source,
            self.type,
            self.channel,
            self.representation,
            self.distillate,
            self.coverage,
            self.status,
        )


def _first_link(fm: dict, name: str) -> str | None:
    links = field_links(fm, name)
    return links[0][0] if links else None


def _title(fm: dict, fallback: str) -> str:
    metadata = fm.get("metadata")
    if isinstance(metadata, dict) and str(metadata.get("title") or "").strip():
        return str(metadata["title"]).strip()
    return fallback


def _link(rel: str) -> str:
    return f"[[{rel}]]"


def _escape(cell: str) -> str:
    return cell.replace("|", "\\|")


def _distillates(docs: dict[str, Doc]) -> dict[str, list[tuple[str, dict]]]:
    """Distillates grouped by what they hang on, a representation or a reference id.

    A distillate that names neither is grouped under its own path, so it stays a
    row of its own rather than disappearing from the inventory. The grouping is
    a list because two distillates may name the same source, which is a state
    the schema forbids and the inventory must still show.
    """
    found: dict[str, list[tuple[str, dict]]] = {}
    for rel, doc in docs.items():
        if not rel.startswith(DISTILLATE_LAYER):
            continue
        key = (
            _first_link(doc.fm, "representation")
            or str(doc.fm.get("reference") or "").strip()
        )
        found.setdefault(key or rel, []).append((rel, doc.fm))
    return found


def _originals(root: Path, representations: dict[str, dict]) -> list[str]:
    """Files in 00_sources/ that no representation names.

    The folder is gitignored, so its absence says nothing and is not a finding.
    """
    directory = root / SOURCE_LAYER
    if not directory.is_dir():
        return []
    claimed = {
        target
        for fm in representations.values()
        for name in ("source", "data")
        if (target := _first_link(fm, name))
    }
    found = []
    for path in sorted(directory.rglob("*")):
        rel = path.relative_to(root).as_posix()
        if not path.is_file() or path.name.startswith(".") or path.name == "README.md":
            continue
        if rel not in claimed:
            found.append(rel)
    return found


def _coverage(docs: dict[str, Doc]) -> dict[str, str]:
    """Per document representation the anchored blocks over all its blocks."""
    anchored = anchored_blocks(docs)
    return {
        rel: f"{len(anchored.get(rel, set()) & set(doc.blocks))}/{len(set(doc.blocks))}"
        for rel, doc in docs.items()
        if doc.fm.get("type") == "representation"
        and doc.fm.get("source-type") == "document"
        and doc.blocks
    }


def rows(root: Path, problems: list[str] | None = None) -> list[Row]:
    """The inventory rows of the vault; parse and reference problems go into `problems`."""
    docs, report = load_docs(root, (REPRESENTATION_LAYER, DISTILLATE_LAYER))
    if problems is not None:
        problems += [f"{rel}: {code} {message}" for code, rel, message in report.errors]
    representations = {
        rel: doc.fm
        for rel, doc in docs.items()
        if rel.startswith((DOCUMENTS_FOLDER, DATA_FOLDER))
    }
    distillates = _distillates(docs)
    references = {
        key: str(record.get("title") or key)
        for key, record in load_references(root, problems).items()
    }
    coverage = _coverage(docs)
    collected: list[Row] = []

    for rel, fm in representations.items():
        source = _title(fm, rel.rsplit("/", 1)[-1])
        doctype = str(fm.get("source-type") or EMPTY)
        channel = str(fm.get("channel") or EMPTY)
        for distillate, _ in distillates.get(rel, [(None, {})]):
            collected.append(
                Row(
                    source=source,
                    type=doctype,
                    channel=channel,
                    representation=_link(rel),
                    distillate=_link(distillate) if distillate else EMPTY,
                    coverage=coverage.get(rel, EMPTY) if distillate else EMPTY,
                    status="distilled" if distillate else "ingested",
                )
            )

    for reference, title in references.items():
        for distillate, fm in distillates.get(reference, [(None, {})]):
            collected.append(
                Row(
                    source=title,
                    type="publication",
                    channel=str(fm.get("channel") or EMPTY),
                    representation=EMPTY,
                    distillate=_link(distillate) if distillate else EMPTY,
                    status="distilled" if distillate else "new",
                )
            )

    keyed = set(representations) | set(references)
    for key, group in distillates.items():
        if key in keyed:
            continue
        for rel, fm in group:
            collected.append(
                Row(
                    source=rel.rsplit("/", 1)[-1],
                    type=str(fm.get("source-type") or EMPTY),
                    channel=EMPTY,
                    representation=EMPTY,
                    distillate=_link(rel),
                    status="distilled",
                )
            )

    for rel in _originals(root, representations):
        collected.append(
            Row(
                source=rel.rsplit("/", 1)[-1],
                type=EMPTY,
                channel=EMPTY,
                representation=EMPTY,
                distillate=EMPTY,
                status="new",
            )
        )

    return sorted(
        collected, key=lambda row: (row.type, row.source.lower(), row.distillate)
    )


def render(rows: list[Row]) -> str:
    lines = [
        "| " + " | ".join(COLUMNS) + " |",
        "|" + "---|" * len(COLUMNS),
    ]
    for row in rows:
        lines.append("| " + " | ".join(_escape(cell) for cell in row.cells()) + " |")
    return "\n".join(lines)


def write(root: Path, table: str) -> str | None:
    """Replace the marked block of the state document; the reason when that is impossible."""
    path = root / STATE
    if not path.is_file():
        return f"no {STATE} to write into: {path}"
    text = path.read_text(encoding="utf-8")
    start, end = text.find(BEGIN), text.find(END)
    if start < 0 or end < 0 or end < start:
        return (
            f"{STATE} carries no inventory markers; add the two lines "
            f"{BEGIN} and {END} around the source inventory table"
        )
    updated = f"{text[: start + len(BEGIN)]}\n{table}\n{text[end:]}"
    if updated != text:
        write_text_atomic(path, updated)
    return None


def main() -> int:
    utf8_console()
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("root", type=Path, help="vault root directory")
    parser.add_argument(
        "--write",
        action="store_true",
        help=f"replace the marked block in {STATE} instead of printing",
    )
    args = parser.parse_args()

    root = args.root.resolve()
    problems: list[str] = []
    table = render(rows(root, problems))
    for problem in problems:
        print(f"WARN {problem}", file=sys.stderr)
    if not args.write:
        print(table)
        return 0
    if error := write(root, table):
        print(f"ERROR {error}", file=sys.stderr)
        return 1
    print(f"OK wrote the source inventory into {STATE}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
