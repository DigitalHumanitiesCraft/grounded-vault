"""Deterministic validation of a Grounded Vault against its schema.

Implements the validation contract from knowledge/operations.md: frontmatter
conformance per document type, anchor resolution, layer direction of anchors,
uniqueness of block and statement IDs, statement IDs, quotation recording,
computation declarations, MOC reachability, bidirectional contested links,
chapter mirror and footnote keywords, status discipline including the ladder
against the anchors a document rests on, assertions that rest on the same
anchors as another, footnote aliases that rename the assertion they cite, a
production chain that holds no document at all, checks older than the content
they judge, sources whose blocks the distillates mostly leave unanchored, and
quotation checks that do not name the text version they ran on. The rules are
defined in knowledge/schema.md; this script only enforces them.

Warnings report that a check found nothing to check, or found something that
needs a human decision rather than a verdict. They are always printed and
counted.

The module is also the shared parsing layer of the other tools. review.py,
inventory.py and migrate.py import the frontmatter split, document loading,
link extraction and the folder constants from here, so that what counts as a
document, a link or a statement cannot drift between them.

Usage:
    python tools/validate.py <vault-root> [--no-computations] [--min-coverage 0.5]
    python tools/validate.py <vault-root> --chapter 40_output/<slug>

Data anchors are re-run and compared by default; --no-computations skips that.
--min-coverage sets the share of a document's blocks that distillates must
anchor before W-COVERAGE stays silent; 0 switches the check off.

--chapter narrows the run to one chapter of the output and, transitively, the
assertions, distillates and representations it hangs on, so that the state of the
rest of the vault does not enter its verdict. The checks that are decidable only
over the whole vault stay out of that mode and are named in its closing lines.

Exit code 0 when no errors were found; warnings alone do not fail the run. In
chapter mode any warning in scope fails the run as well, because there the run
answers whether this chapter is ready for acceptance.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
from collections import Counter
from collections.abc import Iterable
from dataclasses import dataclass, field
from datetime import date, datetime
from pathlib import Path

import yaml

SOURCE_LAYER = "00_sources/"
REPRESENTATION_LAYER = "10_markdown/"
DOCUMENTS_FOLDER = "10_markdown/documents/"
DATA_FOLDER = "10_markdown/data/"
DISTILLATE_LAYER = "20_distillates/"
ASSERTION_LAYER = "30_assertions/"
REFERENCES_FOLDER = "references"

CONTENT_FOLDERS = (
    "10_markdown",
    "20_distillates",
    "30_assertions",
    "40_output",
    "glossary",
)

CHAIN_FOLDERS = ("10_markdown", "20_distillates", "30_assertions", "40_output")

TYPE_FOLDER = {
    "representation": "10_markdown",
    "distillate": "20_distillates",
    "assertion": "30_assertions",
    "moc": "30_assertions",
    "chapter": "40_output",
    "glossary": "glossary",
}

# Frontmatter fields whose values are wikilinks, which the schema requires quoted.
LINK_FIELDS = (
    "representation",
    "data",
    "superseded-by",
    "contested-with",
    "grounding",
    "assertions",
    "topics",
)
# The link fields that name a file of the vault and so must resolve. A topic
# link names its topic, not the path of its topic map.
RESOLVED_LINK_FIELDS = tuple(name for name in LINK_FIELDS if name != "topics")
PLACEHOLDER_SCAN_FILES = ("CLAUDE.md", "HOME.md")

# The layer a document type grounds in; the chapter scope walks down this chain.
LAYER_BELOW = {
    "chapter": ASSERTION_LAYER,
    "assertion": DISTILLATE_LAYER,
    "distillate": REPRESENTATION_LAYER,
}
VAULT_WIDE_CHECKS = ("W-EMPTY", "W-NO-OUTPUT", "W-COVERAGE")
# Below this share of anchored blocks a source counts as unexhausted. Half is
# the point where more of a source is unread than read; an instance moves it.
DEFAULT_MIN_COVERAGE = 0.5
# Data anchors re-run scripts from the vault, so only this folder may hold them.
ANALYSIS_FOLDER = "tools/analysis/"
COMPUTATION_TIMEOUT = 120

SOURCE_TYPES = frozenset({"document", "publication", "data"})
CHANNELS = frozenset({"handover", "collection", "import", "deep-research"})
# A publication has no representation, so its distillate records how the CSL
# record arrived, and only the channels that deliver records apply.
PUBLICATION_CHANNELS = frozenset({"import", "deep-research"})
STATUS_VOCAB = {
    "distillate": frozenset({"grounded", "validated", "verified", "superseded"}),
    "assertion": frozenset({"grounded", "validated", "verified", "contested"}),
    "chapter": frozenset({"grounded", "validated", "verified"}),
}
# The ladder a status climbs. `contested` and `superseded` lie beside it and
# earn no rank, so a document resting on one of them cannot rise above grounded.
STATUS_RANK = {"grounded": 0, "validated": 1, "verified": 2}
REQUIRED_CHECKS = {
    "validated": ("validation", "machine-review"),
    "verified": ("validation", "machine-review", "verification"),
}
# Machine review pairs the assertions a chapter cites, never its sentences, so a
# chapter's rungs carry no machine-review record of their own and the ladder
# minimum over its assertions stands in for it.
CHAPTER_REQUIRED_CHECKS = {
    "validated": ("validation",),
    "verified": ("validation", "verification"),
}
# The frontmatter field naming the anchors whose status a document cannot exceed.
# A representation carries no status, so a distillate has nothing to exceed.
ANCHOR_FIELD = {"assertion": "grounding", "chapter": "assertions"}
REQUIRED_FIELDS = {
    "representation": (
        "type",
        "source-type",
        "channel",
        "metadata",
        "created",
        "updated",
    ),
    "distillate": (
        "type",
        "source-type",
        "topics",
        "status",
        "checked",
        "created",
        "updated",
    ),
    "assertion": (
        "type",
        "topics",
        "status",
        "checked",
        "grounding",
        "created",
        "updated",
    ),
    "moc": ("type", "topic", "created", "updated"),
    "chapter": (
        "type",
        "status",
        "checked",
        "assertions",
        "posits",
        "created",
        "updated",
    ),
    "glossary": ("type", "term", "created", "updated"),
}
# The schema defines a Markdown representation for these two source types only;
# `source` of a data representation is optional, since the data file may be the
# original itself.
REPRESENTATION_FIELDS = {
    "document": ("source", "converter"),
    "data": ("data",),
}

WIKILINK = re.compile(r"\[\[([^\]#|]+?)(?:#\^([A-Za-z0-9-]+))?(?:\|[^\]]*)?\]\]")
ALIASED_LINK = re.compile(r"\[\[([^\]#|]+?)(?:#\^[A-Za-z0-9-]+)?\|([^\]]*)\]\]")
H1 = re.compile(r"^#\s+(.*)$", re.MULTILINE)
BLOCK_ID = re.compile(r"\^([A-Za-z0-9-]+)\s*$")
FOOTNOTE_DEF = re.compile(r"^\[\^([A-Za-z0-9]+)\]:\s*(.*)$")
FOOTNOTE_REF = re.compile(r"\[\^([A-Za-z0-9]+)\]")
COMPUTATION = re.compile(r"computation:\s*`([^`]+)`\s*(?:→|->)\s*`([^`]+)`")
# The quotation block of a publication statement, joined over its lines: the
# verbatim text in quotation marks, then the identifier with its locator.
QUOTATION = re.compile(r'^["“].+["”]\s*\(.+\)$', re.DOTALL)
PLACEHOLDER = re.compile(r"\{\{\s*([^{}]+?)\s*\}\}")
ISO_DATE = re.compile(r"^\d{4}-\d{2}-\d{2}$")


@dataclass
class Doc:
    path: Path
    rel: str  # root-relative path without extension, forward slashes
    fm: dict
    body: str
    blocks: list[str]  # in document order, duplicates kept for the uniqueness check


@dataclass
class Report:
    errors: list[tuple[str, str, str]] = field(default_factory=list)
    warnings: list[tuple[str, str, str]] = field(default_factory=list)

    def error(self, code: str, rel: str, message: str) -> None:
        self.errors.append((code, rel, message))

    def warn(self, code: str, rel: str, message: str) -> None:
        self.warnings.append((code, rel, message))

    def codes(self) -> set[str]:
        return {code for code, _, _ in self.errors}


def utf8_console() -> None:
    """Switch the Windows console streams to UTF-8.

    Findings quote arrows and typographic quotation marks from the vault, which
    the legacy code page of a Windows console cannot encode.
    """
    if sys.platform == "win32":
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")


def write_text_atomic(path: Path, text: str) -> None:
    """Replace a file in one step, keeping the line endings it had on disk.

    The text arrives with LF, as read_text delivers it. A file that carried CRLF
    gets CRLF back, and a new file gets LF on every platform, so that a rewrite
    on Windows does not turn a whole file into a diff.
    """
    newline = "\r\n" if path.is_file() and b"\r\n" in path.read_bytes() else "\n"
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(text, encoding="utf-8", newline=newline)
    tmp.replace(path)


def split_frontmatter(text: str) -> tuple[str, str] | None:
    """The raw YAML block and the body of a Markdown file, None when it has no frontmatter.

    The one place the frontmatter delimiter is read; inventory and migrate
    import it, so that what counts as frontmatter cannot drift between tools.
    A leading byte order mark is tolerated, since some editors on Windows write
    one, and the search for the closing delimiter starts on the newline of the
    opening line, so that an empty block closes too.
    """
    text = text.removeprefix("\ufeff")
    if not text.startswith("---\n"):
        return None
    end = text.find("\n---", 3)
    if end < 0:
        return None
    return text[4:end], text[end + 4 :]


def parse_doc(path: Path, root: Path, report: Report) -> Doc | None:
    rel = path.relative_to(root).with_suffix("").as_posix()
    text = path.read_text(encoding="utf-8-sig")
    split = split_frontmatter(text)
    if split is None:
        what = "unterminated" if text.startswith("---\n") else "missing"
        report.error("E-FRONTMATTER", rel, f"{what} frontmatter")
        return None
    raw, body = split
    try:
        fm = yaml.safe_load(raw)
    except yaml.YAMLError as exc:
        report.error("E-FRONTMATTER", rel, f"frontmatter is not valid YAML: {exc}")
        return None
    if fm is None:
        fm = {}
    if not isinstance(fm, dict):
        report.error("E-FRONTMATTER", rel, "frontmatter is not a mapping")
        return None
    blocks = [m.group(1) for line in body.splitlines() if (m := BLOCK_ID.search(line))]
    return Doc(path=path, rel=rel, fm=fm, body=body, blocks=blocks)


def load_docs(root: Path, folders: Iterable[str]) -> tuple[dict[str, Doc], Report]:
    """Every Markdown document under the given folders, keyed by its rel.

    A file that fails to parse is left out of the documents and recorded in the
    report, so that a caller can never lose one without saying so.
    """
    report = Report()
    docs: dict[str, Doc] = {}
    for folder in folders:
        for path in sorted((root / folder).rglob("*.md")):
            if doc := parse_doc(path, root, report):
                docs[doc.rel] = doc
    return docs, report


def load_references(root: Path, problems: list[str] | None = None) -> dict[str, dict]:
    """CSL records by id, over every JSON file in references/.

    The schema declares an array per file. A single record object is accepted
    as well, because a reference manager exporting one record may write it so.
    A file that is not valid JSON is named in `problems` when the caller passes
    a list; the validator does not, since every reference id it would have held
    then fails to resolve as E-ANCHOR.
    """
    records: dict[str, dict] = {}
    for path in sorted((root / REFERENCES_FOLDER).glob("*.json")):
        try:
            loaded = json.loads(path.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError) as exc:
            if problems is not None:
                problems.append(f"{path.relative_to(root).as_posix()}: {exc}")
            continue
        for record in loaded if isinstance(loaded, list) else [loaded]:
            if isinstance(record, dict) and record.get("id"):
                records[str(record["id"])] = record
    return records


def link_targets(text: str) -> list[tuple[str, str | None]]:
    return [(m.group(1).strip(), m.group(2)) for m in WIKILINK.finditer(text)]


def field_links(fm: dict, name: str) -> list[tuple[str, str | None]]:
    """The wikilink targets of one frontmatter field, whether it holds one value or a list.

    A value that is not a string contributes nothing here, which keeps a scalar
    from being iterated character by character; the validator reports such a
    value as E-FRONTMATTER.
    """
    raw = fm.get(name)
    values = raw if isinstance(raw, list) else [raw]
    return [
        link
        for value in values
        if isinstance(value, str)
        for link in link_targets(value)
    ]


def quotation_text(follow: list[str]) -> str:
    """The quotation block of a publication statement as one line of text.

    Validation holds this string against the declared form and review hands it
    to the reviewer as the passage, so both judge the same text.
    """
    return " ".join(
        line.lstrip()[1:].strip() for line in follow if line.lstrip().startswith(">")
    )


def _check_frontmatter(doc: Doc, report: Report) -> None:
    doctype = doc.fm.get("type")
    if doctype not in REQUIRED_FIELDS:
        report.error("E-FRONTMATTER", doc.rel, f"unknown or missing type: {doctype!r}")
        return
    for key in REQUIRED_FIELDS[doctype]:
        if key not in doc.fm:
            report.error("E-FRONTMATTER", doc.rel, f"missing required field: {key}")
    if not doc.rel.startswith(TYPE_FOLDER[doctype]):
        report.error(
            "E-FRONTMATTER", doc.rel, f"type {doctype} does not belong in this folder"
        )
    if (
        doctype in STATUS_VOCAB
        and "status" in doc.fm
        and doc.fm["status"] not in STATUS_VOCAB[doctype]
    ):
        report.error(
            "E-FRONTMATTER", doc.rel, f"illegal status value: {doc.fm['status']!r}"
        )
    source_type = doc.fm.get("source-type")
    if "source-type" in doc.fm and source_type not in SOURCE_TYPES:
        report.error("E-FRONTMATTER", doc.rel, f"illegal source-type: {source_type!r}")
    if doctype == "representation":
        _check_representation_fields(doc, source_type, report)
    if doctype == "distillate" and source_type == "publication":
        if "channel" in doc.fm and doc.fm["channel"] not in PUBLICATION_CHANNELS:
            report.error(
                "E-FRONTMATTER",
                doc.rel,
                f"illegal channel for a publication: {doc.fm['channel']!r}",
            )
        if not doc.fm.get("reference"):
            report.error(
                "E-FRONTMATTER", doc.rel, "publication distillate needs a reference id"
            )
    elif doctype == "distillate" and not doc.fm.get("representation"):
        report.error("E-FRONTMATTER", doc.rel, "distillate needs a representation link")
    _check_link_fields(doc, report)


def _check_representation_fields(doc: Doc, source_type: object, report: Report) -> None:
    if doc.fm.get("channel") not in CHANNELS:
        report.error(
            "E-FRONTMATTER", doc.rel, f"illegal channel: {doc.fm.get('channel')!r}"
        )
    if "metadata" in doc.fm and not isinstance(doc.fm["metadata"], dict):
        report.error("E-FRONTMATTER", doc.rel, "metadata must be a mapping")
    if source_type == "publication":
        report.error(
            "E-FRONTMATTER",
            doc.rel,
            "a publication has no Markdown representation; its record lives in references/",
        )
    for key in REPRESENTATION_FIELDS.get(str(source_type), ()):
        if key not in doc.fm:
            report.error("E-FRONTMATTER", doc.rel, f"missing required field: {key}")


def _check_link_fields(doc: Doc, report: Report) -> None:
    """A link field holds quoted wikilinks.

    Unquoted, `[[x]]` is a nested YAML list rather than a link, and a field read
    that way would silently carry no anchor at all.
    """
    for name in LINK_FIELDS:
        raw = doc.fm.get(name)
        if raw is None or raw == "" or raw == []:
            continue
        for value in raw if isinstance(raw, list) else [raw]:
            if not isinstance(value, str) or not WIKILINK.search(value):
                report.error(
                    "E-FRONTMATTER",
                    doc.rel,
                    f"{name} value is not a quoted wikilink: {value!r}",
                )


def _check_status_discipline(doc: Doc, report: Report) -> None:
    status = doc.fm.get("status")
    checked = doc.fm.get("checked") or {}
    if not isinstance(checked, dict):
        report.error("E-STATUS", doc.rel, "checked must be a map of check name to date")
        return
    required = (
        CHAPTER_REQUIRED_CHECKS if doc.fm.get("type") == "chapter" else REQUIRED_CHECKS
    )
    for check in required.get(status, ()):
        if check not in checked:
            report.error(
                "E-STATUS", doc.rel, f"status {status} without checked.{check}"
            )
    for name, value in checked.items():
        if _iso_date(value) is None:
            report.error(
                "E-STATUS",
                doc.rel,
                f"checked.{name} records no ISO date: {value!r}",
            )


def _iso_date(value: object) -> date | None:
    """A calendar date in the form YYYY-MM-DD, or the date YAML already parsed from it."""
    if isinstance(value, datetime):
        return value.date()
    if isinstance(value, date):
        return value
    text = str(value).strip()
    if not ISO_DATE.match(text):
        return None
    try:
        return date.fromisoformat(text)
    except ValueError:
        return None


def _check_staleness(doc: Doc, report: Report) -> None:
    """Checks older than the content they judge no longer cover the document.

    A document that carries no check date at all is in the state the ladder
    starts from and is not stale.
    """
    checked = doc.fm.get("checked")
    if not isinstance(checked, dict):
        return
    dates = [d for value in checked.values() if (d := _iso_date(value))]
    updated = _iso_date(doc.fm.get("updated"))
    if not dates or updated is None:
        return
    latest = max(dates)
    if updated > latest:
        report.warn(
            "W-STALE",
            doc.rel,
            f"updated {updated.isoformat()} is newer than the latest check {latest.isoformat()}",
        )


def _check_ladder(doc: Doc, docs: dict[str, Doc], report: Report) -> None:
    """A document's status is the minimum of the states of its anchors.

    A check that ran on this document alone says nothing about the material it
    rests on, so one unreviewed anchor keeps the whole document at grounded.
    """
    field_name = ANCHOR_FIELD.get(doc.fm.get("type"))
    own = STATUS_RANK.get(doc.fm.get("status"), 0)
    if field_name is None or own == 0:
        return
    for target, _ in field_links(doc.fm, field_name):
        other = docs.get(target)
        if other is None:
            continue  # E-ANCHOR speaks about the target that does not exist
        if STATUS_RANK.get(other.fm.get("status"), 0) < own:
            report.error(
                "E-LADDER",
                doc.rel,
                f"status {doc.fm['status']} above its anchor {target} "
                f"at status {other.fm.get('status')!r}",
            )


def _resolve_anchor(
    target: str,
    block: str | None,
    docs: dict[str, Doc],
    root: Path,
    doc: Doc,
    report: Report,
) -> None:
    if target.startswith(SOURCE_LAYER):
        return  # originals are local-only and not resolvable on every clone
    if target not in docs:
        if not (root / f"{target}.md").exists() and not (root / target).exists():
            report.error("E-ANCHOR", doc.rel, f"link target does not exist: {target}")
        return
    if block is not None and block not in docs[target].blocks:
        report.error("E-ANCHOR", doc.rel, f"block ^{block} not found in {target}")


def _check_layer(
    target: str, expected: str, what: str, doc: Doc, report: Report
) -> None:
    """An anchor may only point one layer down, into the layer that grounds it."""
    if target.startswith(SOURCE_LAYER):
        return
    if not target.startswith(expected):
        report.error(
            "E-LAYER",
            doc.rel,
            f"{what} must anchor in {expected}, but points to {target}",
        )


def _frontmatter_links(doc: Doc) -> list[tuple[str, str, str | None]]:
    """Link targets of the frontmatter fields that name other files of the vault."""
    return [
        (name, target, block)
        for name in RESOLVED_LINK_FIELDS
        for target, block in field_links(doc.fm, name)
    ]


def _check_frontmatter_links(
    doc: Doc, docs: dict[str, Doc], root: Path, report: Report
) -> None:
    for name, target, block in _frontmatter_links(doc):
        _resolve_anchor(target, block, docs, root, doc, report)
        if name == "representation":
            _check_layer(target, REPRESENTATION_LAYER, "representation", doc, report)


def _check_duplicate_ids(doc: Doc, report: Report) -> None:
    doctype = doc.fm.get("type")
    if doctype == "representation":
        ids, label = doc.blocks, "block ID"
    elif doctype == "distillate":
        ids = [
            m.group(1)
            for line, _ in statement_lines(doc.body)
            if (m := BLOCK_ID.search(line))
        ]
        label = "statement ID"
    else:
        return
    for dup, count in sorted(Counter(ids).items()):
        if count > 1:
            report.error("E-DUPLICATE", doc.rel, f"duplicate {label}: ^{dup}")


def _check_placeholders(
    root: Path, report: Report, paths: list[Path] | None = None
) -> None:
    """Template tokens that survived instantiation, in content and in the layers around it."""
    if paths is None:
        paths = [
            p
            for folder in CONTENT_FOLDERS
            for p in sorted((root / folder).rglob("*.md"))
        ]
        paths += sorted((root / "knowledge").glob("*.md"))
        paths += [root / name for name in PLACEHOLDER_SCAN_FILES]
    for path in paths:
        if not path.is_file():
            continue
        seen: set[str] = set()
        for m in PLACEHOLDER.finditer(path.read_text(encoding="utf-8")):
            name = m.group(1)
            if name in seen:
                continue
            seen.add(name)
            report.warn(
                "W-PLACEHOLDER",
                path.relative_to(root).with_suffix("").as_posix(),
                f"unfilled template placeholder: {{{{{name}}}}}",
            )


def statement_lines(body: str) -> list[tuple[str, list[str]]]:
    """Top-level bullets of the Core statements section, each with its indented follow-up lines."""
    lines = body.splitlines()
    statements: list[tuple[str, list[str]]] = []
    in_section = False
    for line in lines:
        if line.startswith("## "):
            in_section = line.strip().lower() == "## core statements"
            continue
        if not in_section:
            continue
        if line.startswith("- "):
            statements.append((line, []))
        elif line.startswith((" ", "\t")) and statements:
            statements[-1][1].append(line)
    return statements


def _ids_outside_core_statements(body: str) -> list[str]:
    """IDs a distillate mints anywhere but in its Core statements section.

    Every ID in a distillate is citable from the assertion layer, so an ID on an
    appraisal line would let a judgment of this vault be grounded in as if the
    source had made it.
    """
    stray: list[str] = []
    in_section = False
    for line in body.splitlines():
        if line.startswith("## "):
            in_section = line.strip().lower() == "## core statements"
        elif not in_section and (m := BLOCK_ID.search(line)):
            stray.append(m.group(1))
    return stray


def _own_representation(doc: Doc, docs: dict[str, Doc]) -> str | None:
    """The representation a document distillate's statements must anchor into.

    None when the link is missing, dead or outside the representation layer,
    because E-FRONTMATTER, E-ANCHOR or E-LAYER already speak about that, and a
    comparison against a target that is not there would only repeat them.
    """
    links = field_links(doc.fm, "representation")
    if not links:
        return None
    target = links[0][0]
    if target not in docs or not target.startswith(REPRESENTATION_LAYER):
        return None
    return target


def _check_distillate(
    doc: Doc,
    docs: dict[str, Doc],
    reference_ids: set[str],
    root: Path,
    report: Report,
    run_computations: bool,
) -> None:
    source_type = doc.fm.get("source-type")
    statements = statement_lines(doc.body)
    if not statements:
        report.error("E-STATEMENT", doc.rel, "no core statements found")
    for stray in _ids_outside_core_statements(doc.body):
        report.error(
            "E-STATEMENT",
            doc.rel,
            f"ID ^{stray} minted outside the Core statements section",
        )
    if source_type == "publication":
        if doc.fm.get("reference") and str(doc.fm["reference"]) not in reference_ids:
            report.error(
                "E-ANCHOR",
                doc.rel,
                f"reference id not in references/: {doc.fm['reference']}",
            )
        checked = doc.fm.get("checked") or {}
        if "quote" not in checked:
            report.error(
                "E-QUOTE", doc.rel, "quotation check not recorded (checked.quote)"
            )
        elif not doc.fm.get("checked-against"):
            report.warn(
                "W-VERSION",
                doc.rel,
                "checked.quote names no text version it ran on (checked-against)",
            )
    own = _own_representation(doc, docs) if source_type == "document" else None
    for line, follow in statements:
        short = line.strip()[:60]
        if not BLOCK_ID.search(line):
            report.error(
                "E-STATEMENT", doc.rel, f"core statement without statement ID: {short}"
            )
        anchored = [t for t, block in link_targets(line) if block is not None]
        for target in anchored:
            if source_type == "document" or target.startswith(DISTILLATE_LAYER):
                _check_layer(
                    target, REPRESENTATION_LAYER, "distillate statement", doc, report
                )
        if source_type == "document":
            _check_document_anchor(doc, anchored, own, short, report)
        elif source_type == "publication":
            if not QUOTATION.match(quotation_text(follow)):
                report.error(
                    "E-STATEMENT",
                    doc.rel,
                    "core statement without a quotation in the form "
                    f'"<verbatim>" (<identifier>): {short}',
                )
        elif source_type == "data":
            declared = [m for f in follow if (m := COMPUTATION.search(f))]
            if not declared:
                report.error(
                    "E-STATEMENT",
                    doc.rel,
                    f"core statement without computation: {short}",
                )
            for m in declared:
                _check_computation(
                    m.group(1), m.group(2), root, doc, report, run_computations
                )


def _check_document_anchor(
    doc: Doc, anchored: list[str], own: str | None, short: str, report: Report
) -> None:
    """A document statement carries exactly one block anchor, into its own source."""
    if not anchored:
        report.error(
            "E-STATEMENT", doc.rel, f"core statement without block anchor: {short}"
        )
        return
    if len(anchored) > 1:
        report.error(
            "E-STATEMENT",
            doc.rel,
            f"core statement carries {len(anchored)} block anchors, not exactly one: {short}",
        )
    for target in anchored:
        # A target outside the representation layer is E-LAYER's finding.
        if own and target.startswith(REPRESENTATION_LAYER) and target != own:
            report.error(
                "E-STATEMENT",
                doc.rel,
                f"core statement anchors into {target}, not into its representation {own}",
            )


def _check_computation(
    command: str,
    stated: str,
    root: Path,
    doc: Doc,
    report: Report,
    run_computations: bool,
) -> None:
    parts = command.split()
    index = next((i for i, part in enumerate(parts) if part.endswith(".py")), None)
    if index is None:
        report.error(
            "E-COMPUTATION", doc.rel, f"no script named in computation: {command}"
        )
        return
    named = parts[index].replace("\\", "/")
    if parts[index + 1 :]:
        report.error(
            "E-COMPUTATION",
            doc.rel,
            f"computation script takes no arguments: {command}",
        )
        return
    # Trust boundary: the validator executes what the vault names, and CI runs
    # it on every push, so a script that does not resolve into the analysis
    # folder is refused before existence is even checked. Resolving first keeps
    # a `..` segment from walking out of it.
    script = (root / named).resolve()
    if not script.is_relative_to((root / ANALYSIS_FOLDER).resolve()):
        report.error(
            "E-COMPUTATION",
            doc.rel,
            f"computation script outside {ANALYSIS_FOLDER}: {named}",
        )
        return
    if not script.is_file():
        report.error("E-COMPUTATION", doc.rel, f"computation script missing: {named}")
        return
    if not run_computations:
        return
    try:
        # UTF-8 on both ends, or a script printing non-ASCII fails under the
        # Windows code page while it passes on Linux CI.
        result = subprocess.run(
            [sys.executable, str(script)],
            cwd=root,
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            env={**os.environ, "PYTHONUTF8": "1"},
            timeout=COMPUTATION_TIMEOUT,
            check=False,
        )
    except subprocess.TimeoutExpired:
        report.error(
            "E-COMPUTATION",
            doc.rel,
            f"computation timed out after {COMPUTATION_TIMEOUT}s: {named}",
        )
        return
    if result.returncode != 0:
        report.error(
            "E-COMPUTATION",
            doc.rel,
            f"computation failed: {named}: {result.stderr.strip()[:120]}",
        )
    elif result.stdout.strip() != stated:
        report.error(
            "E-COMPUTATION",
            doc.rel,
            f"stated result {stated!r} but computation yields {result.stdout.strip()!r}",
        )


def _check_topics(doc: Doc, topic_names: set[str], report: Report) -> None:
    # The target, not the alias, is compared, so an alias cannot slip a name
    # past the controlled set.
    for topic, _ in field_links(doc.fm, "topics"):
        if topic not in topic_names:
            report.error(
                "E-TOPIC", doc.rel, f"topic outside the controlled topic set: {topic}"
            )


def _check_assertion(doc: Doc, docs: dict[str, Doc], report: Report) -> None:
    grounding = field_links(doc.fm, "grounding")
    if not grounding:
        report.error(
            "E-GROUNDING", doc.rel, "assertion without a single grounding anchor"
        )
    for target, block in grounding:
        if block is None:
            report.error(
                "E-ANCHOR", doc.rel, f"grounding without statement anchor: {target}"
            )
        _check_layer(target, DISTILLATE_LAYER, "grounding", doc, report)
    contested = [target for target, _ in field_links(doc.fm, "contested-with")]
    if doc.fm.get("status") == "contested" and not contested:
        report.error(
            "E-CONTESTED", doc.rel, "contested assertion without contested-with links"
        )
    for target in contested:
        other = docs.get(target)
        if other is None:
            report.error(
                "E-CONTESTED", doc.rel, f"contested counterpart missing: {target}"
            )
            continue
        back = [t for t, _ in field_links(other.fm, "contested-with")]
        if doc.rel not in back:
            report.error(
                "E-CONTESTED",
                doc.rel,
                f"one-sided contested relation: {target} does not link back",
            )
        if other.fm.get("status") != "contested":
            report.error(
                "E-CONTESTED",
                doc.rel,
                f"contested counterpart {target} is not itself at status contested",
            )


def _check_contested_coverage(
    doc: Doc, docs: dict[str, Doc], grounded: set[str], report: Report
) -> None:
    """A chapter that takes one side of a contested pair reads as settled.

    Where the sources disagree, the vault holds two assertions linked to each
    other; naming one of them and none of its counterparts turns the dispute
    into a finding the chapter does not have.
    """
    for target in sorted(grounded):
        other = docs.get(target)
        if other is None or other.fm.get("status") != "contested":
            continue
        counterparts = {t for t, _ in field_links(other.fm, "contested-with")}
        if counterparts and not counterparts & grounded:
            report.warn(
                "W-CONTESTED",
                doc.rel,
                f"grounds in the contested assertion {target} without any of its "
                f"counterparts ({', '.join(sorted(counterparts))})",
            )


def _check_chapter(doc: Doc, docs: dict[str, Doc], report: Report) -> None:
    defs: dict[str, str] = {}
    body_lines = []
    for line in doc.body.splitlines():
        if m := FOOTNOTE_DEF.match(line):
            defs[m.group(1)] = m.group(2)
        elif not line.startswith((" ", "\t")) or not defs:
            body_lines.append(line)
    refs = {m.group(1) for line in body_lines for m in FOOTNOTE_REF.finditer(line)}
    for ref in sorted(refs - set(defs)):
        report.error("E-FOOTNOTE", doc.rel, f"footnote [^{ref}] used but never defined")
    for unused in sorted(set(defs) - refs):
        report.error(
            "E-FOOTNOTE", doc.rel, f"footnote [^{unused}] defined but never used"
        )

    grounded_assertions: set[str] = set()
    posit_count = 0
    for key, text in defs.items():
        if text.startswith("Grounded in"):
            targets = [t for t, _ in link_targets(text)]
            if not targets:
                report.error(
                    "E-FOOTNOTE", doc.rel, f"footnote [^{key}] grounds in no assertion"
                )
            for target in targets:
                grounded_assertions.add(target)
                _check_layer(target, ASSERTION_LAYER, "chapter footnote", doc, report)
                other = docs.get(target)
                # A target outside the layer is E-LAYER's, a dead one E-ANCHOR's.
                if (
                    other is not None
                    and other.fm.get("type") != "assertion"
                    and target.startswith(ASSERTION_LAYER)
                ):
                    report.error(
                        "E-FOOTNOTE",
                        doc.rel,
                        f"footnote [^{key}] grounds in {target}, which is not an assertion",
                    )
        elif text.startswith("Posit:"):
            posit_count += 1
        else:
            report.error(
                "E-FOOTNOTE",
                doc.rel,
                f"footnote [^{key}] starts with neither 'Grounded in' nor 'Posit:'",
            )

    mirror = {target for target, _ in field_links(doc.fm, "assertions")}
    if mirror != grounded_assertions:
        report.error(
            "E-MIRROR",
            doc.rel,
            f"frontmatter assertions {sorted(mirror)} != footnote assertions {sorted(grounded_assertions)}",
        )
    if doc.fm.get("posits") != posit_count:
        report.error(
            "E-MIRROR",
            doc.rel,
            f"frontmatter posits {doc.fm.get('posits')} != {posit_count} posit footnotes",
        )
    _check_contested_coverage(doc, docs, grounded_assertions, report)
    _check_chapter_aliases(doc, defs, docs, report)

    paragraph = []
    for line in [*body_lines, ""]:
        if line.strip():
            paragraph.append(line)
            continue
        text = " ".join(paragraph)
        if paragraph and not text.startswith("#") and not FOOTNOTE_REF.search(text):
            report.warn(
                "W-UNANCHORED",
                doc.rel,
                f"paragraph without any footnote marker: {text[:60]}",
            )
        paragraph = []


def _check_moc_reachability(
    docs: dict[str, Doc], report: Report, scope: dict[str, Doc]
) -> None:
    mocs = [d for d in docs.values() if d.fm.get("type") == "moc"]
    listed = {target for moc in mocs for target, _ in link_targets(moc.body)}
    for doc in scope.values():
        if doc.fm.get("type") == "assertion" and doc.rel not in listed:
            report.error("E-ORPHAN", doc.rel, "assertion reachable from no topic map")


def _grounding_set(doc: Doc) -> frozenset[tuple[str, str | None]]:
    return frozenset(field_links(doc.fm, "grounding"))


def _check_duplicate_grounding(docs: dict[str, Doc], report: Report) -> None:
    """Two assertions on the same anchors say one thing twice.

    Where one anchor set contains the other, the narrower assertion carries
    nothing its counterpart does not already carry, and the two are either the
    same statement or one of them reaches past its evidence. Which of the two it
    is, is a decision for a person, so the finding is a warning. Comparison is
    over the exact anchor sets; an assertion without any anchor is left out,
    because the empty set is contained in every other and E-GROUNDING already
    speaks about it.
    """
    assertions = sorted(
        (
            (doc.rel, anchors)
            for doc in docs.values()
            if doc.fm.get("type") == "assertion" and (anchors := _grounding_set(doc))
        ),
    )
    for index, (rel, anchors) in enumerate(assertions):
        for other_rel, other in assertions[index + 1 :]:
            if anchors == other:
                narrow, wide = rel, other_rel
                relation = "rests on the same grounding anchors as"
            elif anchors < other or other < anchors:
                narrow, wide = (rel, other_rel) if anchors < other else (other_rel, rel)
                relation = "rests on grounding anchors contained in those of"
            else:
                continue
            report.warn("W-DUPLICATE-GROUNDING", narrow, f"{relation} {wide}")


def _check_chapter_aliases(
    doc: Doc, defs: dict[str, str], docs: dict[str, Doc], report: Report
) -> None:
    """A footnote alias is read as the title of what it cites.

    Where the alias differs from the H1 of the assertion, the chapter tells the
    reader something the anchor does not say, and the drift is invisible in the
    rendered text.
    """
    for key, text in defs.items():
        if not text.startswith("Grounded in"):
            continue
        for match in ALIASED_LINK.finditer(text):
            target, alias = match.group(1).strip(), match.group(2).strip()
            other = docs.get(target)
            if other is None:
                continue  # E-ANCHOR speaks about the target that does not exist
            title = H1.search(other.body)
            if title is None or title.group(1).strip() == alias:
                continue
            report.warn(
                "W-ALIAS",
                doc.rel,
                f"footnote [^{key}] renames {target} as {alias!r}, "
                f"whose title reads {title.group(1).strip()!r}",
            )


def _check_chain_populated(docs: dict[str, Doc], report: Report) -> None:
    """A vault whose production chain holds no document gave every content check an empty subject.

    Topic maps do not count. Instantiation writes one per topic into 30_assertions,
    so counting them would silence the finding for exactly the fresh vault it is for.
    """
    content = (
        doc
        for doc in docs.values()
        if doc.rel.startswith(CHAIN_FOLDERS) and doc.fm.get("type") != "moc"
    )
    if not any(content):
        report.warn(
            "W-EMPTY",
            ".",
            f"no document in the production chain ({' → '.join(CHAIN_FOLDERS)}); "
            "no content check had a subject",
        )


def anchored_blocks(docs: dict[str, Doc]) -> dict[str, set[str]]:
    """Per representation the blocks that some distillate core statement anchors."""
    anchored: dict[str, set[str]] = {}
    for doc in docs.values():
        if doc.fm.get("type") != "distillate":
            continue
        for line, _ in statement_lines(doc.body):
            for target, block in link_targets(line):
                if block is not None:
                    anchored.setdefault(target, set()).add(block)
    return anchored


def _check_coverage(docs: dict[str, Doc], report: Report, minimum: float) -> None:
    """A source whose blocks mostly carry no distillate anchor is not exhausted.

    The chain checks downwards, whether every statement has a passage, and
    nothing in it asks whether the passages were used. Every block was stamped
    as anchor-relevant at ingest, so each unanchored one is a candidate the
    distillate left behind. Only a representation that has a distillate at all
    is judged; before that, the inventory already says `ingested`.
    """
    if minimum <= 0:
        return
    anchored = anchored_blocks(docs)
    for doc in docs.values():
        if doc.fm.get("type") != "representation" or not doc.blocks:
            continue
        if doc.fm.get("source-type") != "document" or doc.rel not in anchored:
            continue
        total, used = len(set(doc.blocks)), len(anchored[doc.rel] & set(doc.blocks))
        if used / total < minimum:
            report.warn(
                "W-COVERAGE",
                doc.rel,
                f"{total - used} of {total} blocks anchored by no distillate "
                f"statement (coverage {used / total:.2f} below {minimum})",
            )


def _check_output_present(docs: dict[str, Doc], report: Report) -> None:
    """A validator must not report green on a contract that had no subject."""
    if not any(doc.fm.get("type") == "chapter" for doc in docs.values()):
        report.warn(
            "W-NO-OUTPUT",
            "40_output/",
            "no chapter document; the footnote contract does not take effect in this instance",
        )


def _resolve_chapter(spec: str, root: Path, docs: dict[str, Doc]) -> Doc | None:
    """A chapter named by root-relative path, by absolute path, or by bare slug."""
    raw = str(spec).replace("\\", "/").strip()
    if Path(raw).is_absolute():
        try:
            raw = Path(raw).resolve().relative_to(root).as_posix()
        except ValueError:
            return None
    raw = raw.removesuffix(".md").strip("/")
    for rel in (raw, f"{TYPE_FOLDER['chapter']}/{raw}"):
        doc = docs.get(rel)
        if doc is not None and doc.fm.get("type") == "chapter":
            return doc
    return None


def _links_below(doc: Doc) -> set[str]:
    """The link targets of a document that point into the layer it grounds in."""
    below = LAYER_BELOW.get(doc.fm.get("type"))
    if below is None:
        return set()
    targets = {target for _, target, _ in _frontmatter_links(doc)}
    targets |= {target for target, _ in link_targets(doc.body)}
    return {target for target in targets if target.startswith(below)}


def _chapter_scope(chapter: Doc, docs: dict[str, Doc]) -> dict[str, Doc]:
    """The chapter plus, transitively, the documents it grounds in.

    Traversal follows only anchors that point one layer down, the direction the
    schema allows, so a sideways link into a neighbouring branch does not widen
    the scope.
    """
    scope = {chapter.rel: chapter}
    queue = [chapter]
    while queue:
        current = queue.pop()
        for target in sorted(_links_below(current)):
            if target in docs and target not in scope:
                scope[target] = docs[target]
                queue.append(docs[target])
    return scope


def validate(
    root: Path,
    run_computations: bool = True,
    chapter: str | None = None,
    min_coverage: float = DEFAULT_MIN_COVERAGE,
) -> Report:
    # Resolved, because the chapter lookup and the computation trust boundary
    # compare resolved paths against it.
    root = Path(root).resolve()
    docs, report = load_docs(root, CONTENT_FOLDERS)
    reference_ids = set(load_references(root))
    topic_names = {
        str(d.fm.get("topic")) for d in docs.values() if d.fm.get("type") == "moc"
    }

    scope = docs
    if chapter is not None:
        target_doc = _resolve_chapter(chapter, root, docs)
        if target_doc is None:
            report.errors.clear()
            report.warnings.clear()
            report.error("E-SCOPE", str(chapter), "no chapter document of this name")
            return report
        scope = _chapter_scope(target_doc, docs)
        # A document that failed to parse is in no scope, so keep the parse
        # findings of those the scope anchors into.
        reachable = set(scope) | {
            t for doc in scope.values() for t in _links_below(doc)
        }
        report.errors = [e for e in report.errors if e[1] in reachable]
        report.warnings = [w for w in report.warnings if w[1] in reachable]

    for doc in scope.values():
        _check_frontmatter(doc, report)
        _check_frontmatter_links(doc, docs, root, report)
        _check_duplicate_ids(doc, report)
        doctype = doc.fm.get("type")
        if doctype in ("distillate", "assertion", "chapter"):
            _check_status_discipline(doc, report)
            _check_staleness(doc, report)
            _check_ladder(doc, docs, report)
        if doctype in ("distillate", "assertion"):
            _check_topics(doc, topic_names, report)
        if doctype == "distillate":
            _check_distillate(doc, docs, reference_ids, root, report, run_computations)
        elif doctype == "assertion":
            _check_assertion(doc, docs, report)
        elif doctype == "chapter":
            _check_chapter(doc, docs, report)
        for target, block in link_targets(doc.body):
            if block is not None or target.startswith(CONTENT_FOLDERS):
                _resolve_anchor(target, block, docs, root, doc, report)
    _check_moc_reachability(docs, report, scope)
    _check_duplicate_grounding(scope, report)
    if chapter is None:
        _check_placeholders(root, report)
        _check_chain_populated(docs, report)
        _check_output_present(docs, report)
        _check_coverage(docs, report, min_coverage)
    else:
        _check_placeholders(root, report, [doc.path for doc in scope.values()])
    return report


def main() -> int:
    utf8_console()
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("root", type=Path, help="vault root directory")
    parser.add_argument(
        "--no-computations",
        action="store_true",
        help="skip re-running data anchors",
    )
    parser.add_argument(
        "--chapter",
        metavar="40_output/<slug>",
        help="judge one chapter and the chain it hangs on, path or slug",
    )
    parser.add_argument(
        "--min-coverage",
        type=float,
        default=DEFAULT_MIN_COVERAGE,
        metavar="SHARE",
        help="share of a document's blocks distillates must anchor; 0 disables",
    )
    args = parser.parse_args()

    report = validate(
        args.root,
        run_computations=not args.no_computations,
        chapter=args.chapter,
        min_coverage=args.min_coverage,
    )
    for code, rel, message in report.errors:
        print(f"ERROR {code} {rel}: {message}", file=sys.stderr)
    for code, rel, message in report.warnings:
        print(f"WARN {code} {rel}: {message}", file=sys.stderr)
    print(f"{len(report.errors)} error(s), {len(report.warnings)} warning(s)")
    if args.chapter:
        print(f"not decidable per chapter, left out: {', '.join(VAULT_WIDE_CHECKS)}")
        ready = not report.errors and not report.warnings
        verdict = "READY" if ready else "NOT READY"
        print(f"CHAPTER {verdict} {args.chapter}")
        return 0 if ready else 1
    if not report.errors:
        print("OK vault conforms to its schema")
    return 1 if report.errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
