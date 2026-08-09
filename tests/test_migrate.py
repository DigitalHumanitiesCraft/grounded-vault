"""Tests for tools/migrate.py on a synthetic legacy vault.

The fixture is written per test into a temporary directory and carries one
specimen of every mechanic: a folder that is renamed, links and paths that point
into it, a section heading, footnote keywords next to prose that must survive
untouched, and the frontmatter of each document type.
"""

import sys
from pathlib import Path

import yaml

REPO = Path(__file__).parents[1]
sys.path.insert(0, str(REPO / "tools"))

from migrate import KISUG, migrate  # noqa: E402

REPRESENTATION = """---
type: volltext
herkunft: intern
quelle: "[[_sources/paper.docx]]"
themen: [Governance]
created: 2026-01-01
updated: 2026-01-01
---

# Paper

- A claim of the source. ^b1
"""

DISTILLATE = """---
type: distillat
herkunft: intern
quelle:
  original: "[[_sources/paper.docx]]"
  volltext: "[[00_volltext/paper]]"
  format: docx
themen: ["[[Governance]]"]
status: verifiziert
created: 2026-01-01
updated: 2026-01-01
---

# Distillat

## Kernaussagen

- The source says something. [[00_volltext/paper#^b1]] ^s1

## Begriffe und Setzungen

- **Setzung**: the word Setzung in prose stays as it is.
"""

ASSERTION = """---
type: aussage
herkunft: intern
themen: ["[[Governance]]"]
belege:
  - distillat: "[[10_distillate/intern/paper]]"
    block: ^s1
  - distillat: "[[10_distillate/extern/other]]"
    zitat: "a quotation instead of an anchor"
status: gestützt
created: 2026-01-01
updated: 2026-01-01
---

# Aussage

## Stützung

- [[10_distillate/intern/paper#^s1]]: grounds the assertion.
"""

MOC = """---
type: moc
thema: "[[Governance]]"
created: 2026-01-01
updated: 2026-01-01
---

# Governance

- [[20_wissen/aussage-one]]
"""

CHAPTER = """---
type: strategie
themen: ["[[Governance]]"]
stützt-sich-auf:
  - "[[20_wissen/aussage-one]]"
status: draft
created: 2026-01-01
updated: 2026-01-01
---

# Chapter

Some text.[^1][^2]

[^1]: Belegt durch [[20_wissen/aussage-one|the assertion]].
[^2]: Setzung: a decision of the authors.
"""

GLOSSARY = """---
type: glossar
id: llm
updated: 2026-01-01
---

# LLM

See [[20_wissen/aussage-one]].
"""

GITIGNORE = "_sources/*\n!_sources/README.md\n"

FILES = {
    ".gitignore": GITIGNORE,
    "_sources/inventar.json": '{"paper": "_sources/paper.docx"}\n',
    "00_volltext/paper.md": REPRESENTATION,
    "10_distillate/intern/paper.md": DISTILLATE,
    "20_wissen/aussage-one.md": ASSERTION,
    "20_wissen/MOC-governance.md": MOC,
    "30_strategie/kapitel-1.md": CHAPTER,
    "glossar/llm.md": GLOSSARY,
}


def build(root: Path) -> None:
    for rel, text in FILES.items():
        path = root / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")


def frontmatter(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    return yaml.safe_load(text[4 : text.find("\n---", 4)])


def run(tmp_path: Path) -> Path:
    build(tmp_path)
    migrate(tmp_path, KISUG, vcs="none")
    return tmp_path


def test_folders_are_renamed(tmp_path):
    root = run(tmp_path)
    for old, new in KISUG.folders:
        assert not (root / old).exists()
        assert (root / new).is_dir()


def test_paths_are_rewritten_in_links_and_in_json(tmp_path):
    root = run(tmp_path)
    body = (root / "30_assertions" / "aussage-one.md").read_text(encoding="utf-8")
    assert "[[20_distillates/intern/paper#^s1]]" in body
    assert "10_distillate" not in body
    assert "00_sources/paper.docx" in (root / "00_sources" / "inventar.json").read_text(
        encoding="utf-8"
    )


def test_types_keys_and_status_are_mapped(tmp_path):
    root = run(tmp_path)
    representation = frontmatter(root / "10_markdown" / "paper.md")
    assert representation["type"] == "representation"
    assert representation["source"] == "[[00_sources/paper.docx]]"
    assert representation["topics"] == ["Governance"]

    distillate = frontmatter(root / "20_distillates" / "intern" / "paper.md")
    assert distillate["type"] == "distillate"
    assert distillate["status"] == "validated"
    assert distillate["representation"] == "[[10_markdown/paper]]"
    assert "quelle" not in distillate

    chapter = frontmatter(root / "40_output" / "kapitel-1.md")
    assert chapter["type"] == "chapter"
    assert chapter["assertions"] == ["[[30_assertions/aussage-one]]"]
    assert chapter["status"] == "grounded"  # draft has no template counterpart

    assert frontmatter(root / "30_assertions" / "MOC-governance.md")["topic"] == (
        "Governance"
    )
    assert frontmatter(root / "glossary" / "llm.md")["type"] == "glossary"


def test_grounding_records_become_anchored_links(tmp_path):
    root = run(tmp_path)
    grounding = frontmatter(root / "30_assertions" / "aussage-one.md")["grounding"]
    assert grounding[0] == "[[20_distillates/intern/paper#^s1]]"
    # A record without a block ID keeps its shape, so the gap stays visible.
    assert isinstance(grounding[1], dict)
    assert grounding[1]["zitat"] == "a quotation instead of an anchor"


def test_heading_is_renamed_and_prose_is_not(tmp_path):
    root = run(tmp_path)
    body = (root / "20_distillates" / "intern" / "paper.md").read_text(encoding="utf-8")
    assert "## Core statements" in body
    assert "## Kernaussagen" not in body
    assert "## Begriffe und Setzungen" in body
    assert "the word Setzung in prose stays as it is" in body


def test_footnote_keywords_are_renamed(tmp_path):
    root = run(tmp_path)
    body = (root / "40_output" / "kapitel-1.md").read_text(encoding="utf-8")
    assert "[^1]: Grounded in [[30_assertions/aussage-one|the assertion]]." in body
    assert "[^2]: Posit: a decision of the authors." in body


def test_gitignore_follows_the_renamed_folders(tmp_path):
    """Otherwise the ignore rule misses and the source originals get staged."""
    root = run(tmp_path)
    assert (root / ".gitignore").read_text(encoding="utf-8") == (
        "00_sources/*\n!00_sources/README.md\n"
    )


def test_phases_run_apart(tmp_path):
    build(tmp_path)
    migrate(tmp_path, KISUG, vcs="none", only="folders")
    assert (tmp_path / "20_distillates" / "intern" / "paper.md").is_file()
    assert "[[00_volltext/paper]]" in (
        tmp_path / "20_distillates" / "intern" / "paper.md"
    ).read_text(encoding="utf-8")
    migrate(tmp_path, KISUG, vcs="none", only="content")
    assert (
        frontmatter(tmp_path / "20_distillates" / "intern" / "paper.md")[
            "representation"
        ]
        == "[[10_markdown/paper]]"
    )


def test_migration_is_idempotent(tmp_path):
    root = run(tmp_path)
    before = {p: p.read_bytes() for p in sorted(root.rglob("*")) if p.is_file()}
    migrate(root, KISUG, vcs="none")
    after = {p: p.read_bytes() for p in sorted(root.rglob("*")) if p.is_file()}
    assert before == after
