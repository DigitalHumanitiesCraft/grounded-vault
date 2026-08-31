"""Tests for the deterministic project-page generator."""

import sys
from pathlib import Path

REPO = Path(__file__).parents[1]
sys.path.insert(0, str(REPO / "tools"))

from build_docs import REPOSITORY_URL, _inline  # noqa: E402


def test_relative_links_resolve_from_their_source_document() -> None:
    rendered = _inline(
        "Read [the paper](../paper/README.md#scope).",
        Path("docs/concept.md"),
    )

    assert f'href="{REPOSITORY_URL}/blob/main/paper/README.md#scope"' in rendered


def test_external_and_fragment_links_remain_unchanged() -> None:
    rendered = _inline(
        "Use [the site](https://example.org/a) or [this section](#part).",
        Path("README.md"),
    )

    assert 'href="https://example.org/a"' in rendered
    assert 'href="#part"' in rendered
