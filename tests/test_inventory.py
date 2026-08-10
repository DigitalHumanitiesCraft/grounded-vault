"""Tests for tools/inventory.py against the shipped fixture vaults.

The generator reads the files rather than a register, so the fixture vaults are
the subject: `minimal/` carries one source per source type, and the temporary
vaults below add the states a conformant fixture cannot show, an original that
has not been ingested and a state document without the markers.
"""

import shutil
import sys
from pathlib import Path

import pytest

REPO = Path(__file__).parents[1]
sys.path.insert(0, str(REPO / "tools"))

from inventory import BEGIN, END, render, rows, write  # noqa: E402

MINIMAL = REPO / "tests" / "fixtures" / "minimal"

STATE = f"""---
title: State
---

# State

## Source inventory

{BEGIN}
| Source | Type | Channel | Markdown representation | Distillate | Status |
|---|---|---|---|---|---|
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
    assert row.status == "distilled"


def test_a_publication_row_comes_from_the_csl_record() -> None:
    row = _row(MINIMAL, "Water Metering in Community Gardens")
    assert (row.type, row.channel, row.representation) == (
        "publication",
        "import",
        "—",
    )
    assert row.distillate == "[[20_distillates/publications/example-2024-metering]]"
    assert row.status == "distilled"


def test_the_data_source_is_listed_with_its_type() -> None:
    row = _row(MINIMAL, "Quarterly water meter readings")
    assert (row.type, row.status) == ("data", "distilled")


def test_a_representation_without_a_distillate_is_ingested(tmp_path: Path) -> None:
    root = tmp_path / "vault"
    shutil.copytree(MINIMAL, root)
    (root / "20_distillates" / "documents" / "report-garden-water-2026.md").unlink()
    row = _row(root, "Annual Water Report")
    assert (row.distillate, row.status) == ("—", "ingested")


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
    broken = REPO / "tests" / "fixtures" / "broken"
    listed = [
        row.distillate
        for row in rows(broken)
        if row.representation == "[[10_markdown/documents/note]]"
    ]
    assert len(listed) == len(set(listed)) > 1


def test_a_missing_source_folder_is_no_finding() -> None:
    assert not (MINIMAL / "00_sources").exists()
    assert rows(MINIMAL)


def test_the_table_carries_the_declared_columns() -> None:
    table = render(rows(MINIMAL)).splitlines()
    assert table[0] == (
        "| Source | Type | Channel | Markdown representation | Distillate | Status |"
    )
    assert table[1] == "|---|---|---|---|---|---|"
    assert len(table) == 2 + len(rows(MINIMAL))


def test_the_generated_table_is_stable() -> None:
    assert render(rows(MINIMAL)) == render(rows(MINIMAL))


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
    with pytest.raises(SystemExit) as raised:
        write(root, "| |")
    assert BEGIN in str(raised.value)


def test_a_missing_state_document_is_a_clear_error(tmp_path: Path) -> None:
    with pytest.raises(SystemExit) as raised:
        write(tmp_path, "| |")
    assert "knowledge/state.md" in str(raised.value)
