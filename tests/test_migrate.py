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

from migrate import KISUG, Summary, migrate  # noqa: E402

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

EXTERNAL_DISTILLATE = """---
type: distillat
herkunft: extern
themen: ["[[Governance]]"]
status: verifiziert
created: 2026-01-01
updated: 2026-01-01
---

# Externes Distillat

## Kernaussagen

- The publication says something. ^s1

> "a quotation instead of an anchor" (p. 1)
"""

GITIGNORE = "_sources/*\n!_sources/README.md\n"

FILES = {
    ".gitignore": GITIGNORE,
    "_sources/inventar.json": '{"paper": "_sources/paper.docx"}\n',
    "00_volltext/paper.md": REPRESENTATION,
    "10_distillate/intern/paper.md": DISTILLATE,
    "10_distillate/extern/other.md": EXTERNAL_DISTILLATE,
    "20_wissen/aussage-one.md": ASSERTION,
    "20_wissen/MOC-governance.md": MOC,
    "30_strategie/kapitel-1.md": CHAPTER,
    "glossar/llm.md": GLOSSARY,
}


def build(root: Path, extra: dict[str, str] | None = None) -> None:
    for rel, text in {**FILES, **(extra or {})}.items():
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


def test_external_distillates_reenter_at_grounded(tmp_path):
    # Their old `verifiziert` claims a quote check that never ran; only the
    # live quote review may lift them again.
    root = run(tmp_path)
    external = frontmatter(root / "20_distillates" / "extern" / "other.md")
    assert external["status"] == "grounded"
    internal = frontmatter(root / "20_distillates" / "intern" / "paper.md")
    assert internal["status"] == "validated"


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


def run_with(tmp_path: Path, extra: dict[str, str], only: str = "all") -> Summary:
    build(tmp_path, extra)
    return migrate(tmp_path, KISUG, vcs="none", only=only)


def test_a_clean_vault_leaves_no_stale_reference(tmp_path):
    assert run_with(tmp_path, {}).stale == []


def test_an_instance_tool_pointing_at_an_old_folder_is_reported(tmp_path):
    """The failure the check exists for: a linter whose folder constant went stale."""
    summary = run_with(
        tmp_path,
        {"tools/lint.py": 'ROOT = "vault"\nSRC = Path("00_volltext")\n'},
    )
    assert len(summary.stale) == 1
    (ref,) = summary.stale
    assert ref.path == "tools/lint.py"
    assert ref.line == 2
    assert ref.old == "00_volltext"


def test_a_tool_on_the_new_folders_is_not_reported(tmp_path):
    summary = run_with(tmp_path, {"tools/lint.py": 'SRC = Path("10_markdown")\n'})
    assert summary.stale == []


def test_a_line_naming_both_sides_of_a_rename_is_a_migration_note(tmp_path):
    """A journal reporting the rename names old and new together; a stale
    constant names the old side alone."""
    summary = run_with(
        tmp_path,
        {"knowledge/journal.md": "- `00_volltext` was renamed to `10_markdown`.\n"},
    )
    assert summary.stale == []


def test_an_old_folder_name_as_a_word_in_prose_is_not_reported(tmp_path):
    summary = run_with(
        tmp_path,
        {"notes/prosa.md": "Das Glossar und der Volltext, glossar als Wort.\n"},
    )
    assert summary.stale == []


def test_the_folder_phase_alone_reports_nothing(tmp_path):
    """Every content file still points at the old names there; the check is
    meaningful only once the content phase has run."""
    summary = run_with(
        tmp_path, {"tools/lint.py": 'SRC = Path("00_volltext")\n'}, only="folders"
    )
    assert summary.stale == []


def test_a_documented_command_naming_a_missing_path_is_reported(tmp_path):
    """The failure the check exists for: the action layer kept the old command."""
    summary = run_with(
        tmp_path,
        {
            "CLAUDE.md": "Run `python tools/lint.py 10_markdown/` before reporting.\n",
        },
    )
    assert [(ref.path, ref.line, ref.old) for ref in summary.dead_commands] == [
        ("CLAUDE.md", 1, "tools/lint.py")
    ]


def test_a_documented_command_on_existing_paths_is_not_reported(tmp_path):
    summary = run_with(
        tmp_path,
        {
            "CLAUDE.md": (
                "Run `python tools/validate.py .` and read `knowledge/state.md`.\n"
                "Distillates live in `20_distillates/<source-type>s/`.\n"
            ),
            "tools/validate.py": "",
            "knowledge/state.md": "",
        },
    )
    assert summary.dead_commands == []


def test_an_instance_without_an_action_layer_reports_nothing(tmp_path):
    assert run_with(tmp_path, {}).dead_commands == []


def test_the_folder_phase_alone_reports_no_dead_command(tmp_path):
    summary = run_with(
        tmp_path, {"CLAUDE.md": "Run `python tools/gone.py`.\n"}, only="folders"
    )
    assert summary.dead_commands == []


def test_migration_is_idempotent(tmp_path):
    root = run(tmp_path)
    before = {p: p.read_bytes() for p in sorted(root.rglob("*")) if p.is_file()}
    migrate(root, KISUG, vcs="none")
    after = {p: p.read_bytes() for p in sorted(root.rglob("*")) if p.is_file()}
    assert before == after
