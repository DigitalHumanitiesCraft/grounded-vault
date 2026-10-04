"""The nested instances carry copies of the invariant knowledge documents.

Every external instance is a copy of the template, so the two instances nested
in this repository follow the same model. A copy may differ from the root only
in the frontmatter values an instantiation fills, and this test fails the suite
as soon as a root rule change has not reached a copy.
"""

from pathlib import Path

import pytest
import yaml

from validate import split_frontmatter

ROOT = Path(__file__).resolve().parents[1]
INSTANCES = ("examples/prov-entity", "paper")
INVARIANT = ("index", "schema", "operations")
FILLED_KEYS = {"name", "repository", "created", "updated"}


def _parts(path: Path):
    text = path.read_text(encoding="utf-8").replace("\r\n", "\n")
    raw, body = split_frontmatter(text)
    return yaml.safe_load(raw), body


@pytest.mark.parametrize("instance", INSTANCES)
@pytest.mark.parametrize("doc", INVARIANT)
def test_instance_copy_equals_root_apart_from_filled_values(instance, doc):
    root_fm, root_body = _parts(ROOT / "knowledge" / f"{doc}.md")
    copy_fm, copy_body = _parts(ROOT / instance / "knowledge" / f"{doc}.md")
    assert copy_body == root_body, (
        f"{instance}/knowledge/{doc}.md body differs from the root"
    )
    assert set(copy_fm) == set(root_fm)
    for key, value in root_fm.items():
        if key == "project":
            assert set(value) == set(copy_fm["project"])
            continue
        if key in FILLED_KEYS:
            continue
        assert copy_fm[key] == value, (
            f"{instance}/knowledge/{doc}.md frontmatter {key} differs"
        )


@pytest.mark.parametrize("instance", INSTANCES)
@pytest.mark.parametrize("doc", INVARIANT)
def test_instance_copy_has_no_placeholder(instance, doc):
    assert "{{" not in (ROOT / instance / "knowledge" / f"{doc}.md").read_text(
        encoding="utf-8"
    )
