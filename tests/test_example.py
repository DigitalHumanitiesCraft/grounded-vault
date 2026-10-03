"""Exercise the public example through the script-pipeline command interfaces.

The real retained excerpt and manifest test source integrity. Temporary copies
exercise review booking with explicitly simulated judgements, which establish
no semantic review. Run with pytest tests/test_example.py from the repository.
"""

import hashlib
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path

from review import cut_pairs, read_verdicts
from validate import validate

REPO = Path(__file__).parents[1]
EXAMPLE = REPO / "examples" / "prov-entity"
ENTITY_DEFINITION = (
    "An entity is a physical, digital, conceptual, or other kind of thing "
    "with some fixed aspects; entities may be real or imaginary."
)
STATEMENT = (
    "PROV-DM defines an entity as a physical, digital, conceptual or other "
    "kind of thing with fixed aspects."
)


def _run(tool: str, *arguments: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, "-X", "utf8", str(REPO / "tools" / tool), *arguments],
        cwd=REPO,
        capture_output=True,
        text=True,
        encoding="utf-8",
        check=True,
        timeout=30,
    )


def test_example_retains_the_real_excerpt_and_immutable_source_hashes() -> None:
    manifest = json.loads((EXAMPLE / "manifest.json").read_text(encoding="utf-8"))
    for record in manifest["files"]:
        path = EXAMPLE / record["path"]
        assert hashlib.sha256(path.read_bytes()).hexdigest() == record["sha256"]
    original = (EXAMPLE / "00_sources" / "prov-entity.txt").read_text(encoding="utf-8")
    representation = (
        EXAMPLE / "10_markdown" / "documents" / "prov-entity.md"
    ).read_text(encoding="utf-8")
    assert ENTITY_DEFINITION in original
    assert f"{ENTITY_DEFINITION} ^entity-definition" in representation
    assert manifest["source_url"] in original
    assert manifest["source_copyright"] in original
    assert manifest["source_license"] in original
    for path in EXAMPLE.rglob("*.md"):
        assert "{{" not in path.read_text(encoding="utf-8"), path


def test_example_validates_the_complete_chain_without_warnings() -> None:
    whole = validate(EXAMPLE)
    assert whole.errors == []
    assert whole.warnings == []
    chapter = validate(EXAMPLE, chapter="40_output/01-entity-definition")
    assert chapter.errors == []
    assert chapter.warnings == []
    assert "0 error(s), 0 warning(s)" in _run("validate.py", str(EXAMPLE)).stdout
    scoped = _run(
        "validate.py", str(EXAMPLE), "--chapter", "40_output/01-entity-definition"
    )
    assert "CHAPTER READY" in scoped.stdout


def test_example_pairs_cover_the_same_narrow_statement_deterministically() -> None:
    problems: list[str] = []
    first = cut_pairs(EXAMPLE, problems)
    second = cut_pairs(EXAMPLE)
    assert problems == []
    assert [pair.to_dict() for pair in first] == [pair.to_dict() for pair in second]
    assert {pair.kind for pair in first} == {"source", "assertion"}
    assert len(first) == 2
    for pair in first:
        assert pair.statement == STATEMENT
        assert (
            pair.prompt_hash == hashlib.sha256(pair.prompt.encode("utf-8")).hexdigest()
        )


def test_recorded_actual_review_still_matches_the_committed_pairs() -> None:
    problems: list[str] = []
    verdicts = read_verdicts(EXAMPLE / "checks" / "review-2026-10-03.jsonl", problems)
    assert problems == []
    pairs = cut_pairs(EXAMPLE)
    assert set(verdicts) == {pair.id for pair in pairs}
    assert all(verdicts[pair.id].prompt_hash == pair.prompt_hash for pair in pairs)


def test_example_cli_review_roundtrip_uses_simulated_judgements_only_in_copy(
    tmp_path: Path,
) -> None:
    """Simulation tests data binding and bookkeeping without calling a reviewer."""
    original_state = {
        path.relative_to(EXAMPLE): path.read_bytes()
        for path in EXAMPLE.rglob("*")
        if path.is_file()
    }
    copied = tmp_path / "example"
    shutil.copytree(EXAMPLE, copied)
    # Reset only the temporary variant so simulation cannot inherit a real check.
    for folder in ("20_distillates", "30_assertions", "40_output"):
        for path in (copied / folder).rglob("*.md"):
            text = path.read_text(encoding="utf-8").replace(
                "status: validated", "status: grounded"
            )
            text = re.sub(r"(?m)^checked:\n(?:[ \t]+[^\n]*\n)*", "checked: {}\n", text)
            path.write_text(text, encoding="utf-8")
    prompts = tmp_path / "prompts.jsonl"
    _run("review.py", "emit", str(copied), "--out", str(prompts))
    records = [
        json.loads(line) for line in prompts.read_text(encoding="utf-8").splitlines()
    ]
    verdicts = tmp_path / "simulated-verdicts.jsonl"
    verdicts.write_text(
        "".join(
            json.dumps(
                {
                    "id": record["id"],
                    "prompt_hash": record["prompt_hash"],
                    "verdict": "fully supports",
                    "reviewer": "Explicitly simulated regression-test judgement",
                }
            )
            + "\n"
            for record in records
        ),
        encoding="utf-8",
    )
    before = (copied / "30_assertions" / "prov-entity-definition.md").read_bytes()
    _run("review.py", "judge", str(copied), "--verdicts", str(verdicts))
    assert (
        copied / "30_assertions" / "prov-entity-definition.md"
    ).read_bytes() == before
    _run(
        "review.py",
        "judge",
        str(copied),
        "--verdicts",
        str(verdicts),
        "--apply",
        "--date",
        "2026-10-03",
    )
    for relative in (
        "20_distillates/documents/prov-entity.md",
        "30_assertions/prov-entity-definition.md",
    ):
        text = (copied / relative).read_text(encoding="utf-8")
        assert "machine-review: 2026-10-03" in text
        assert "status: grounded" in text
    checked = validate(copied)
    assert checked.errors == []
    assert checked.warnings == []
    for relative, content in original_state.items():
        assert (EXAMPLE / relative).read_bytes() == content
