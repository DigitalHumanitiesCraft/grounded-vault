"""Fixture tests for tools/validate.py against the shipped fixture vaults.

tests/fixtures/minimal is the positive fixture and must pass clean;
tests/fixtures/broken carries one specimen per defect class and every class must
be caught. The warning tests use temporary vaults, because a warning states that
a check found no subject, which neither shipped fixture can show.
"""

import shutil
import sys
from pathlib import Path

REPO = Path(__file__).parents[1]
sys.path.insert(0, str(REPO / "tools"))

from validate import validate  # noqa: E402

MINIMAL = REPO / "tests" / "fixtures" / "minimal"
BROKEN = REPO / "tests" / "fixtures" / "broken"

EXPECTED_BROKEN_CODES = {
    "E-ANCHOR",  # dead block reference and dead frontmatter target
    "E-TOPIC",  # topic outside the controlled topic set
    "E-LAYER",  # anchor pointing past or beside its grounding layer
    "E-GROUNDING",  # assertion without a single grounding anchor
    "E-DUPLICATE",  # duplicate block and statement IDs
    "E-ORPHAN",  # assertion in no topic map
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
        "30_assertions/wrong-layer-grounding",
        "40_output/02-layer",
        "20_distillates/documents/sideways",
    }


def test_an_empty_grounding_list_is_an_error() -> None:
    report = validate(BROKEN)
    assert "30_assertions/empty-grounding" in _rels(report.errors, "E-GROUNDING")


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
        "W-EMPTY",
        "W-NO-INVENTORY",
        "W-NO-OUTPUT",
    }


def test_a_single_chain_document_ends_the_empty_finding(tmp_path: Path) -> None:
    doc = tmp_path / "10_markdown" / "documents"
    doc.mkdir(parents=True)
    (doc / "note.md").write_text("---\ntype: representation\n---\n", encoding="utf-8")
    report = validate(tmp_path)
    assert "W-EMPTY" not in {code for code, _, _ in report.warnings}


def test_a_populated_vault_reports_no_empty_chain() -> None:
    report = validate(MINIMAL)
    assert _rels(report.warnings, "W-EMPTY") == set()


def test_a_declared_warning_is_not_reported_as_unexpected(tmp_path: Path) -> None:
    _declare_expected_warnings(tmp_path, "W-EMPTY, W-NO-INVENTORY, W-NO-OUTPUT")
    report = validate(tmp_path)
    assert report.unexpected_warnings() == []


def test_an_undeclared_warning_stays_unexpected(tmp_path: Path) -> None:
    _declare_expected_warnings(tmp_path, "W-EMPTY, W-NO-INVENTORY")
    report = validate(tmp_path)
    assert [code for code, _, _ in report.unexpected_warnings()] == ["W-NO-OUTPUT"]


def test_a_declaration_that_no_longer_fires_is_reported(tmp_path: Path) -> None:
    _declare_expected_warnings(tmp_path, "W-NO-INVENTORY, W-NO-OUTPUT, W-GONE")
    report = validate(tmp_path)
    assert "W-STALE-EXPECTATION" in {code for code, _, _ in report.warnings}


def test_checks_older_than_the_content_are_reported() -> None:
    report = validate(BROKEN)
    assert _rels(report.warnings, "W-STALE") == {"20_distillates/documents/stale"}


def test_a_document_without_any_check_date_is_not_stale() -> None:
    """Absent check dates are status grounded, which is a state and not a defect."""
    report = validate(MINIMAL)
    assert _rels(report.warnings, "W-STALE") == set()


CHAPTER = "40_output/01-findings"

SIDE_DISTILLATE = """---
type: distillate
source-type: document
representation: "[[10_markdown/documents/report-garden-water-2026]]"
topics: ["[[Water]]"]
status: grounded
checked: {}
created: 2026-07-11
updated: 2026-07-11
---

# Distillate: side branch

## Core statements

- A statement whose anchor does not resolve. [[10_markdown/documents/report-garden-water-2026#^nope]] ^s1
"""

SIDE_ASSERTION = """---
type: assertion
topics: ["[[Water]]"]
status: grounded
checked: {}
grounding:
  - "[[20_distillates/documents/side-branch#^s1]]"
created: 2026-07-11
updated: 2026-07-11
---

# A side branch assertion

## Support

- [[20_distillates/documents/side-branch#^s1]] — what the side branch contributes.
"""

SIDE_CHAPTER = """---
type: chapter
status: grounded
checked: {}
assertions: ["[[30_assertions/side-branch]]"]
posits: 0
created: 2026-07-11
updated: 2026-07-11
---

# Side branch

A sentence of the side branch.[^1]

[^1]: Grounded in [[30_assertions/side-branch]].
"""


def _vault_with_side_branch(tmp_path: Path) -> Path:
    """A copy of the clean fixture plus a second chain that carries a dead anchor."""
    root = tmp_path / "vault"
    shutil.copytree(MINIMAL, root)
    (root / "20_distillates" / "documents" / "side-branch.md").write_text(
        SIDE_DISTILLATE, encoding="utf-8"
    )
    (root / "30_assertions" / "side-branch.md").write_text(
        SIDE_ASSERTION, encoding="utf-8"
    )
    (root / "40_output" / "02-side.md").write_text(SIDE_CHAPTER, encoding="utf-8")
    return root


def test_a_chapter_stays_clean_while_the_rest_of_the_vault_is_broken(
    tmp_path: Path,
) -> None:
    root = _vault_with_side_branch(tmp_path)
    assert validate(root).errors != []
    report = validate(root, chapter=CHAPTER)
    assert report.errors == [], report.errors
    assert report.unexpected_warnings() == [], report.warnings


def test_a_defect_in_a_branch_the_chapter_does_not_hang_on_stays_out(
    tmp_path: Path,
) -> None:
    root = _vault_with_side_branch(tmp_path)
    report = validate(root, chapter=CHAPTER)
    assert not [rel for _, rel, _ in report.errors if "side-branch" in rel]
    other = validate(root, chapter="40_output/02-side")
    assert "20_distillates/documents/side-branch" in _rels(other.errors, "E-ANCHOR")


def test_a_defect_in_a_distillate_under_the_chapter_reaches_the_verdict(
    tmp_path: Path,
) -> None:
    root = tmp_path / "vault"
    shutil.copytree(MINIMAL, root)
    distillate = root / "20_distillates" / "documents" / "report-garden-water-2026.md"
    distillate.write_text(
        distillate.read_text(encoding="utf-8").replace("#^c3d4", "#^gone"),
        encoding="utf-8",
    )
    report = validate(root, chapter=CHAPTER)
    assert "20_distillates/documents/report-garden-water-2026" in _rels(
        report.errors, "E-ANCHOR"
    )


def test_a_defect_in_a_representation_under_the_chapter_reaches_the_verdict(
    tmp_path: Path,
) -> None:
    root = tmp_path / "vault"
    shutil.copytree(MINIMAL, root)
    representation = root / "10_markdown" / "documents" / "report-garden-water-2026.md"
    representation.write_text(
        representation.read_text(encoding="utf-8").replace("channel: handover", ""),
        encoding="utf-8",
    )
    report = validate(root, chapter=CHAPTER)
    assert "10_markdown/documents/report-garden-water-2026" in _rels(
        report.errors, "E-FRONTMATTER"
    )


def test_the_chapter_is_named_by_slug_or_by_path() -> None:
    for spec in ("01-findings", CHAPTER, f"{CHAPTER}.md"):
        report = validate(MINIMAL, chapter=spec)
        assert report.errors == [], (spec, report.errors)


def test_an_unknown_chapter_is_a_finding() -> None:
    report = validate(MINIMAL, chapter="40_output/does-not-exist")
    assert "E-SCOPE" in report.codes()


def test_only_a_chapter_can_be_the_scope() -> None:
    report = validate(MINIMAL, chapter="30_assertions/metering-reduces-water-use")
    assert "E-SCOPE" in report.codes()


def test_the_vault_wide_checks_stay_out_of_the_chapter_mode(tmp_path: Path) -> None:
    root = tmp_path / "vault"
    shutil.copytree(MINIMAL, root)
    (root / "knowledge" / "state.md").unlink()
    assert "W-NO-INVENTORY" in {code for code, _, _ in validate(root).warnings}
    report = validate(root, chapter=CHAPTER)
    assert report.errors == [], report.errors
    assert report.warnings == [], report.warnings


def test_a_placeholder_under_the_chapter_is_reported(tmp_path: Path) -> None:
    root = tmp_path / "vault"
    shutil.copytree(MINIMAL, root)
    distillate = root / "20_distillates" / "documents" / "report-garden-water-2026.md"
    distillate.write_text(
        distillate.read_text(encoding="utf-8") + "\n{{OPEN_QUESTION}}\n",
        encoding="utf-8",
    )
    report = validate(root, chapter=CHAPTER)
    assert _rels(report.warnings, "W-PLACEHOLDER") == {
        "20_distillates/documents/report-garden-water-2026.md"
    }
