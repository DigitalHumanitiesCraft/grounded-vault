"""Fixture tests for the deterministic parts of tools/review.py.

Covered are pair cutting, prompt construction, verdict parsing and the booking
of checked.machine-review, all against tests/fixtures/minimal. The judging
mechanism itself is not exercised here: no test calls a model, and the batch
path is driven with hand-written verdict records.
"""

import json
import re
import shutil
from dataclasses import replace
from pathlib import Path

import pytest

from review import (
    ASSERTION_PROMPT,
    SOURCE_PROMPT,
    VERDICTS,
    Judgement,
    book_results,
    cut_pairs,
    parse_verdict,
    read_verdicts,
    run_claude,
    set_checked_date,
)
from validate import validate

REPO = Path(__file__).parents[1]
OPERATIONS = REPO / "knowledge" / "operations.md"
MINIMAL = REPO / "tests" / "fixtures" / "minimal"

DOC_DISTILLATE = "20_distillates/documents/report-garden-water-2026"
DATA_DISTILLATE = "20_distillates/data/water-readings-2025"
PUB_DISTILLATE = "20_distillates/publications/example-2024-metering"
ASSERTION = "30_assertions/metering-reduces-water-use"


@pytest.fixture(scope="module")
def pairs():
    return cut_pairs(MINIMAL)


def _by_id(pairs, pair_id):
    found = [p for p in pairs if p.id == pair_id]
    assert len(found) == 1, f"{pair_id} not cut exactly once: {len(found)}"
    return found[0]


def test_every_statement_and_every_grounding_becomes_one_pair(pairs) -> None:
    source_pairs = [p for p in pairs if p.kind == "source"]
    assertion_pairs = [p for p in pairs if p.kind == "assertion"]
    assert len(source_pairs) == 5  # 3 document, 1 data, 1 publication statements
    assert len(assertion_pairs) == 3  # one per grounding anchor of the assertion
    assert len({p.id for p in pairs}) == len(pairs)


def test_pair_cutting_is_deterministic() -> None:
    first = cut_pairs(MINIMAL)
    second = cut_pairs(MINIMAL)
    assert [p.id for p in first] == [p.id for p in second]
    assert [p.location for p in first] == [p.location for p in second]


def test_document_pair_is_block_plus_heading_path(pairs) -> None:
    pair = _by_id(pairs, f"{DOC_DISTILLATE}#^s1")
    assert pair.anchor == "10_markdown/documents/report-garden-water-2026#^a1b2"
    assert "Annual Water Report of the Example Community Garden 2026" in pair.location
    assert (
        "Water meters were installed on all forty plots in January 2025."
        in pair.location
    )
    assert pair.statement == "Water meters were installed on all plots in January 2025."


def test_publication_pair_is_the_verbatim_quotation(pairs) -> None:
    pair = _by_id(pairs, f"{PUB_DISTILLATE}#^s1")
    assert (
        '"Metering alone reduced irrigation volumes in nine of eleven surveyed gardens."'
        in pair.location
    )
    assert "example2024metering, p. 4" in pair.location
    assert pair.statement.startswith("In the surveyed gardens, metering alone")


def test_data_pair_is_the_computation_and_its_result(pairs) -> None:
    pair = _by_id(pairs, f"{DATA_DISTILLATE}#^s1")
    assert "python tools/analysis/reduction.py" in pair.location
    assert "31.4" in pair.location
    assert pair.statement == "Water use in 2025 was 31.4 percent below 2024."


def test_assertion_pair_holds_statement_and_assertion_sentence(pairs) -> None:
    pair = _by_id(pairs, f"{ASSERTION}<-{DATA_DISTILLATE}#^s1")
    assert pair.location == "Water use in 2025 was 31.4 percent below 2024."
    assert pair.statement.startswith("After meters were installed on all plots,")
    assert "wet summer as a co-factor" in pair.statement
    assert pair.document == ASSERTION


def test_anti_anchoring_keeps_the_producing_reasoning_out(pairs) -> None:
    """Nothing but location and statement enters the pair, so no link, anchor or Support text."""
    for pair in pairs:
        assert "[[" not in pair.location and "[[" not in pair.statement
        assert "^s" not in pair.statement
        assert "## Support" not in pair.prompt
        assert "what this anchor contributes" not in pair.prompt
    contribution = "the readings reproduce the drop as 31.4 percent"
    assert all(contribution not in pair.prompt for pair in pairs)


def test_prompts_follow_the_skeletons_of_operations_md(pairs) -> None:
    source = _by_id(pairs, f"{DOC_DISTILLATE}#^s1").prompt
    assertion = _by_id(pairs, f"{ASSERTION}<-{DATA_DISTILLATE}#^s1").prompt
    for prompt in (source, assertion):
        assert prompt.startswith("You are an adversarial reviewer.")
        for verdict in VERDICTS:
            assert verdict in prompt
    assert "PASSAGE:" in source and "STATEMENT:" in source
    assert "ASSERTION:" not in source
    assert "STATEMENT:" in assertion and "ASSERTION:" in assertion
    assert "PASSAGE:" not in assertion


def _skeleton(marker: str) -> str:
    """The quoted prompt skeleton that follows `marker` in operations.md."""
    lines = OPERATIONS.read_text(encoding="utf-8").split(marker, 1)[1].splitlines()
    quoted: list[str] = []
    for line in lines:
        if line.strip().startswith(">"):
            quoted.append(line.strip()[1:])
        elif quoted:
            break
    return " ".join(quoted)


def _comparable(text: str) -> str:
    """Placeholders reduced to their braces and whitespace to single spaces."""
    return " ".join(re.sub(r"\{[^}]*\}", "{}", text).split())


@pytest.mark.parametrize(
    ("template", "marker"),
    [
        (SOURCE_PROMPT, "Reference prompt skeleton:"),
        (ASSERTION_PROMPT, "### Assertion review prompt skeleton"),
    ],
    ids=["source", "assertion"],
)
def test_prompt_text_is_word_for_word_the_skeleton(template: str, marker: str) -> None:
    filled = template.replace("{vocabulary}", " | ".join(VERDICTS))
    assert _comparable(filled) == _comparable(_skeleton(marker))


@pytest.mark.parametrize(
    ("response", "expected"),
    [
        ("fully supports", "fully supports"),
        ("Fully supports.\nThe passage states exactly this.", "fully supports"),
        ("**overreaches**\nThe statement widens the finding.", "overreaches"),
        (
            "Verdict: not in the text\nNothing in the passage says so.",
            "not in the text",
        ),
        ("  partially supports  ", "partially supports"),
        (
            "Contradicts.\nThe passage names a different year.",
            "contradicts",
        ),
    ],
)
def test_parse_verdict_accepts_the_vocabulary(response: str, expected: str) -> None:
    assert parse_verdict(response) == expected


@pytest.mark.parametrize(
    "response",
    [
        "",
        "supports",
        "yes",
        "mostly supports",
        "It fully supports the first half but overreaches on the second.",
        "not fully supports",
        "fully supports? No, the statement is wrong.",
        "The passage does not fully supports the assertion.",
        "fully supports but overreaches on the second claim",
        "fully supports nothing",
    ],
)
def test_parse_verdict_rejects_everything_else(response: str) -> None:
    with pytest.raises(ValueError):
        parse_verdict(response)


def test_set_checked_date_keeps_the_rest_of_the_frontmatter() -> None:
    text = "---\ntype: distillate\nchecked:\n  quote: 2026-07-11\nupdated: 2026-07-11\n---\n\n# X\n"
    out = set_checked_date(text, "machine-review", "2026-08-09")
    assert "  quote: 2026-07-11\n" in out
    assert "  machine-review: 2026-08-09\n" in out
    assert out.count("checked:") == 1
    assert (
        set_checked_date(out, "machine-review", "2026-08-10").count("machine-review")
        == 1
    )


def test_set_checked_date_expands_an_empty_map() -> None:
    text = "---\ntype: assertion\nchecked: {}\nupdated: 2026-07-11\n---\n\n# X\n"
    out = set_checked_date(text, "machine-review", "2026-08-09")
    assert "checked:\n  machine-review: 2026-08-09\nupdated: 2026-07-11\n" in out


def test_set_checked_date_refuses_a_document_without_the_field() -> None:
    with pytest.raises(ValueError):
        set_checked_date("---\ntype: moc\n---\n\n# X\n", "machine-review", "2026-08-09")


def _all_fully_supports(pairs) -> dict[str, Judgement]:
    return {p.id: Judgement("fully supports", p.prompt_hash) for p in pairs}


def test_booking_sets_the_date_only_on_a_clean_document(tmp_path) -> None:
    vault = tmp_path / "vault"
    shutil.copytree(MINIMAL, vault)
    pairs = cut_pairs(vault)
    verdicts = _all_fully_supports(pairs)
    pair = _by_id(pairs, f"{DOC_DISTILLATE}#^s3")
    verdicts[pair.id] = Judgement("overreaches", pair.prompt_hash)

    outcome = book_results(vault, pairs, verdicts, "2026-08-09", apply=True)

    booked = {r.document for r in outcome.documents if r.booked}
    assert DOC_DISTILLATE not in booked
    assert {DATA_DISTILLATE, PUB_DISTILLATE, ASSERTION} <= booked
    assert [(d.pair_id, d.verdict) for d in outcome.deviations] == [
        (f"{DOC_DISTILLATE}#^s3", "overreaches")
    ]
    assert "machine-review: 2026-08-09" in (vault / f"{ASSERTION}.md").read_text(
        encoding="utf-8"
    )
    assert "machine-review" not in (vault / f"{DOC_DISTILLATE}.md").read_text(
        encoding="utf-8"
    )


def test_booking_without_apply_writes_nothing(tmp_path) -> None:
    vault = tmp_path / "vault"
    shutil.copytree(MINIMAL, vault)
    pairs = cut_pairs(vault)
    before = (vault / f"{ASSERTION}.md").read_text(encoding="utf-8")

    outcome = book_results(
        vault, pairs, _all_fully_supports(pairs), "2026-08-09", apply=False
    )

    assert all(r.booked for r in outcome.documents)
    assert (vault / f"{ASSERTION}.md").read_text(encoding="utf-8") == before


def test_unjudged_pairs_block_the_booking_and_are_reported(tmp_path) -> None:
    vault = tmp_path / "vault"
    shutil.copytree(MINIMAL, vault)
    pairs = cut_pairs(vault)
    verdicts = _all_fully_supports(pairs)
    del verdicts[f"{PUB_DISTILLATE}#^s1"]

    outcome = book_results(vault, pairs, verdicts, "2026-08-09", apply=True)

    assert outcome.unjudged == [f"{PUB_DISTILLATE}#^s1"]
    assert PUB_DISTILLATE not in {r.document for r in outcome.documents if r.booked}


def test_booking_keeps_the_line_endings_of_the_file(tmp_path) -> None:
    vault = tmp_path / "vault"
    shutil.copytree(MINIMAL, vault)
    path = vault / f"{ASSERTION}.md"
    path.write_bytes(
        path.read_text(encoding="utf-8").replace("\n", "\r\n").encode("utf-8")
    )
    pairs = cut_pairs(vault)

    book_results(vault, pairs, _all_fully_supports(pairs), "2026-08-09", apply=True)

    raw = path.read_bytes()
    assert b"machine-review: 2026-08-09" in raw
    assert raw.count(b"\n") == raw.count(b"\r\n")


class _Result:
    returncode = 0
    stderr = ""
    stdout = "fully supports\nThe passage states exactly this."


def test_run_claude_passes_the_prompt_on_stdin(monkeypatch, pairs) -> None:
    """Windows caps a command line at ~32k characters, so no prompt goes into argv."""
    calls = []

    def fake_run(command, **kwargs):
        calls.append((command, kwargs))
        return _Result()

    monkeypatch.setattr("review.shutil.which", lambda name: "claude")
    monkeypatch.setattr("review.subprocess.run", fake_run)

    long_pair = pairs[0].__class__(
        id="x",
        kind="source",
        document="d",
        anchor="a",
        location="L" * 40000,
        statement="C",
    )
    problems: list[str] = []
    records = run_claude([long_pair], "sonnet", problems)

    assert problems == []
    assert [r["verdict"] for r in records] == ["fully supports"]
    command, kwargs = calls[0]
    assert all(long_pair.prompt not in part for part in command)
    assert max(len(part) for part in command) < 4096
    assert kwargs["input"] == long_pair.prompt


def test_booked_vault_still_validates(tmp_path) -> None:
    vault = tmp_path / "vault"
    shutil.copytree(MINIMAL, vault)
    pairs = cut_pairs(vault)
    book_results(vault, pairs, _all_fully_supports(pairs), "2026-08-09", apply=True)
    assert validate(vault).errors == []


def test_booking_skips_a_document_that_fails_validation(tmp_path) -> None:
    """Validation gates review, so a verdict never books over a validation error."""
    vault = tmp_path / "vault"
    shutil.copytree(MINIMAL, vault)
    path = vault / f"{ASSERTION}.md"
    path.write_text(
        path.read_text(encoding="utf-8").replace(
            "status: grounded", "status: approved"
        ),
        encoding="utf-8",
    )
    pairs = cut_pairs(vault)

    outcome = book_results(
        vault, pairs, _all_fully_supports(pairs), "2026-08-09", apply=True
    )

    assert ASSERTION not in {r.document for r in outcome.documents if r.booked}
    assert DOC_DISTILLATE in {r.document for r in outcome.documents if r.booked}
    assert any(p.startswith(f"{ASSERTION}: not booked") for p in outcome.problems)
    assert "machine-review" not in path.read_text(encoding="utf-8")


def test_a_document_that_does_not_parse_is_reported(tmp_path) -> None:
    vault = tmp_path / "vault"
    shutil.copytree(MINIMAL, vault)
    (vault / "20_distillates" / "documents" / "broken.md").write_text(
        "---\n- not a mapping\n---\n", encoding="utf-8"
    )
    problems: list[str] = []
    cut_pairs(vault, problems)
    assert problems == [
        "20_distillates/documents/broken: E-FRONTMATTER frontmatter is not a mapping"
    ]


@pytest.mark.parametrize("field", ["statement", "location"])
def test_changed_pair_cannot_reuse_an_old_verdict(tmp_path, field: str) -> None:
    vault = tmp_path / "vault"
    shutil.copytree(MINIMAL, vault)
    pairs = cut_pairs(vault)
    old_verdicts = _all_fully_supports(pairs)
    pair = pairs[0]
    changed = replace(pair, **{field: getattr(pair, field) + " Changed after review."})
    path = vault / f"{pair.document}.md"
    before = path.read_bytes()

    outcome = book_results(
        vault, [changed, *pairs[1:]], old_verdicts, "2026-10-03", apply=True
    )

    assert pair.document not in {r.document for r in outcome.documents if r.booked}
    assert any("stale verdict" in problem for problem in outcome.problems)
    assert path.read_bytes() == before


def test_prompt_hash_binds_the_review_instructions(monkeypatch, pairs) -> None:
    pair = pairs[0]
    emitted = pair.to_dict()
    assert re.fullmatch(r"[0-9a-f]{64}", emitted["prompt_hash"])
    monkeypatch.setattr("review.SOURCE_PROMPT", SOURCE_PROMPT + "\nNew instruction.")
    assert pair.prompt_hash != emitted["prompt_hash"]


def test_file_changed_after_pair_cutting_is_not_booked(tmp_path) -> None:
    vault = tmp_path / "vault"
    shutil.copytree(MINIMAL, vault)
    pairs = cut_pairs(vault)
    verdicts = _all_fully_supports(pairs)
    path = vault / f"{ASSERTION}.md"
    path.write_text(
        path.read_text(encoding="utf-8").replace(
            "the garden's water use fell by 31.4 percent",
            "the garden's water use doubled",
        ),
        encoding="utf-8",
    )
    before = path.read_bytes()
    outcome = book_results(vault, pairs, verdicts, "2026-10-03", apply=True)
    assert ASSERTION not in {r.document for r in outcome.documents if r.booked}
    assert path.read_bytes() == before
    assert any("stale verdict" in problem for problem in outcome.problems)


def test_new_statement_after_pair_cutting_requires_another_review(tmp_path) -> None:
    vault = tmp_path / "vault"
    shutil.copytree(MINIMAL, vault)
    pairs = cut_pairs(vault)
    verdicts = _all_fully_supports(pairs)
    path = vault / f"{DOC_DISTILLATE}.md"
    text = path.read_text(encoding="utf-8")
    statement = next(line for line in text.splitlines() if line.endswith("^s1"))
    path.write_text(
        text.replace("## Terms", statement.replace("^s1", "^s4") + "\n\n## Terms"),
        encoding="utf-8",
    )
    before = path.read_bytes()
    outcome = book_results(vault, pairs, verdicts, "2026-10-03", apply=True)
    assert DOC_DISTILLATE not in {r.document for r in outcome.documents if r.booked}
    assert path.read_bytes() == before
    assert any("pair set changed" in problem for problem in outcome.problems)


def test_legacy_unbound_verdict_does_not_pass(pairs) -> None:
    outcome = book_results(
        MINIMAL, pairs, {p.id: "fully supports" for p in pairs}, "2026-10-03"
    )
    assert not any(r.booked for r in outcome.documents)
    assert outcome.problems


def test_empty_review_cannot_report_success(capsys) -> None:
    from review import _report

    outcome = book_results(MINIMAL, [], {}, "2026-10-03")
    assert _report(outcome, []) == 1
    assert "no machine review took place" in capsys.readouterr().err


def test_invalid_review_date_cannot_be_booked(tmp_path) -> None:
    vault = tmp_path / "vault"
    shutil.copytree(MINIMAL, vault)
    pairs = cut_pairs(vault)
    path = vault / f"{ASSERTION}.md"
    before = path.read_bytes()
    outcome = book_results(
        vault, pairs, _all_fully_supports(pairs), "not-a-date", apply=True
    )
    assert outcome.problems == ["review date must use strict ISO YYYY-MM-DD format"]
    assert path.read_bytes() == before


def test_empty_emit_fails_before_writing_an_empty_batch(
    tmp_path, monkeypatch, capsys
) -> None:
    from review import main

    output = tmp_path / "prompts.jsonl"
    monkeypatch.setattr(
        "sys.argv", ["review.py", "emit", str(tmp_path), "--out", str(output)]
    )
    assert main() == 1
    assert not output.exists()
    assert "no reviewable pairs" in capsys.readouterr().err


def test_unknown_verdict_id_is_rejected(pairs) -> None:
    verdicts = _all_fully_supports(pairs)
    verdicts["old-removed-pair"] = next(iter(verdicts.values()))
    outcome = book_results(MINIMAL, pairs, verdicts, "2026-10-03")
    assert not outcome.documents
    assert outcome.problems == ["unknown verdict id: old-removed-pair"]


def test_read_verdicts_requires_the_emitted_hash(tmp_path, pairs) -> None:
    pair = pairs[0]
    path = tmp_path / "verdicts.jsonl"
    path.write_text(
        json.dumps({"id": pair.id, "verdict": "fully supports"}) + "\n",
        encoding="utf-8",
    )
    problems = []
    assert read_verdicts(path, problems) == {}
    assert "prompt_hash" in problems[0]


@pytest.mark.parametrize("verdict", ["fully supports", "overreaches"])
def test_duplicate_verdict_records_never_keep_a_pass(tmp_path, pairs, verdict) -> None:
    pair = pairs[0]
    records = [
        {"id": pair.id, "prompt_hash": pair.prompt_hash, "verdict": value}
        for value in ("fully supports", verdict, "fully supports")
    ]
    path = tmp_path / "verdicts.jsonl"
    path.write_text(
        "\n".join(json.dumps(record) for record in records), encoding="utf-8"
    )
    problems = []
    assert read_verdicts(path, problems) == {}
    assert all("duplicate verdict id" in problem for problem in problems)


def test_verdict_and_raw_response_must_agree(tmp_path, pairs) -> None:
    pair = pairs[0]
    record = {
        "id": pair.id,
        "prompt_hash": pair.prompt_hash,
        "verdict": "fully supports",
        "response": "overreaches\nThe claim exceeds the passage.",
    }
    path = tmp_path / "verdicts.jsonl"
    path.write_text(json.dumps(record), encoding="utf-8")
    problems = []
    assert read_verdicts(path, problems) == {}
    assert "conflict" in problems[0]


def test_valid_verdict_round_trip_preserves_prompt_binding(tmp_path, pairs) -> None:
    records = [
        {"id": p.id, "prompt_hash": p.prompt_hash, "verdict": "fully supports"}
        for p in pairs
    ]
    path = tmp_path / "verdicts.jsonl"
    path.write_text(
        "\n".join(json.dumps(record) for record in records), encoding="utf-8"
    )
    problems = []
    verdicts = read_verdicts(path, problems)
    assert problems == []
    assert verdicts == _all_fully_supports(pairs)
    outcome = book_results(MINIMAL, pairs, verdicts, "2026-10-03")
    assert all(r.booked for r in outcome.documents)


def test_assertion_statement_cannot_hide_behind_a_supported_heading(tmp_path) -> None:
    vault = tmp_path / "vault"
    shutil.copytree(MINIMAL, vault)
    path = vault / f"{ASSERTION}.md"
    text = path.read_text(encoding="utf-8")
    start = text.index("## Statement\n") + len("## Statement\n")
    end = text.index("## Support\n", start)
    statement = "The findings establish an unrelated causal claim."
    path.write_text(text[:start] + f"\n{statement}\n\n" + text[end:], encoding="utf-8")
    pairs = [p for p in cut_pairs(vault) if p.document == ASSERTION]
    assert pairs
    assert all(p.statement == statement for p in pairs)


def test_empty_statement_section_is_reported_instead_of_reviewing_the_title(
    tmp_path,
) -> None:
    vault = tmp_path / "vault"
    shutil.copytree(MINIMAL, vault)
    path = vault / f"{ASSERTION}.md"
    text = path.read_text(encoding="utf-8")
    start = text.index("## Statement\n") + len("## Statement\n")
    end = text.index("## Support\n", start)
    path.write_text(text[:start] + "\n" + text[end:], encoding="utf-8")
    problems = []
    pairs = cut_pairs(vault, problems)
    assert not any(p.document == ASSERTION for p in pairs)
    assert f"{ASSERTION}: no assertion statement, skipped" in problems
