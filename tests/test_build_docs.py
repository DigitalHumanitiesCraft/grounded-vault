"""Tests for the deterministic project-page generator."""

import subprocess
import sys
from pathlib import Path

from build_docs import REPOSITORY_URL, _inline

REPO = Path(__file__).parents[1]


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


def test_the_page_is_written_with_lf_line_endings(tmp_path: Path) -> None:
    """A rebuild on Windows must not turn every line of the page into a diff."""
    output = tmp_path / "index.html"
    result = subprocess.run(
        [
            sys.executable,
            str(REPO / "tools" / "build_docs.py"),
            "--date",
            "2026-01-01",
            "--output",
            str(output),
        ],
        capture_output=True,
        text=True,
        check=False,
    )
    assert result.returncode == 0, result.stderr
    assert result.stdout.startswith("OK ")
    assert b"\r\n" not in output.read_bytes()
