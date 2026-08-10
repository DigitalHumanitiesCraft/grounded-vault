"""Fixture tests for tools/validate.py against the shipped fixture vaults.

tests/fixtures/minimal is the positive fixture and must pass clean;
tests/fixtures/broken carries one specimen per defect class and every class must
be caught. The warning tests use temporary vaults, because a warning states that
a check found no subject, which neither shipped fixture can show.
"""

import re
import shutil
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).parents[1]
sys.path.insert(0, str(REPO / "tools"))

from validate import VAULT_WIDE_CHECKS, validate  # noqa: E402

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
    "E-STATEMENT",  # core statement without a statement ID
    "E-STATUS",  # status without recorded checks
    "E-LADDER",  # status above the status of the anchors it rests on
    "E-FOOTNOTE",  # wrong keyword and undefined marker
    "E-MIRROR",  # frontmatter mirror out of sync
    "E-COMPUTATION",  # computation script missing
    "E-QUOTE",  # intake-time quotation check not recorded
}

# Warnings the broken fixture carries; each has its own test below, because the
# broken-fixture tests above speak about error codes only.
EXPECTED_BROKEN_WARNINGS = {
    "W-PLACEHOLDER",  # test_a_surviving_template_placeholder_is_a_warning
    "W-STALE",  # test_checks_older_than_the_content_are_reported
    "W-UNANCHORED",  # test_a_paragraph_without_a_footnote_marker_is_a_warning
    "W-CONTESTED",  # test_a_chapter_taking_one_side_of_a_contested_pair_is_reported
    "W-DUPLICATE-GROUNDING",  # test_two_assertions_on_the_same_anchors_are_reported
    "W-ALIAS",  # test_a_footnote_alias_that_renames_its_assertion_is_reported
}

# Codes no fixture can carry, because they need a vault state a conformant file
# set does not have; each is asserted from a temporary vault instead.
EXPECTED_TEMPORARY_VAULT_CODES = {
    "E-SCOPE",  # test_an_unknown_chapter_is_a_finding
    "W-EMPTY",  # test_an_empty_vault_says_which_checks_had_no_subject
    "W-NO-OUTPUT",  # test_an_empty_vault_says_which_checks_had_no_subject
}

EMITTED_CODE = re.compile(r"report\.(?:error|warn)\(\s*\"([EW]-[A-Z-]+)\"")


def _rels(entries: list[tuple[str, str, str]], code: str) -> set[str]:
    return {rel for found, rel, _ in entries if found == code}


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
        "20_distillates/documents/report-garden-water-2026.md"
    }
