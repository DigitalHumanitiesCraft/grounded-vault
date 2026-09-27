"""Tests for tools/inventory.py against the shipped fixture vaults.

The generator reads the files rather than a register, so the fixture vaults are
the subject: `minimal/` carries one source per source type, and the temporary
vaults below add the states a conformant fixture cannot show, an original that
has not been ingested and a state document without the markers.
"""

import json
import shutil
from pathlib import Path

import pytest

from inventory import BEGIN, COLUMNS, END, render, rows, write

REPO = Path(__file__).parents[1]
MINIMAL = REPO / "tests" / "fixtures" / "minimal"
BROKEN = REPO / "tests" / "fixtures" / "broken"

STATE = f"""---
title: State
---

# State

## Source inventory

{BEGIN}
| Source | Type | Channel | Markdown representation | Distillate | Coverage | Status |
|---|---|---|---|---|---|---|
| stale row that predates the last ingest | | | | | |
{END}

## Open work
"""


def _row(root: Path, source_starts_with: str):
    (found,) = [r for r in rows(root) if r.source.startswith(source_starts_with)]
    return found


def test_a_distilled_document_carries_both_links() -> None:
    row = _row(MINIMAL, "Annual Water Report")
    assert row.type == "document"
    assert row.channel == "handover"
    assert row.representation == "[[10_markdown/documents/report-garden-water-2026]]"
    assert row.distillate == "[[20_distillates/documents/report-garden-water-2026]]"
    assert row.coverage == "3/3"
    assert row.status == "distilled"


def test_a_publication_row_comes_from_the_csl_record() -> None:
    row = _row(MINIMAL, "Water Metering in Community Gardens")
    assert (row.type, row.channel, row.representation) == (
        "publication",
        "import",
        "—",
    )
    assert row.distillate == "[[20_distillates/publications/example-2024-metering]]"
    assert (row.coverage, row.status) == ("—", "distilled")


def test_the_data_source_is_listed_with_its_type() -> None:
    row = _row(MINIMAL, "Quarterly water meter readings")
    assert (row.type, row.status) == ("data", "distilled")


def test_a_representation_without_a_distillate_is_ingested(tmp_path: Path) -> None:
    root = tmp_path / "vault"
    shutil.copytree(MINIMAL, root)
    (root / "20_distillates" / "documents" / "report-garden-water-2026.md").unlink()
    row = _row(root, "Annual Water Report")
    assert (row.distillate, row.coverage, row.status) == ("—", "—", "ingested")


def test_an_original_that_no_representation_names_is_new(tmp_path: Path) -> None:
    """00_sources/ is gitignored, so this state exists only on a working copy."""
    root = tmp_path / "vault"
    shutil.copytree(MINIMAL, root)
    (root / "00_sources").mkdir()
    (root / "00_sources" / "README.md").write_text("ignored", encoding="utf-8")
    (root / "00_sources" / "new-handover.pdf").write_bytes(b"%PDF-")
    row = _row(root, "new-handover.pdf")
    assert (row.representation, row.distillate, row.status) == ("—", "—", "new")
    assert not [r for r in rows(root) if r.source == "README.md"]


def test_an_original_already_ingested_raises_no_second_row(tmp_path: Path) -> None:
    root = tmp_path / "vault"
    shutil.copytree(MINIMAL, root)
    (root / "00_sources").mkdir()
    (root / "00_sources" / "report-garden-water-2026.pdf").write_bytes(b"%PDF-")
    assert not [r for r in rows(root) if r.source.endswith(".pdf")]


def test_two_distillates_of_one_source_both_appear() -> None:
    """The schema forbids the state, so the inventory has to show it.

    The broken fixture hangs several distillates on one representation; keying
    the table by the representation alone would silently drop all but one.
    """
    listed = [
        row.distillate
        for row in rows(BROKEN)
        if row.representation == "[[10_markdown/documents/note]]"
    ]
    assert len(listed) == len(set(listed)) > 1


def test_a_missing_source_folder_is_no_finding() -> None:
    assert not (MINIMAL / "00_sources").exists()
    assert rows(MINIMAL)


def test_the_table_carries_the_declared_columns() -> None:
    table = render(rows(MINIMAL)).splitlines()
    assert table[0] == "| " + " | ".join(COLUMNS) + " |"
    assert table[1] == "|---|---|---|---|---|---|---|"
    assert all(line.count(" | ") == len(COLUMNS) - 1 for line in table[2:])


@pytest.mark.parametrize("fixture", [MINIMAL, BROKEN], ids=["minimal", "broken"])
def test_the_fixture_inventory_is_what_the_generator_writes(fixture: Path) -> None:
    """The shipped state documents are generator output, never hand edits."""
    text = (fixture / "knowledge" / "state.md").read_bytes().decode("utf-8")
    text = text.replace("\r\n", "\n")
    block = text[text.index(BEGIN) + len(BEGIN) : text.index(END)].strip("\n")
    assert block == render(rows(fixture))


def test_write_replaces_the_marked_block(tmp_path: Path) -> None:
    root = tmp_path / "vault"
    shutil.copytree(MINIMAL, root)
    (root / "knowledge" / "state.md").write_text(STATE, encoding="utf-8")
    table = render(rows(root))
    write(root, table)
    text = (root / "knowledge" / "state.md").read_text(encoding="utf-8")
    assert f"{BEGIN}\n{table}\n{END}" in text
    assert "stale row that predates the last ingest" not in text
    assert text.startswith("---\ntitle: State\n---")
    assert text.rstrip().endswith("## Open work")


def test_write_is_idempotent(tmp_path: Path) -> None:
    root = tmp_path / "vault"
    shutil.copytree(MINIMAL, root)
    (root / "knowledge" / "state.md").write_text(STATE, encoding="utf-8")
    write(root, render(rows(root)))
    once = (root / "knowledge" / "state.md").read_text(encoding="utf-8")
    write(root, render(rows(root)))
    assert (root / "knowledge" / "state.md").read_text(encoding="utf-8") == once


def test_missing_markers_are_a_clear_error(tmp_path: Path) -> None:
    root = tmp_path / "vault"
    shutil.copytree(MINIMAL, root)
    (root / "knowledge" / "state.md").write_text(
        "---\ntitle: State\n---\n\n# State\n", encoding="utf-8"
    )
    error = write(root, "| |")
    assert error is not None and BEGIN in error


def test_a_missing_state_document_is_a_clear_error(tmp_path: Path) -> None:
    error = write(tmp_path, "| |")
    assert error is not None and "knowledge/state.md" in error


@pytest.mark.parametrize("newline", ["\n", "\r\n"], ids=["lf", "crlf"])
def test_write_keeps_the_line_endings_of_the_state_document(
    tmp_path: Path, newline: str
) -> None:
    """Either ending survives on every platform, so a rewrite diffs only in content."""
    root = tmp_path / "vault"
    shutil.copytree(MINIMAL, root)
    path = root / "knowledge" / "state.md"
    path.write_bytes(STATE.replace("\n", newline).encode("utf-8"))
    assert write(root, render(rows(root))) is None
    raw = path.read_bytes()
    assert b"Water Metering" in raw
    crlf = raw.count(b"\r\n")
    assert crlf == (raw.count(b"\n") if newline == "\r\n" else 0)


def test_a_document_that_does_not_parse_is_reported() -> None:
    """The row is lost with the frontmatter, so the loss has to be said."""
    problems: list[str] = []
    rows(BROKEN, problems)
    assert problems == [
        "20_distillates/documents/not-a-mapping: E-FRONTMATTER frontmatter is not a mapping",
        "20_distillates/documents/unterminated: E-FRONTMATTER unterminated frontmatter",
    ]


def test_a_single_reference_object_yields_its_row(tmp_path: Path) -> None:
    root = tmp_path / "vault"
    shutil.copytree(MINIMAL, root)
    path = root / "references" / "example-corpus.csl.json"
    path.write_text(
        json.dumps(json.loads(path.read_text(encoding="utf-8"))[0]), encoding="utf-8"
    )
    assert _row(root, "Water Metering in Community Gardens").status == "distilled"


def test_an_unreadable_reference_file_is_reported(tmp_path: Path) -> None:
    root = tmp_path / "vault"
    shutil.copytree(MINIMAL, root)
    (root / "references" / "broken.json").write_text("[{", encoding="utf-8")
    problems: list[str] = []
    rows(root, problems)
    assert [p.split(":")[0] for p in problems] == ["references/broken.json"]


def test_coverage_counts_the_blocks_the_distillates_anchor(tmp_path: Path) -> None:
    root = tmp_path / "vault"
    shutil.copytree(MINIMAL, root)
    path = root / "10_markdown" / "documents" / "report-garden-water-2026.md"
    path.write_text(
        path.read_text(encoding="utf-8") + "\nAn unread paragraph. ^u0\n",
        encoding="utf-8",
    )
    assert _row(root, "Annual Water Report").coverage == "3/4"
