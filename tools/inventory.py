"""Generate the source inventory of a Grounded Vault from its file state.

The inventory used to be kept by hand and checked by the validator, which made
it a second record of what the vault holds and let it drift away from the files.
The files are the record; this script reads them and writes the table.

One row per source, in the shape `knowledge/state.md` declares:
Source | Type | Channel | Markdown representation | Distillate | Status.
The processing status follows from what is present: an original without a
Markdown representation is `new`, a representation without a distillate is
`ingested`, and a distillate makes the source `distilled`. Type and channel come
from the frontmatter of the representation; a publication has no representation,
so its row is built from the CSL record in `references/` and carries the import
channel.

`00_sources/` is gitignored and may be absent on a clone. It is read when it is
there, so an original that has not been ingested yet shows up as a `new` row, and
skipped when it is not, in which case that state is simply invisible.

Usage:
    python tools/inventory.py <vault-root> [--write]

Without `--write` the table goes to stdout. With `--write` it replaces the block
between the `<!-- inventory:begin -->` and `<!-- inventory:end -->` markers in
knowledge/state.md.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path

import yaml

STATE = "knowledge/state.md"
BEGIN = "<!-- inventory:begin -->"
END = "<!-- inventory:end -->"

REPRESENTATION_FOLDERS = ("10_markdown/documents", "10_markdown/data")
DISTILLATE_FOLDER = "20_distillates"
SOURCE_FOLDER = "00_sources"
REFERENCE_FOLDER = "references"

COLUMNS = (
    "Source",
    "Type",
    "Channel",
    "Markdown representation",
    "Distillate",
    "Status",
)
EMPTY = "—"

WIKILINK = re.compile(r"\[\[([^\]#|]+?)(?:#\^[A-Za-z0-9-]+)?(?:\|[^\]]*)?\]\]")


@dataclass
class Row:
    source: str
    type: str
    channel: str
    representation: str
    distillate: str
    status: str

    def cells(self) -> tuple[str, ...]:
        return (
            self.source,
            self.type,
            self.channel,
            self.representation,
            self.distillate,
            self.status,
        )


def _frontmatter(path: Path) -> dict:
    """The YAML block of a Markdown file, empty when it carries none."""
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        return {}
    end = text.find("\n---", 4)
    if end < 0:
        return {}
    try:
        loaded = yaml.safe_load(text[4:end])
    except yaml.YAMLError:
        return {}
    return loaded if isinstance(loaded, dict) else {}


def _link_target(value: object) -> str | None:
    match = WIKILINK.search(str(value))
    return match.group(1).strip() if match else None


def _title(fm: dict, fallback: str) -> str:
    metadata = fm.get("metadata")
    if isinstance(metadata, dict) and str(metadata.get("title") or "").strip():
        return str(metadata["title"]).strip()
    return fallback


def _link(rel: str) -> str:
    return f"[[{rel}]]"


def _escape(cell: str) -> str:
    return cell.replace("|", "\\|")


def _markdown_files(root: Path, folder: str) -> list[Path]:
    directory = root / folder
    return sorted(directory.rglob("*.md")) if directory.is_dir() else []


def _representations(root: Path) -> dict[str, dict]:
    found: dict[str, dict] = {}
    for folder in REPRESENTATION_FOLDERS:
        for path in _markdown_files(root, folder):
            rel = path.relative_to(root).with_suffix("").as_posix()
            found[rel] = _frontmatter(path)
    return found


def _distillates(root: Path) -> dict[str, list[tuple[str, dict]]]:
    """Distillates grouped by what they hang on, a representation or a reference id.

    A distillate that names neither is grouped under its own path, so it stays a
    row of its own rather than disappearing from the inventory. The grouping is
    a list because two distillates may name the same source, which is a state
    the schema forbids and the inventory must still show.
    """
    found: dict[str, list[tuple[str, dict]]] = {}
    for path in _markdown_files(root, DISTILLATE_FOLDER):
        rel = path.relative_to(root).with_suffix("").as_posix()
        fm = _frontmatter(path)
        key = (
            _link_target(fm.get("representation") or "")
            or str(fm.get("reference") or "").strip()
        )
        found.setdefault(key or rel, []).append((rel, fm))
    return found


def _references(root: Path) -> dict[str, str]:
    """CSL record id to its title, over every JSON file in references/."""
    found: dict[str, str] = {}
    directory = root / REFERENCE_FOLDER
    if not directory.is_dir():
        return found
    for path in sorted(directory.glob("*.json")):
        try:
            records = json.loads(path.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError):
            continue
        for record in records if isinstance(records, list) else [records]:
            if isinstance(record, dict) and record.get("id"):
                found[str(record["id"])] = str(record.get("title") or record["id"])
    return found


def _originals(root: Path, representations: dict[str, dict]) -> list[str]:
    """Files in 00_sources/ that no representation names.

    The folder is gitignored, so its absence says nothing and is not a finding.
    """
    directory = root / SOURCE_FOLDER
    if not directory.is_dir():
        return []
    claimed = {
        target
        for fm in representations.values()
        for field in ("source", "data")
        if (target := _link_target(fm.get(field) or ""))
    }
    found = []
    for path in sorted(directory.rglob("*")):
        rel = path.relative_to(root).as_posix()
        if not path.is_file() or path.name.startswith(".") or path.name == "README.md":
            continue
        if rel not in claimed:
            found.append(rel)
    return found


def rows(root: Path) -> list[Row]:
    representations = _representations(root)
    distillates = _distillates(root)
    references = _references(root)
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
                    status="distilled" if distillate else "ingested",
                )
            )

    for reference, title in references.items():
        for distillate, _ in distillates.get(reference, [(None, {})]):
            collected.append(
                Row(
                    source=title,
                    type="publication",
                    channel="import",
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


def write(root: Path, table: str) -> None:
    path = root / STATE
    if not path.is_file():
        raise SystemExit(f"no {STATE} to write into: {path}")
    text = path.read_text(encoding="utf-8")
    start, end = text.find(BEGIN), text.find(END)
    if start < 0 or end < 0 or end < start:
        raise SystemExit(
            f"{STATE} carries no inventory markers; add the two lines "
            f"{BEGIN} and {END} around the source inventory table"
        )
    updated = f"{text[: start + len(BEGIN)]}\n{table}\n{text[end:]}"
    if updated != text:
        path.write_text(updated, encoding="utf-8")


def main() -> None:
    if sys.platform == "win32":
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("root", type=Path, help="vault root directory")
    parser.add_argument(
        "--write",
        action="store_true",
        help=f"replace the marked block in {STATE} instead of printing",
    )
    args = parser.parse_args()

    root = args.root.resolve()
    table = render(rows(root))
    if args.write:
        write(root, table)
        print(f"wrote the source inventory into {STATE}")
    else:
        print(table)


if __name__ == "__main__":
    main()
