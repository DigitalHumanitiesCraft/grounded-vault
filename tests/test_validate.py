"""Fixture tests for tools/validate.py against the shipped example instances.

examples/minimal is the positive fixture and must pass clean; examples/broken
carries one specimen per defect class and every class must be caught. The
warning tests use temporary vaults, because a warning states that a check found
no subject, which neither shipped fixture can show.
"""

import sys
from pathlib import Path

REPO = Path(__file__).parents[1]
sys.path.insert(0, str(REPO / "tools"))

from validate import validate  # noqa: E402

MINIMAL = REPO / "examples" / "minimal"
BROKEN = REPO / "examples" / "broken"

EXPECTED_BROKEN_CODES = {
    "E-ANCHOR",  # dead block reference and dead frontmatter target
    "E-TOPIC",  # topic outside the controlled topic set
    "E-LAYER",  # anchor pointing past or beside its grounding layer
    "E-GROUNDING",  # claim without a single grounding anchor
    "E-DUPLICATE",  # duplicate block and statement IDs
    "E-ORPHAN",  # claim in no topic map
    "E-CONTESTED",  # one-sided contested relation
    "E-FRONTMATTER",  # illegal status value
    "E-STATUS",  # status without recorded checks
    "E-FOOTNOTE",  # wrong keyword and undefined marker
    "E-MIRROR",  # frontmatter mirror out of sync
    "E-COMPUTATION",  # computation script missing
    "E-QUOTE",  # intake-time quotation check not recorded
    "E-INVENTORY",  # document in no inventory register
}

SPECIFICATION = """---
title: Specification
expected-warnings: [{expected}]
---

# Specification
"""


def _rels(entries: list[tuple[str, str, str]], code: str) -> set[str]:
    return {rel for found, rel, _ in entries if found == code}


def _declare_expected_warnings(root: Path, expected: str) -> None:
    (root / "knowledge").mkdir(exist_ok=True)
    (root / "knowledge" / "specification.md").write_text(
        SPECIFICATION.format(expected=expected), encoding="utf-8"
    )


def test_minimal_is_clean() -> None:
    report = validate(MINIMAL)
    assert report.errors == [], report.errors


def test_minimal_computations_reproduce_by_default() -> None:
    report = validate(MINIMAL)
    assert report.errors == [], report.errors


def test_computations_can_be_switched_off() -> None:
    report = validate(MINIMAL, run_computations=False)
    assert report.errors == [], report.errors


def test_minimal_raises_no_warning() -> None:
    report = validate(MINIMAL)
    assert report.warnings == [], report.warnings


def test_broken_catches_every_defect_class() -> None:
    report = validate(BROKEN)
    missing = EXPECTED_BROKEN_CODES - report.codes()
    assert not missing, f"defect classes not caught: {missing}"


def test_broken_reports_no_false_alarms_outside_expected_classes() -> None:
    report = validate(BROKEN)
    unexpected = report.codes() - EXPECTED_BROKEN_CODES
    assert not unexpected, f"unexpected error classes: {unexpected}"


def test_every_layer_violation_is_caught_at_its_own_layer() -> None:
    report = validate(BROKEN)
    assert _rels(report.errors, "E-LAYER") == {
        "30_claims/wrong-layer-grounding",
        "40_deliverable/02-layer",
        "20_distillates/documents/sideways",
    }


def test_an_empty_grounding_list_is_an_error() -> None:
    report = validate(BROKEN)
    assert "30_claims/empty-grounding" in _rels(report.errors, "E-GROUNDING")


def test_duplicate_block_and_statement_ids_are_caught() -> None:
    report = validate(BROKEN)
    assert _rels(report.errors, "E-DUPLICATE") == {
        "10_markdown/documents/duplicate-blocks",
        "20_distillates/documents/duplicate-statements",
    }


def test_dead_frontmatter_targets_are_resolved() -> None:
    report = validate(BROKEN)
    messages = [
        message
        for code, rel, message in report.errors
        if code == "E-ANCHOR" and rel == "20_distillates/documents/dead-representation"
    ]
    assert len(messages) == 2, messages


def test_a_surviving_template_placeholder_is_a_warning() -> None:
    report = validate(BROKEN)
    placeholders = [w for w in report.warnings if w[0] == "W-PLACEHOLDER"]
    assert [rel for _, rel, _ in placeholders] == [
        "10_markdown/documents/placeholder-note.md"
    ]
    assert "PROJECT_NAME" in placeholders[0][2]


def test_placeholders_are_scanned_outside_the_content_folders(tmp_path: Path) -> None:
    (tmp_path / "knowledge").mkdir()
    (tmp_path / "knowledge" / "index.md").write_text("{{LANGUAGE}}", encoding="utf-8")
    (tmp_path / "CLAUDE.md").write_text("{{HARNESS_RULES}}", encoding="utf-8")
    (tmp_path / "HOME.md").write_text("{{PROJECT_NAME}}", encoding="utf-8")
    report = validate(tmp_path)
    assert _rels(report.warnings, "W-PLACEHOLDER") == {
        "knowledge/index.md",
        "CLAUDE.md",
        "HOME.md",
    }


def test_an_empty_vault_says_which_checks_had_no_subject(tmp_path: Path) -> None:
    report = validate(tmp_path)
    assert report.errors == []
    assert {code for code, _, _ in report.warnings} == {
        "W-NO-INVENTORY",
        "W-NO-DELIVERABLE",
    }


def test_a_declared_warning_is_not_reported_as_unexpected(tmp_path: Path) -> None:
    _declare_expected_warnings(tmp_path, "W-NO-INVENTORY, W-NO-DELIVERABLE")
    report = validate(tmp_path)
    assert report.unexpected_warnings() == []


def test_an_undeclared_warning_stays_unexpected(tmp_path: Path) -> None:
    _declare_expected_warnings(tmp_path, "W-NO-INVENTORY")
    report = validate(tmp_path)
    assert [code for code, _, _ in report.unexpected_warnings()] == ["W-NO-DELIVERABLE"]


def test_a_declaration_that_no_longer_fires_is_reported(tmp_path: Path) -> None:
    _declare_expected_warnings(tmp_path, "W-NO-INVENTORY, W-NO-DELIVERABLE, W-GONE")
    report = validate(tmp_path)
    assert "W-STALE-EXPECTATION" in {code for code, _, _ in report.warnings}
