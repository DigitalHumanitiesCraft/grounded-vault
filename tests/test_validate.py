"""Fixture tests for tools/validate.py against the shipped fixture vaults.

tests/fixtures/minimal is the positive fixture and must pass clean;
tests/fixtures/broken carries one specimen per defect class and every class must
be caught. The warning tests use temporary vaults, because a warning states that
a check found no subject, which neither shipped fixture can show.
"""

import json
import re
import shutil
import subprocess
import sys
from pathlib import Path

import pytest

from validate import (
    VAULT_WIDE_CHECKS,
    Report,
    load_references,
    parse_doc,
    split_frontmatter,
    validate,
)

REPO = Path(__file__).parents[1]

MINIMAL = REPO / "tests" / "fixtures" / "minimal"
BROKEN = REPO / "tests" / "fixtures" / "broken"

# The sub-rules of each code are pinned one by one in BROKEN_FINDINGS below.
EXPECTED_BROKEN_CODES = {
    "E-ANCHOR",
    "E-TOPIC",
    "E-LAYER",
    "E-GROUNDING",
    "E-DUPLICATE",
    "E-ORPHAN",
    "E-CONTESTED",
    "E-FRONTMATTER",
    "E-STATEMENT",
    "E-STATUS",
    "E-LADDER",
    "E-FOOTNOTE",
    "E-MIRROR",
    "E-COMPUTATION",
    "E-QUOTE",
}

DOC_DEFECTS = "20_distillates/documents/statement-defects"
COMPUTATION_DEFECTS = "20_distillates/data/computation-defects"
INCOMPLETE = "10_markdown/documents/incomplete-representation"

# One entry per sub-rule of an error code: the code, the specimen and a part of
# the message only that sub-rule writes. A code can keep firing from one branch
# while another branch has gone silent, which a test on codes alone never sees.
BROKEN_FINDINGS = [
    ("E-ANCHOR", "20_distillates/documents/note", "block ^dead not found"),
    ("E-ANCHOR", "10_markdown/data/dead-data", "does-not-exist.csv"),
    (
        "E-ANCHOR",
        "30_assertions/grounding-without-statement",
        "without statement anchor",
    ),
    ("E-ANCHOR", "20_distillates/publications/no-quote-check", "not in references/"),
    ("E-TOPIC", "20_distillates/documents/note", "outside the controlled topic set"),
    (
        "E-LAYER",
        "20_distillates/documents/representation-wrong-layer",
        "representation must",
    ),
    ("E-LAYER", "20_distillates/documents/sideways", "distillate statement must"),
    ("E-LAYER", "30_assertions/wrong-layer-grounding", "grounding must"),
    ("E-LAYER", "40_output/02-layer", "chapter footnote must"),
    ("E-GROUNDING", "30_assertions/empty-grounding", "without a single grounding"),
    ("E-DUPLICATE", "10_markdown/documents/duplicate-blocks", "duplicate block ID"),
    (
        "E-DUPLICATE",
        "20_distillates/documents/duplicate-statements",
        "duplicate statement ID",
    ),
    ("E-ORPHAN", "30_assertions/orphan-assertion", "reachable from no topic map"),
    ("E-CONTESTED", "30_assertions/contested-alone", "without contested-with links"),
    ("E-CONTESTED", "30_assertions/contested-missing", "counterpart missing"),
    ("E-CONTESTED", "30_assertions/one-sided", "does not link back"),
    ("E-CONTESTED", "30_assertions/one-sided", "not itself at status contested"),
    (
        "E-FRONTMATTER",
        "20_distillates/documents/unterminated",
        "unterminated frontmatter",
    ),
    ("E-FRONTMATTER", "20_distillates/documents/not-a-mapping", "not a mapping"),
    (
        "E-FRONTMATTER",
        "20_distillates/publications/illegal-channel",
        "illegal channel for a publication",
    ),
    (
        "E-FRONTMATTER",
        "30_assertions/misplaced-glossary",
        "does not belong in this folder",
    ),
    (
        "E-FRONTMATTER",
        "30_assertions/misplaced-glossary",
        "missing required field: term",
    ),
    ("E-FRONTMATTER", "30_assertions/bad-status", "illegal status value"),
    (
        "E-FRONTMATTER",
        "20_distillates/documents/illegal-source-type",
        "illegal source-type",
    ),
    (
        "E-FRONTMATTER",
        "20_distillates/publications/no-reference",
        "needs a reference id",
    ),
    (
        "E-FRONTMATTER",
        "20_distillates/documents/no-representation",
        "needs a representation link",
    ),
    (
        "E-FRONTMATTER",
        "20_distillates/documents/unquoted-topics",
        "not a quoted wikilink",
    ),
    ("E-FRONTMATTER", INCOMPLETE, "missing required field: source"),
    ("E-FRONTMATTER", INCOMPLETE, "missing required field: converter"),
    ("E-FRONTMATTER", INCOMPLETE, "metadata must be a mapping"),
    ("E-FRONTMATTER", "10_markdown/data/no-data", "missing required field: data"),
    (
        "E-FRONTMATTER",
        "10_markdown/documents/publication-representation",
        "publication has no Markdown representation",
    ),
    (
        "E-STATEMENT",
        "20_distillates/documents/no-core-statements",
        "no core statements",
    ),
    ("E-STATEMENT", "20_distillates/documents/no-statement-id", "without statement ID"),
    (
        "E-STATEMENT",
        "20_distillates/documents/appraisal-anchor",
        "outside the Core statements",
    ),
    ("E-STATEMENT", DOC_DEFECTS, "without block anchor"),
    ("E-STATEMENT", DOC_DEFECTS, "carries 2 block anchors"),
    ("E-STATEMENT", DOC_DEFECTS, "not into its representation"),
    (
        "E-STATEMENT",
        "20_distillates/publications/malformed-quotation",
        "without a quotation",
    ),
    ("E-STATEMENT", COMPUTATION_DEFECTS, "without computation"),
    ("E-STATUS", "30_assertions/validated-unchecked", "without checked.validation"),
    ("E-STATUS", "20_distillates/documents/checked-not-a-map", "checked must be a map"),
    ("E-STATUS", "20_distillates/documents/checked-bad-date", "records no ISO date"),
    ("E-LADDER", "30_assertions/ladder-jump", "above its anchor"),
    ("E-FOOTNOTE", "40_output/01-bad", "starts with neither"),
    ("E-FOOTNOTE", "40_output/01-bad", "used but never defined"),
    ("E-FOOTNOTE", "40_output/06-footnotes", "defined but never used"),
    ("E-FOOTNOTE", "40_output/06-footnotes", "grounds in no assertion"),
    ("E-FOOTNOTE", "40_output/06-footnotes", "which is not an assertion"),
    ("E-MIRROR", "40_output/01-bad", "frontmatter assertions"),
    ("E-MIRROR", "40_output/07-posits", "frontmatter posits 2 != 1"),
    (
        "E-COMPUTATION",
        "20_distillates/data/missing-script",
        "computation script missing",
    ),
    (
        "E-COMPUTATION",
        "20_distillates/data/outside-analysis",
        "outside tools/analysis/",
    ),
    (
        "E-COMPUTATION",
        COMPUTATION_DEFECTS,
        "outside tools/analysis/: tools/analysis/../../",
    ),
    ("E-COMPUTATION", COMPUTATION_DEFECTS, "no script named"),
    ("E-COMPUTATION", COMPUTATION_DEFECTS, "takes no arguments"),
    (
        "E-COMPUTATION",
        COMPUTATION_DEFECTS,
        "computation failed: tools/analysis/fails.py",
    ),
    (
        "E-COMPUTATION",
        COMPUTATION_DEFECTS,
        "stated result '41' but computation yields '42'",
    ),
    ("E-QUOTE", "20_distillates/publications/no-quote-check", "checked.quote"),
]

# Warnings the broken fixture carries; each has its own test below, because the
# broken-fixture tests above speak about error codes only.
EXPECTED_BROKEN_WARNINGS = {
    "W-PLACEHOLDER",  # test_a_surviving_template_placeholder_is_a_warning
    "W-STALE",  # test_checks_older_than_the_content_are_reported
    "W-UNANCHORED",  # test_a_paragraph_without_a_footnote_marker_is_a_warning
    "W-CONTESTED",  # test_a_chapter_taking_one_side_of_a_contested_pair_is_reported
    "W-DUPLICATE-GROUNDING",  # test_two_assertions_on_the_same_anchors_are_reported
    "W-ALIAS",  # test_a_footnote_alias_that_renames_its_assertion_is_reported
    "W-VERSION",  # test_a_quotation_check_without_a_text_version_is_reported
}

# Codes no fixture can carry, because they need a vault state a conformant file
# set does not have; each is asserted from a temporary vault instead.
EXPECTED_TEMPORARY_VAULT_CODES = {
    "E-SCOPE",  # test_an_unknown_chapter_is_a_finding
    "W-EMPTY",  # test_an_empty_vault_says_which_checks_had_no_subject
    "W-NO-OUTPUT",  # test_an_empty_vault_says_which_checks_had_no_subject
    "W-COVERAGE",  # test_a_source_the_distillates_mostly_leave_unanchored_is_reported
}

EMITTED_CODE = re.compile(r"report\.(?:error|warn)\(\s*\"([EW]-[A-Z-]+)\"")


def _rels(entries: list[tuple[str, str, str]], code: str) -> set[str]:
    return {rel for found, rel, _ in entries if found == code}


def test_minimal_is_clean_with_its_computations_rerun() -> None:
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


@pytest.fixture(scope="module")
def broken_errors() -> list[tuple[str, str, str]]:
    return validate(BROKEN).errors


@pytest.mark.parametrize(("code", "rel", "part"), BROKEN_FINDINGS)
def test_every_sub_rule_fires_on_its_specimen(
    broken_errors: list[tuple[str, str, str]], code: str, rel: str, part: str
) -> None:
    messages = [m for c, r, m in broken_errors if c == code and r == rel]
    assert any(part in m for m in messages), messages


def test_every_code_the_validator_emits_has_a_specimen() -> None:
    """No finding class may exist that the suite never sees fire.

    The registries above are the claim of coverage, and this test holds them
    against the codes actually emitted, so that a new check without a specimen
    fails here and a registry entry the validator no longer raises does too.
    """
    source = (REPO / "tools" / "validate.py").read_text(encoding="utf-8")
    emitted = set(EMITTED_CODE.findall(source))
    covered = (
        EXPECTED_BROKEN_CODES
        | EXPECTED_BROKEN_WARNINGS
        | EXPECTED_TEMPORARY_VAULT_CODES
    )
    assert emitted - covered == set(), (
        f"finding classes without a specimen: {emitted - covered}"
    )
    assert covered - emitted == set(), (
        f"specimens for codes never emitted: {covered - emitted}"
    )


def test_operations_documents_exactly_the_emitted_codes() -> None:
    # The code table in operations.md § Check is what agents read to act on a
    # finding, so a code missing there is a finding nobody can interpret.
    source = (REPO / "tools" / "validate.py").read_text(encoding="utf-8")
    operations = (REPO / "knowledge" / "operations.md").read_text(encoding="utf-8")
    documented = set(re.findall(r"^\| `([EW]-[A-Z-]+)`", operations, re.MULTILINE))
    assert documented == set(EMITTED_CODE.findall(source))


def test_every_layer_violation_is_caught_at_its_own_layer() -> None:
    report = validate(BROKEN)
    assert _rels(report.errors, "E-LAYER") == {
        "30_assertions/wrong-layer-grounding",
        "40_output/02-layer",
        "20_distillates/documents/sideways",
        "20_distillates/documents/representation-wrong-layer",
    }


def test_an_empty_grounding_list_is_an_error() -> None:
    report = validate(BROKEN)
    assert "30_assertions/empty-grounding" in _rels(report.errors, "E-GROUNDING")


def test_duplicate_block_and_statement_ids_are_caught() -> None:
    report = validate(BROKEN)
    assert {
        rel
        for code, rel, message in report.errors
        if code == "E-DUPLICATE"
        and ("duplicate block ID" in message or "duplicate statement ID" in message)
    } == {
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
        "10_markdown/documents/placeholder-note"
    ]
    assert "PROJECT_NAME" in placeholders[0][2]


def test_placeholders_are_scanned_outside_the_content_folders(tmp_path: Path) -> None:
    (tmp_path / "knowledge").mkdir()
    (tmp_path / "knowledge" / "index.md").write_text("{{LANGUAGE}}", encoding="utf-8")
    (tmp_path / "CLAUDE.md").write_text("{{HARNESS_RULES}}", encoding="utf-8")
    (tmp_path / "HOME.md").write_text("{{PROJECT_NAME}}", encoding="utf-8")
    report = validate(tmp_path)
    assert _rels(report.warnings, "W-PLACEHOLDER") == {
        "knowledge/index",
        "CLAUDE",
        "HOME",
    }


def test_an_empty_vault_says_which_checks_had_no_subject(tmp_path: Path) -> None:
    report = validate(tmp_path)
    assert report.errors == []
    assert {code for code, _, _ in report.warnings} == {"W-EMPTY", "W-NO-OUTPUT"}


def test_a_single_chain_document_ends_the_empty_finding(tmp_path: Path) -> None:
    doc = tmp_path / "10_markdown" / "documents"
    doc.mkdir(parents=True)
    (doc / "note.md").write_text("---\ntype: representation\n---\n", encoding="utf-8")
    report = validate(tmp_path)
    assert "W-EMPTY" not in {code for code, _, _ in report.warnings}


def test_the_topic_maps_of_a_fresh_instance_do_not_count_as_content(
    tmp_path: Path,
) -> None:
    """Instantiation writes one topic map per topic, and they land in 30_assertions.

    Counting them would hide the empty chain of every freshly instantiated vault,
    the very state the finding exists for.
    """
    moc = tmp_path / "30_assertions"
    moc.mkdir(parents=True)
    (moc / "MOC-Provenance.md").write_text(
        "---\ntype: moc\ntopic: Provenance\ncreated: 2026-08-09\nupdated: 2026-08-09\n---\n\n"
        "# Provenance\n",
        encoding="utf-8",
    )
    report = validate(tmp_path)
    assert "W-EMPTY" in {code for code, _, _ in report.warnings}


def test_a_populated_vault_reports_no_empty_chain() -> None:
    report = validate(MINIMAL)
    assert _rels(report.warnings, "W-EMPTY") == set()


def _run_cli(root: Path, *args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(REPO / "tools" / "validate.py"), str(root), *args],
        capture_output=True,
        text=True,
        check=False,
    )


def test_a_warning_alone_does_not_fail_the_full_run(tmp_path: Path) -> None:
    """Over the whole vault a warning is a finding to read, never a verdict."""
    root = _vault_with_a_placeholder(tmp_path)
    result = _run_cli(root, "--no-computations")
    assert result.returncode == 0, result.stderr
    assert "W-PLACEHOLDER" in result.stderr
    assert "1 error(s), 0 warning(s)" not in result.stdout
    assert "0 error(s), 1 warning(s)" in result.stdout


def test_a_warning_fails_the_chapter_mode(tmp_path: Path) -> None:
    """There the run answers whether this chapter may be accepted."""
    root = _vault_with_a_placeholder(tmp_path)
    result = _run_cli(root, "--no-computations", "--chapter", CHAPTER)
    assert result.returncode == 1, result.stdout
    assert "CHAPTER NOT READY" in result.stdout


def test_a_chapter_without_a_finding_is_ready(tmp_path: Path) -> None:
    result = _run_cli(MINIMAL, "--no-computations", "--chapter", CHAPTER)
    assert result.returncode == 0, result.stderr
    assert "CHAPTER READY" in result.stdout


def _vault_with_a_placeholder(tmp_path: Path) -> Path:
    """A clean vault whose chapter chain carries one warning and no error."""
    root = tmp_path / "vault"
    shutil.copytree(MINIMAL, root)
    distillate = root / "20_distillates" / "documents" / "report-garden-water-2026.md"
    distillate.write_text(
        distillate.read_text(encoding="utf-8") + "\n{{OPEN_QUESTION}}\n",
        encoding="utf-8",
    )
    return root


def test_checks_older_than_the_content_are_reported() -> None:
    report = validate(BROKEN)
    assert _rels(report.warnings, "W-STALE") == {"20_distillates/documents/stale"}


def test_a_document_without_any_check_date_is_not_stale() -> None:
    """Absent check dates are status grounded, which is a state and not a defect."""
    report = validate(MINIMAL)
    assert _rels(report.warnings, "W-STALE") == set()


@pytest.mark.parametrize("old_check", ["machine-review", "verification"])
def test_fresh_validation_does_not_hide_an_older_review(
    tmp_path: Path, old_check: str
) -> None:
    """Each check covers its own content state, even after validation is rerun."""
    root = tmp_path / "vault"
    shutil.copytree(MINIMAL, root)
    rel = "30_assertions/metering-reduces-water-use"
    path = root / f"{rel}.md"
    text = path.read_text(encoding="utf-8")
    text = text.replace(
        "checked: {}", f"checked:\n  validation: 2026-07-12\n  {old_check}: 2026-07-11"
    )
    text = text.replace("updated: 2026-07-11", "updated: 2026-07-12")
    path.write_text(text, encoding="utf-8")
    findings = [
        (code, target, message)
        for code, target, message in validate(root).warnings
        if code == "W-STALE" and target == rel
    ]
    assert len(findings) == 1
    assert old_check in findings[0][2]


CHECKED = "checked:\n  validation: 2026-07-11\n  machine-review: 2026-07-11"
CHAIN_UNDER_THE_CHAPTER = (
    "20_distillates/documents/report-garden-water-2026.md",
    "20_distillates/data/water-readings-2025.md",
    "20_distillates/publications/example-2024-metering.md",
    "30_assertions/metering-reduces-water-use.md",
)


def _raise_chain_to(tmp_path: Path, status: str) -> Path:
    """A copy of the clean fixture whose chain below the chapter carries `status`."""
    root = tmp_path / "vault"
    shutil.copytree(MINIMAL, root)
    for rel in CHAIN_UNDER_THE_CHAPTER:
        path = root / rel
        text = path.read_text(encoding="utf-8")
        text = text.replace("status: grounded", f"status: {status}")
        text = text.replace("checked: {}", CHECKED)
        text = text.replace(
            "checked:\n  quote: 2026-07-11", f"{CHECKED}\n  quote: 2026-07-11"
        )
        path.write_text(text, encoding="utf-8")
    return root


def test_a_paragraph_without_a_footnote_marker_is_a_warning() -> None:
    report = validate(BROKEN)
    assert _rels(report.warnings, "W-UNANCHORED") == {"40_output/03-unanchored"}


def test_an_id_minted_outside_the_core_statements_is_caught() -> None:
    """An appraisal line carrying an ID would be citable as if it were evidence."""
    report = validate(BROKEN)
    assert "20_distillates/documents/appraisal-anchor" in _rels(
        report.errors, "E-STATEMENT"
    )


def test_an_appraisal_section_raises_nothing_on_its_own() -> None:
    """The clean fixture carries the appraisal, which stays off the anchor surface."""
    distillate = (
        MINIMAL / "20_distillates" / "documents" / "report-garden-water-2026.md"
    )
    assert "## Appraisal" in distillate.read_text(encoding="utf-8")
    report = validate(MINIMAL)
    assert report.errors == [], report.errors
    assert report.warnings == [], report.warnings


def test_two_assertions_on_the_same_anchors_are_reported() -> None:
    """Two assertions carried by the same evidence are one assertion said twice."""
    report = validate(BROKEN)
    assert _rels(report.warnings, "W-DUPLICATE-GROUNDING") == {
        "30_assertions/duplicate-grounding-a"
    }
    (message,) = [m for c, _, m in report.warnings if c == "W-DUPLICATE-GROUNDING"]
    assert "30_assertions/duplicate-grounding-b" in message


def test_an_assertion_whose_anchors_are_contained_in_another_is_reported(
    tmp_path: Path,
) -> None:
    """A subset carries nothing its superset does not already carry."""
    root = tmp_path / "vault"
    shutil.copytree(BROKEN, root)
    narrower = root / "30_assertions" / "duplicate-grounding-b.md"
    narrower.write_text(
        narrower.read_text(encoding="utf-8").replace(
            '  - "[[20_distillates/documents/note#^s8]]"\n', ""
        ),
        encoding="utf-8",
    )
    report = validate(root)
    (message,) = [m for c, _, m in report.warnings if c == "W-DUPLICATE-GROUNDING"]
    assert "contained in" in message


def test_distinct_grounding_sets_raise_nothing() -> None:
    report = validate(MINIMAL)
    assert _rels(report.warnings, "W-DUPLICATE-GROUNDING") == set()


def test_an_assertion_without_grounding_is_no_duplicate_of_anything() -> None:
    """The empty set is contained in every other, and E-GROUNDING already speaks."""
    report = validate(BROKEN)
    assert "30_assertions/empty-grounding" not in {
        rel for code, rel, message in report.warnings if code == "W-DUPLICATE-GROUNDING"
    }
    assert not [
        m
        for c, _, m in report.warnings
        if c == "W-DUPLICATE-GROUNDING" and "empty-grounding" in m
    ]


def test_a_footnote_alias_that_renames_its_assertion_is_reported() -> None:
    report = validate(BROKEN)
    assert _rels(report.warnings, "W-ALIAS") == {"40_output/05-alias"}


def test_an_alias_equal_to_the_title_of_its_target_is_silent(tmp_path: Path) -> None:
    root = tmp_path / "vault"
    shutil.copytree(BROKEN, root)
    chapter = root / "40_output" / "05-alias.md"
    title = "Two assertions of the broken fixture rest on the same two anchors"
    chapter.write_text(
        chapter.read_text(encoding="utf-8").replace(
            "|a different assertion altogether]]", f"|{title}]]"
        ),
        encoding="utf-8",
    )
    report = validate(root)
    assert _rels(report.warnings, "W-ALIAS") == set()


def test_a_chapter_taking_one_side_of_a_contested_pair_is_reported() -> None:
    report = validate(BROKEN)
    assert _rels(report.warnings, "W-CONTESTED") == {"40_output/04-contested"}


def test_a_chapter_carrying_both_sides_of_a_contested_pair_is_silent(
    tmp_path: Path,
) -> None:
    root = tmp_path / "vault"
    shutil.copytree(BROKEN, root)
    chapter = root / "40_output" / "04-contested.md"
    text = chapter.read_text(encoding="utf-8")
    text = text.replace(
        'assertions: ["[[30_assertions/one-sided]]"]',
        'assertions: ["[[30_assertions/one-sided]]", "[[30_assertions/other-side]]"]',
    )
    text = text.replace(
        "[^1]: Grounded in [[30_assertions/one-sided]].",
        "[^1]: Grounded in [[30_assertions/one-sided]].\n"
        "[^2]: Grounded in [[30_assertions/other-side]].",
    )
    text = text.replace("settled.[^1]", "settled.[^1] And so does its counterpart.[^2]")
    chapter.write_text(text, encoding="utf-8")
    report = validate(root)
    assert _rels(report.warnings, "W-CONTESTED") == set()
    assert "40_output/04-contested" not in _rels(report.errors, "E-MIRROR")


def test_a_status_above_the_status_of_its_anchors_is_caught() -> None:
    """`ladder-jump` is the pure specimen, with its own ledger complete.

    `validated-unchecked` claims the same status without any check date, so it
    stands above its anchors as well and the two findings are independent.
    """
    report = validate(BROKEN)
    assert _rels(report.errors, "E-LADDER") == {
        "30_assertions/ladder-jump",
        "30_assertions/validated-unchecked",
    }


def test_a_chain_that_carries_its_status_all_the_way_down_passes(
    tmp_path: Path,
) -> None:
    root = _raise_chain_to(tmp_path, "validated")
    report = validate(root)
    assert _rels(report.errors, "E-LADDER") == set()


def test_a_chapter_above_its_assertions_is_caught(tmp_path: Path) -> None:
    root = _raise_chain_to(tmp_path, "validated")
    chapter = root / "40_output" / "01-findings.md"
    chapter.write_text(
        chapter.read_text(encoding="utf-8").replace(
            "status: grounded\nchecked: {}",
            "status: validated\nchecked:\n  validation: 2026-07-11\n"
            "  machine-review: 2026-07-11",
        ),
        encoding="utf-8",
    )
    assertion = root / "30_assertions" / "metering-reduces-water-use.md"
    assertion.write_text(
        assertion.read_text(encoding="utf-8").replace(
            "status: validated", "status: grounded"
        ),
        encoding="utf-8",
    )
    report = validate(root)
    assert _rels(report.errors, "E-LADDER") == {"40_output/01-findings"}
    # The rule is decidable per document, so it holds in the chapter mode too.
    scoped = validate(root, chapter=CHAPTER)
    assert _rels(scoped.errors, "E-LADDER") == {"40_output/01-findings"}


def test_a_chapter_is_validated_by_validation_over_validated_assertions(
    tmp_path: Path,
) -> None:
    # Machine review pairs the cited assertions, not the chapter's sentences,
    # so the chapter's rung needs its validation date and the ladder minimum.
    root = _raise_chain_to(tmp_path, "validated")
    chapter = root / "40_output" / "01-findings.md"
    chapter.write_text(
        chapter.read_text(encoding="utf-8").replace(
            "status: grounded\nchecked: {}",
            "status: validated\nchecked:\n  validation: 2026-07-11",
        ),
        encoding="utf-8",
    )
    report = validate(root)
    assert "40_output/01-findings" not in _rels(report.errors, "E-STATUS")
    assert "40_output/01-findings" not in _rels(report.errors, "E-LADDER")


def test_a_check_entry_without_a_date_is_a_finding(tmp_path: Path) -> None:
    root = tmp_path / "vault"
    shutil.copytree(MINIMAL, root)
    distillate = root / "20_distillates" / "documents" / "report-garden-water-2026.md"
    distillate.write_text(
        distillate.read_text(encoding="utf-8").replace(
            "checked: {}", "checked:\n  validation: yes"
        ),
        encoding="utf-8",
    )
    report = validate(root)
    assert "20_distillates/documents/report-garden-water-2026" in _rels(
        report.errors, "E-STATUS"
    )


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
    assert report.warnings == [], report.warnings


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
    """The two remaining vault-wide findings speak about the vault as a whole.

    A run narrowed to one chapter says nothing about whether the vault holds a
    chapter or any content at all, so neither may enter its verdict.
    """
    root = tmp_path / "vault"
    shutil.copytree(MINIMAL, root)
    report = validate(root, chapter=CHAPTER)
    assert not set(VAULT_WIDE_CHECKS) & {code for code, _, _ in report.warnings}


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
        "20_distillates/documents/report-garden-water-2026"
    }


def test_a_quotation_check_without_a_text_version_is_reported() -> None:
    report = validate(BROKEN)
    assert _rels(report.warnings, "W-VERSION") == {
        "20_distillates/publications/unversioned-quote"
    }


def test_a_quotation_outside_the_declared_form_is_caught() -> None:
    """A line with a quotation mark and a parenthesis is not yet a quotation."""
    report = validate(BROKEN)
    assert "20_distillates/publications/malformed-quotation" in _rels(
        report.errors, "E-STATEMENT"
    )
    assert "20_distillates/publications/unversioned-quote" not in _rels(
        report.errors, "E-STATEMENT"
    )


def test_a_quotation_may_run_over_several_lines(tmp_path: Path) -> None:
    root = tmp_path / "vault"
    shutil.copytree(MINIMAL, root)
    path = root / "20_distillates" / "publications" / "example-2024-metering.md"
    text = path.read_text(encoding="utf-8").replace(
        '  > "Metering alone reduced irrigation volumes in nine of eleven surveyed gardens." (example2024metering, p. 4)',
        '  > "Metering alone reduced irrigation volumes\n  > in nine of eleven surveyed gardens." (example2024metering, p. 4)',
    )
    path.write_text(text, encoding="utf-8")
    report = validate(root)
    assert _rels(report.errors, "E-STATEMENT") == set()


def _vault_with_an_unread_source(tmp_path: Path) -> Path:
    """The minimal vault whose report gains four blocks no distillate anchors."""
    root = tmp_path / "vault"
    shutil.copytree(MINIMAL, root)
    path = root / "10_markdown" / "documents" / "report-garden-water-2026.md"
    extra = "".join(f"\nAn unread paragraph number {n}. ^u{n}\n" for n in range(4))
    path.write_text(path.read_text(encoding="utf-8") + extra, encoding="utf-8")
    return root


def test_a_source_the_distillates_mostly_leave_unanchored_is_reported(
    tmp_path: Path,
) -> None:
    root = _vault_with_an_unread_source(tmp_path)
    report = validate(root, run_computations=False)
    (finding,) = [w for w in report.warnings if w[0] == "W-COVERAGE"]
    assert finding[1] == "10_markdown/documents/report-garden-water-2026"
    assert "4 of 7 blocks" in finding[2]


def test_the_coverage_threshold_is_a_parameter(tmp_path: Path) -> None:
    root = _vault_with_an_unread_source(tmp_path)
    assert (
        _rels(
            validate(root, run_computations=False, min_coverage=0).warnings,
            "W-COVERAGE",
        )
        == set()
    )
    assert _rels(
        validate(root, run_computations=False, min_coverage=0.45).warnings, "W-COVERAGE"
    ) == {"10_markdown/documents/report-garden-water-2026"}


def test_a_representation_without_a_distillate_is_not_judged_for_coverage(
    tmp_path: Path,
) -> None:
    """Before the first distillate the inventory already says ingested."""
    root = _vault_with_an_unread_source(tmp_path)
    (root / "20_distillates" / "documents" / "report-garden-water-2026.md").unlink()
    report = validate(root, run_computations=False)
    assert _rels(report.warnings, "W-COVERAGE") == set()


def test_coverage_stays_out_of_the_chapter_mode(tmp_path: Path) -> None:
    root = _vault_with_an_unread_source(tmp_path)
    result = _run_cli(root, "--no-computations", "--chapter", CHAPTER)
    assert result.returncode == 0, result.stdout
    assert "W-COVERAGE" not in result.stderr


def test_an_empty_frontmatter_block_parses_as_an_empty_mapping(tmp_path: Path) -> None:
    assert split_frontmatter("---\n---\n\n# Body\n") == ("", "\n\n# Body\n")
    path = tmp_path / "empty.md"
    path.write_text("---\n---\n", encoding="utf-8")
    report = Report()
    doc = parse_doc(path, tmp_path, report)
    assert doc is not None and doc.fm == {}
    assert report.errors == []


def test_a_byte_order_mark_does_not_hide_the_frontmatter(tmp_path: Path) -> None:
    assert split_frontmatter("\ufeff---\na: 1\n---\nbody") == ("a: 1", "\nbody")
    path = tmp_path / "bom.md"
    path.write_text("---\ntype: glossary\n---\n", encoding="utf-8-sig")
    doc = parse_doc(path, tmp_path, Report())
    assert doc is not None and doc.fm == {"type": "glossary"}


def test_a_scalar_link_field_counts_as_one_link(tmp_path: Path) -> None:
    """A scalar used to be iterated character by character, one finding per letter."""
    root = tmp_path / "vault"
    shutil.copytree(MINIMAL, root)
    path = root / "20_distillates" / "documents" / "report-garden-water-2026.md"
    path.write_text(
        path.read_text(encoding="utf-8").replace(
            'topics: ["[[Water]]"]', 'topics: "[[Water]]"'
        ),
        encoding="utf-8",
    )
    assert validate(root, run_computations=False).errors == []


def test_a_scalar_grounding_still_holds_the_ladder(tmp_path: Path) -> None:
    root = tmp_path / "vault"
    shutil.copytree(BROKEN, root)
    path = root / "30_assertions" / "ladder-jump.md"
    path.write_text(
        path.read_text(encoding="utf-8").replace(
            'grounding:\n  - "[[20_distillates/documents/note#^s3]]"',
            'grounding: "[[20_distillates/documents/note#^s3]]"',
        ),
        encoding="utf-8",
    )
    report = validate(root, run_computations=False)
    assert "30_assertions/ladder-jump" in _rels(report.errors, "E-LADDER")


def test_a_computation_printing_non_ascii_reproduces(tmp_path: Path) -> None:
    """The Windows console code page cannot encode the sign, UTF-8 mode can."""
    root = tmp_path / "vault"
    shutil.copytree(MINIMAL, root)
    script = root / "tools" / "analysis" / "reduction.py"
    script.write_text(
        script.read_text(encoding="utf-8").replace(
            "print(reduction)", 'print(f"\\u2248 {reduction}")'
        ),
        encoding="utf-8",
    )
    path = root / "20_distillates" / "data" / "water-readings-2025.md"
    path.write_text(
        path.read_text(encoding="utf-8").replace(
            "\u2192 `31.4`", "\u2192 `\u2248 31.4`"
        ),
        encoding="utf-8",
    )
    assert validate(root).errors == []


def test_a_computation_that_exceeds_its_timeout_is_a_finding(monkeypatch) -> None:
    def too_slow(command, **kwargs):
        raise subprocess.TimeoutExpired(command, kwargs["timeout"])

    monkeypatch.setattr("validate.subprocess.run", too_slow)
    report = validate(MINIMAL)
    (message,) = [m for c, _, m in report.errors if c == "E-COMPUTATION"]
    assert "timed out" in message


def test_a_single_reference_object_resolves(tmp_path: Path) -> None:
    """A reference manager may export one record as an object instead of an array."""
    root = tmp_path / "vault"
    shutil.copytree(MINIMAL, root)
    path = root / "references" / "example-corpus.csl.json"
    records = json.loads(path.read_text(encoding="utf-8"))
    path.write_text(json.dumps(records[0]), encoding="utf-8")
    assert validate(root, run_computations=False).errors == []


@pytest.mark.parametrize(
    "rel",
    [
        "20_distillates/documents/report-garden-water-2026",
        "20_distillates/data/water-readings-2025",
        "20_distillates/publications/example-2024-metering",
    ],
)
def test_a_source_cannot_have_duplicate_distillates(tmp_path: Path, rel: str) -> None:
    root = tmp_path / "vault"
    shutil.copytree(MINIMAL, root)
    original = root / f"{rel}.md"
    duplicate = root / f"{rel}-duplicate.md"
    duplicate.write_bytes(original.read_bytes())
    report = validate(root, run_computations=False)
    assert _rels(report.errors, "E-DUPLICATE") == {rel, f"{rel}-duplicate"}


def test_distillates_of_explicitly_different_publication_versions_are_distinct(
    tmp_path: Path,
) -> None:
    root = tmp_path / "vault"
    shutil.copytree(MINIMAL, root)
    original = root / "20_distillates/publications/example-2024-metering.md"
    duplicate = original.with_stem("example-2024-metering-earlier-version")
    duplicate.write_text(
        original.read_text(encoding="utf-8").replace(
            "publisher PDF as exported 2026-07-11", "preprint as exported 2026-07-10"
        ),
        encoding="utf-8",
    )
    assert validate(root, run_computations=False).errors == []


@pytest.mark.parametrize("separate_file", [False, True])
def test_duplicate_reference_ids_never_resolve_by_last_record_wins(
    tmp_path: Path, separate_file: bool
) -> None:
    root = tmp_path / "vault"
    shutil.copytree(MINIMAL, root)
    path = root / "references/example-corpus.csl.json"
    record = json.loads(path.read_text(encoding="utf-8"))[0]
    if separate_file:
        target = path.with_name("duplicate-reference.json")
        target.write_text(json.dumps(record), encoding="utf-8")
    else:
        path.write_text(json.dumps([record, record, record]), encoding="utf-8")
    report = validate(root, run_computations=False)
    assert _rels(report.errors, "E-DUPLICATE")
    assert "20_distillates/publications/example-2024-metering" in _rels(
        report.errors, "E-ANCHOR"
    )
    problems = []
    assert record["id"] not in load_references(root, problems)
    assert all("duplicate CSL id" in problem for problem in problems)


@pytest.mark.parametrize(
    "contents",
    [
        "[{",
        "null",
        '"not a record"',
        "[null]",
        "[42]",
        '[{"title": "Record without identity"}]',
        '[{"id": ""}]',
        '[{"id": "   "}]',
        '[{"id": []}]',
        '[{"id": true}]',
        '[{"id": {"value": "invalid"}}]',
    ],
)
def test_unused_malformed_reference_files_are_errors(
    tmp_path: Path, contents: str
) -> None:
    """Boundary variants exercise invalid imports beside the real positive corpus."""
    root = tmp_path / "vault"
    shutil.copytree(MINIMAL, root)
    (root / "references/unused-malformed.json").write_text(contents, encoding="utf-8")
    report = validate(root, run_computations=False)
    assert "references/unused-malformed.json" in _rels(report.errors, "E-FRONTMATTER")
    assert _rels(report.errors, "E-ANCHOR") == set()


def test_non_utf8_reference_file_is_a_finding(tmp_path: Path) -> None:
    root = tmp_path / "vault"
    shutil.copytree(MINIMAL, root)
    (root / "references/unused-malformed.json").write_bytes(b"\xff")
    assert "references/unused-malformed.json" in _rels(
        validate(root, run_computations=False).errors, "E-FRONTMATTER"
    )


def test_reference_loader_keeps_compatible_inventory_problem_sink(
    tmp_path: Path,
) -> None:
    root = tmp_path / "vault"
    shutil.copytree(MINIMAL, root)
    (root / "references/unused-malformed.json").write_text("[null]", encoding="utf-8")
    problems = []
    records = load_references(root, problems)
    assert "example2024metering" in records
    assert len(problems) == 1
    assert problems[0].startswith("references/unused-malformed.json:")


def test_unrelated_reference_import_errors_stay_out_of_chapter_scope(
    tmp_path: Path,
) -> None:
    root = tmp_path / "vault"
    shutil.copytree(MINIMAL, root)
    (root / "references/unused-malformed.json").write_text("[null]", encoding="utf-8")
    report = validate(root, run_computations=False, chapter=CHAPTER)
    assert report.errors == []
    assert report.warnings == []
