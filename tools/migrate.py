"""Migrate a legacy vault onto the Grounded Vault template chain.

The mechanics are generic and instance-agnostic: folder renaming, path and
wikilink rewriting, section heading renaming, footnote phrase renaming, and a
frontmatter pass that maps the document type, renames keys, reshapes the values
that changed shape, and projects the old status ladder onto the template one.
What a concrete instance
is called stays out of the mechanics and lives in the mapping table at the
bottom of this file, one `Mapping` per instance, selected with `--instance`.

Folder renames go through git by default so history follows the file; a
rehearsal on a working copy without a repository uses `--vcs none`, which takes
the same code path with a plain rename.

The migration is structural. It never invents content: fields the template
requires but the legacy instance never recorded (check dates, source types,
statement IDs) stay missing and are meant to surface as validator errors for
the hand pass that follows.

Usage:
    python tools/migrate.py <vault-root> --instance <name> [--vcs git|none]

Under git, run the two phases apart and commit between them, so the renames
reach history as renames instead of as a delete beside an unrelated add:

    python tools/migrate.py . --instance kisug --only folders
    git commit -m "Rename the folders onto the template chain"
    python tools/migrate.py . --instance kisug --only content

The content phase ends with a scan for surviving references to the retired
folder names in everything the migration does not rewrite, the instance's own
tools, workflows, package scripts, ignore files and documentation. Each hit is
reported with file, line and old name as a warning; the migration itself has
succeeded, and what remains is hand work on the instance. Every instance tool
then needs a run whose reported file count is greater than zero, because a tool
still pointing at a folder that no longer exists walks an empty tree and reports
zero problems, which reads like a passing run.

The same pass reads the instance action layer, CLAUDE.md, and reports every
backtick-quoted command line whose path the instance does not have, so that a
rename the documentation did not follow surfaces before an agent runs it.
"""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from collections.abc import Callable
from dataclasses import dataclass, field
from pathlib import Path

import yaml

ANY_TYPE = "*"

FOOTNOTE_DEF = re.compile(r"^(\[\^[A-Za-z0-9]+\]:\s*)(.*)$")

# The follow-up scan reads code, configuration and documentation, the files a
# migration does not rewrite but which an instance's own tool chain is made of.
SCAN_SUFFIXES = frozenset(
    {
        ".py",
        ".js",
        ".mjs",
        ".cjs",
        ".ts",
        ".toml",
        ".yaml",
        ".yml",
        ".json",
        ".md",
        ".sh",
        ".ps1",
        ".cfg",
        ".ini",
    }
)
SCAN_NAMES = frozenset({".gitignore", ".gitattributes", "Makefile", "Dockerfile"})
# Dependency and build output, never hand-written and never the instance's own.
SCAN_SKIP_DIRS = frozenset(
    {
        ".venv",
        "venv",
        ".tox",
        ".mypy_cache",
        ".ruff_cache",
        ".pytest_cache",
        "site-packages",
        "dist",
        "build",
    }
)


@dataclass(frozen=True)
class Mapping:
    """The instance-specific half of a migration."""

    name: str
    folders: tuple[tuple[str, str], ...] = ()
    rewrite_globs: tuple[str, ...] = ("**/*.md",)
    skip_dirs: tuple[str, ...] = (".git", ".obsidian", "__pycache__", "node_modules")
    headings: tuple[tuple[str, str], ...] = ()
    footnote_phrases: tuple[tuple[str, str], ...] = ()
    type_map: dict[str, str] = field(default_factory=dict)
    transforms: dict[str, tuple[str, ...]] = field(default_factory=dict)
    keys: dict[str, dict[str, str]] = field(default_factory=dict)
    status_map: dict[str, str] = field(default_factory=dict)
    status_default: str | None = None
    status_types: tuple[str, ...] = ()
    # Path prefixes (posix, post-rename) whose documents are forced to
    # `grounded` regardless of status_map, because their old status claims a
    # check that never ran.
    status_grounded_prefixes: tuple[str, ...] = ()


@dataclass(frozen=True)
class StaleReference:
    """One surviving mention of a retired folder name outside the content."""

    path: str
    line: int
    old: str
    text: str


@dataclass
class Summary:
    moved: list[tuple[str, str]] = field(default_factory=list)
    stale: list[StaleReference] = field(default_factory=list)
    dead_commands: list[StaleReference] = field(default_factory=list)
    files_rewritten: int = 0
    paths_rewritten: int = 0
    headings_rewritten: int = 0
    footnotes_rewritten: int = 0
    frontmatter_changed: int = 0
    unmapped_types: dict[str, int] = field(default_factory=dict)
    unmapped_status: dict[str, int] = field(default_factory=dict)


# --------------------------------------------------------------- frontmatter
# Transforms reshape a frontmatter value whose old and new form differ in more
# than its key. They are named in the mapping table and resolved from here, and
# they run after the key renames, so they address fields by their template name.


def records_to_grounding(fm: dict) -> None:
    """Legacy grounding records become single anchored wikilinks.

    A record carrying a block ID collapses into `[[target#^id]]`. A record
    without one has no statement anchor to collapse onto and is left as it
    stands, so the missing anchor stays visible instead of being papered over.
    """
    entries = fm.get("grounding")
    if not isinstance(entries, list):
        return
    rebuilt: list = []
    for entry in entries:
        if not isinstance(entry, dict):
            rebuilt.append(entry)
            continue
        target = str(entry.get("distillat", "")).strip()
        block = str(entry.get("block", "")).strip().lstrip("^")
        if target.endswith("]]") and block:
            rebuilt.append(f"{target[:-2]}#^{block}]]")
        else:
            rebuilt.append(entry)
    fm["grounding"] = rebuilt


def quelle_to_representation(fm: dict) -> None:
    """A distillate of a stored source points at its Markdown representation.

    Only the record shape that names a full text carries that link; a
    bibliographic record does not, and is left for the publication pass.
    """
    quelle = fm.get("quelle")
    if not isinstance(quelle, dict) or "volltext" not in quelle:
        return
    fm["representation"] = quelle["volltext"]
    del fm["quelle"]


def unwrap_topic(fm: dict) -> None:
    """A topic map names its topic as a bare term, not as a link to itself."""
    topic = fm.get("topic")
    if isinstance(topic, str):
        fm["topic"] = topic.strip().strip("[] ")


TRANSFORMS: dict[str, Callable[[dict], None]] = {
    "records_to_grounding": records_to_grounding,
    "quelle_to_representation": quelle_to_representation,
    "unwrap_topic": unwrap_topic,
}


def _scoped(table: dict[str, dict], doctype: str | None) -> dict:
    merged = dict(table.get(ANY_TYPE, {}))
    merged.update(table.get(str(doctype), {}))
    return merged


def migrate_frontmatter(
    fm: dict, mapping: Mapping, summary: Summary, rel: str = ""
) -> dict:
    """Type, keys, values and status of one document, in that order."""
    old_type = fm.get("type")
    if old_type is not None:
        if old_type in mapping.type_map:
            fm["type"] = mapping.type_map[old_type]
        elif mapping.type_map and old_type not in mapping.type_map.values():
            summary.unmapped_types[str(old_type)] = (
                summary.unmapped_types.get(str(old_type), 0) + 1
            )
    doctype = fm.get("type")

    renames = _scoped(mapping.keys, doctype)
    if renames:
        fm = {renames.get(key, key): value for key, value in fm.items()}

    for name in mapping.transforms.get(ANY_TYPE, ()) + mapping.transforms.get(
        str(doctype), ()
    ):
        TRANSFORMS[name](fm)

    if str(doctype) in mapping.status_types and "status" in fm:
        old_status = str(fm["status"])
        if any(rel.startswith(prefix) for prefix in mapping.status_grounded_prefixes):
            fm["status"] = "grounded"
            return fm
        already_migrated = old_status in set(mapping.status_map.values()) | {
            mapping.status_default
        }
        if already_migrated:
            pass  # a rerun must not push an already mapped status to the default
        elif old_status in mapping.status_map:
            fm["status"] = mapping.status_map[old_status]
        elif mapping.status_default is not None:
            fm["status"] = mapping.status_default
            summary.unmapped_status[old_status] = (
                summary.unmapped_status.get(old_status, 0) + 1
            )
    return fm


# ---------------------------------------------------------------- text passes


def _path_pattern(mapping: Mapping) -> re.Pattern[str] | None:
    """Old folder names in a path position, longest name first."""
    olds = sorted((old for old, _ in mapping.folders), key=len, reverse=True)
    if not olds:
        return None
    alternation = "|".join(re.escape(old) for old in olds)
    return re.compile(rf"(?<![A-Za-z0-9_./-])({alternation})(?=/)")


def rewrite_paths(text: str, mapping: Mapping) -> tuple[str, int]:
    pattern = _path_pattern(mapping)
    if pattern is None:
        return text, 0
    table = dict(mapping.folders)
    count = 0

    def replace(match: re.Match[str]) -> str:
        nonlocal count
        count += 1
        return table[match.group(1)]

    return pattern.sub(replace, text), count


def rewrite_headings(body: str, mapping: Mapping) -> tuple[str, int]:
    count = 0
    lines = body.splitlines(keepends=True)
    for index, line in enumerate(lines):
        stripped = line.rstrip("\r\n")
        for old, new in mapping.headings:
            if stripped.strip() == old:
                lines[index] = line.replace(stripped, new, 1)
                count += 1
                break
    return "".join(lines), count


def rewrite_footnotes(body: str, mapping: Mapping) -> tuple[str, int]:
    """Only the keyword that opens a footnote definition, never running prose."""
    count = 0
    lines = body.splitlines(keepends=True)
    for index, line in enumerate(lines):
        match = FOOTNOTE_DEF.match(line.rstrip("\r\n"))
        if not match:
            continue
        head, rest = match.groups()
        for old, new in mapping.footnote_phrases:
            if rest.startswith(old):
                rest = new + rest[len(old) :]
                count += 1
                break
        else:
            continue
        lines[index] = head + rest + line[len(line.rstrip("\r\n")) :]
    return "".join(lines), count


def _split_frontmatter(text: str) -> tuple[str, str] | None:
    if not text.startswith("---\n"):
        return None
    end = text.find("\n---", 4)
    if end < 0:
        return None
    return text[4:end], text[end + 4 :]


def migrate_file(path: Path, mapping: Mapping, summary: Summary, rel: str = "") -> None:
    original = path.read_text(encoding="utf-8")
    text, paths = rewrite_paths(original, mapping)
    summary.paths_rewritten += paths

    if path.suffix != ".md":
        if text != original:
            path.write_text(text, encoding="utf-8")
            summary.files_rewritten += 1
        return

    # Body rewrites do not depend on frontmatter; a generated export carries
    # footnotes without any.
    split = _split_frontmatter(text)
    raw_fm, body = split if split else (None, text)
    body, headings = rewrite_headings(body, mapping)
    body, footnotes = rewrite_footnotes(body, mapping)
    summary.headings_rewritten += headings
    summary.footnotes_rewritten += footnotes

    if raw_fm is None:
        result = body
    else:
        try:
            fm = yaml.safe_load(raw_fm) or {}
        except yaml.YAMLError as exc:
            raise SystemExit(f"{path}: frontmatter is not valid YAML: {exc}") from exc
        if not isinstance(fm, dict):
            raise SystemExit(f"{path}: frontmatter is not a mapping")
        migrated = migrate_frontmatter(dict(fm), mapping, summary, rel)
        if migrated != fm:
            summary.frontmatter_changed += 1
        dumped = yaml.safe_dump(
            migrated,
            sort_keys=False,
            allow_unicode=True,
            default_flow_style=False,
            width=10**6,
        )
        result = f"---\n{dumped}---{body}"

    if result != original:
        path.write_text(result, encoding="utf-8")
        summary.files_rewritten += 1


# ------------------------------------------------------------------- folders


def move(src: Path, dst: Path, vcs: str, root: Path) -> None:
    if vcs == "git":
        subprocess.run(
            ["git", "mv", str(src.relative_to(root)), str(dst.relative_to(root))],
            cwd=root,
            check=True,
        )
    else:
        src.rename(dst)


def rename_folders(root: Path, mapping: Mapping, vcs: str, summary: Summary) -> None:
    for old, new in mapping.folders:
        src, dst = root / old, root / new
        if not src.is_dir():
            continue
        if dst.exists():
            raise SystemExit(f"cannot rename {old} to {new}: {new} already exists")
        move(src, dst, vcs, root)
        summary.moved.append((old, new))


def content_files(root: Path, mapping: Mapping) -> list[Path]:
    seen: dict[Path, None] = {}
    for pattern in mapping.rewrite_globs:
        for path in sorted(root.glob(pattern)):
            if not path.is_file():
                continue
            if any(part in mapping.skip_dirs for part in path.relative_to(root).parts):
                continue
            seen.setdefault(path, None)
    return list(seen)


# ------------------------------------------------------- follow-up folder scan
# A migration renames the folders and rewrites what the mapping declares as
# content. Everything else an instance carries keeps pointing where it pointed:
# its own linter, its analysis and build scripts, CI workflows, package scripts,
# ignore files, documentation. A folder constant left on the old name does not
# raise; the tool walks an empty tree, counts zero files and reports zero
# problems, so a dead run reads like a passing one. The scan below makes that
# state visible right where it is created.


def _scan_patterns(mapping: Mapping) -> tuple[re.Pattern[str], re.Pattern[str]] | None:
    """A loose pattern for code and configuration, a strict one for Markdown.

    In code and configuration an old folder name is a path by default, so any
    standalone occurrence counts. Markdown also carries prose, where a name like
    `glossar` is an ordinary word, so there the name must sit in a path position
    or be quoted whole (quotes, apostrophes or backticks) to count.
    """
    olds = sorted((old for old, _ in mapping.folders), key=len, reverse=True)
    if not olds:
        return None
    alt = "|".join(re.escape(old) for old in olds)
    loose = re.compile(rf"(?<![A-Za-z0-9_.\-])({alt})(?![A-Za-z0-9_\-])")
    strict = re.compile(
        rf"""(?:['"`]({alt})['"`]|(?<![A-Za-z0-9_.\-])({alt})(?=[/\\]))"""
    )
    return loose, strict


def scan_files(root: Path, mapping: Mapping) -> list[Path]:
    skip = SCAN_SKIP_DIRS | set(mapping.skip_dirs)
    found = []
    for path in sorted(root.rglob("*")):
        if not path.is_file():
            continue
        rel = path.relative_to(root)
        if any(part in skip for part in rel.parts):
            continue
        if path.suffix.lower() in SCAN_SUFFIXES or path.name in SCAN_NAMES:
            found.append(path)
    return found


def stale_references(root: Path, mapping: Mapping) -> list[StaleReference]:
    """Mentions of a retired folder name that the migration did not reach.

    Files the migration rewrote clear themselves, since they no longer hold an
    old name, so no folder needs excluding and a tool that happens to live
    inside a content folder is checked too. A line that names both sides of the
    same rename is read as a report about the migration (a journal entry, the
    mapping table itself) and is not a finding.
    """
    patterns = _scan_patterns(mapping)
    if patterns is None:
        return []
    loose, strict = patterns
    table = dict(mapping.folders)
    findings: list[StaleReference] = []
    for path in scan_files(root, mapping):
        pattern = strict if path.suffix.lower() == ".md" else loose
        try:
            text = path.read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError):
            continue
        for number, line in enumerate(text.splitlines(), start=1):
            for match in pattern.finditer(line):
                old = next(group for group in match.groups() if group)
                if table[old] in line:
                    continue
                findings.append(
                    StaleReference(
                        path=path.relative_to(root).as_posix(),
                        line=number,
                        old=old,
                        text=line.strip(),
                    )
                )
    return findings


# The action layer documents the instance's commands in backticks. A rename that
# the documentation did not follow leaves a command line naming a path that no
# longer exists, and the next agent runs it, gets a file-not-found and has no way
# to tell an outdated instruction from a broken vault.

INSTANCE_ACTION_LAYER = "CLAUDE.md"
BACKTICKED = re.compile(r"`([^`\n]+)`")
# Placeholder and glob syntax stands for a path rather than naming one.
UNRESOLVABLE = ("<", ">", "{", "}", "*", "://", "$")


def _documented_paths(command: str) -> list[str]:
    """The path-like tokens of one backtick-quoted command line."""
    found = []
    for raw in command.split():
        token = raw.strip("\"'()[],;:").rstrip(".")
        if token.startswith("-") or any(part in token for part in UNRESOLVABLE):
            continue
        if "/" in token or token.endswith(".py"):
            found.append(token)
    return found


def dead_commands(root: Path) -> list[StaleReference]:
    """Documented command lines whose paths the instance does not have."""
    path = root / INSTANCE_ACTION_LAYER
    if not path.is_file():
        return []
    findings: list[StaleReference] = []
    for number, line in enumerate(
        path.read_text(encoding="utf-8").splitlines(), start=1
    ):
        for match in BACKTICKED.finditer(line):
            for token in _documented_paths(match.group(1)):
                if not (root / token).exists():
                    findings.append(
                        StaleReference(
                            path=INSTANCE_ACTION_LAYER,
                            line=number,
                            old=token,
                            text=line.strip(),
                        )
                    )
    return findings


def migrate(root: Path, mapping: Mapping, vcs: str, only: str = "all") -> Summary:
    """Rename the folders, then rewrite the files that point into them.

    Running the two phases as separate commits keeps the renames pure, so git
    records them as renames rather than as a delete plus an unrelated add.
    """
    summary = Summary()
    if only in ("all", "folders"):
        rename_folders(root, mapping, vcs, summary)
    if only in ("all", "content"):
        for path in content_files(root, mapping):
            migrate_file(path, mapping, summary, path.relative_to(root).as_posix())
        # Only meaningful once the content pass has run; after the folder phase
        # alone every content file still points at the old names.
        summary.stale = stale_references(root, mapping)
        summary.dead_commands = dead_commands(root)
    return summary


# ==========================================================================
# Instance mapping table. Everything above is generic; everything below names
# one concrete legacy vault. Add a Mapping per instance and select it with
# --instance.
# ==========================================================================

KISUG = Mapping(
    name="kisug",
    folders=(
        ("_sources", "00_sources"),
        ("00_volltext", "10_markdown"),
        ("10_distillate", "20_distillates"),
        ("20_wissen", "30_assertions"),
        ("30_strategie", "40_output"),
        ("glossar", "glossary"),
    ),
    # .gitignore names the old folders; leaving it be would unignore the
    # source originals it keeps out of the repository.
    rewrite_globs=("**/*.md", "00_sources/*.json", ".gitignore"),
    headings=(("## Kernaussagen", "## Core statements"),),
    footnote_phrases=(
        ("Belegt durch ", "Grounded in "),
        ("Setzung:", "Posit:"),
    ),
    type_map={
        "volltext": "representation",
        "distillat": "distillate",
        "aussage": "assertion",
        "strategie": "chapter",
        "glossar": "glossary",
        "moc": "moc",
    },
    transforms={
        "assertion": ("records_to_grounding",),
        "distillate": ("quelle_to_representation",),
        "moc": ("unwrap_topic",),
    },
    keys={
        ANY_TYPE: {"themen": "topics"},
        "representation": {"quelle": "source"},
        "assertion": {"belege": "grounding"},
        "chapter": {"stützt-sich-auf": "assertions"},
        "moc": {"thema": "topic"},
    },
    status_map={"verifiziert": "validated", "gestützt": "validated"},
    status_default="grounded",
    status_types=("distillate", "assertion", "chapter"),
    # The external distillates carry `verifiziert` although the quote check
    # against the originals never ran; they re-enter at grounded and climb only
    # through the live quote review.
    status_grounded_prefixes=("20_distillates/extern/",),
)

# The Promptotyping paper vault (DigitalHumanitiesCraft/Promptotyping, vault/)
# was instantiated from the pre-rename template and is already English with the
# template's key names and status vocabulary; the migration is the folder chain
# and the claim-to-assertion rename. Its sources are kept out of git by the
# repository-root .gitignore, which lies outside the vault root and is updated
# by hand, as are the site files that read the vault.
PROMPTOTYPING = Mapping(
    name="promptotyping",
    folders=(
        ("_sources", "00_sources"),
        ("00_representation", "10_markdown"),
        ("10_distillates", "20_distillates"),
        ("20_claims", "30_assertions"),
        ("30_deliverable", "40_output"),
    ),
    # Source originals stay byte-identical (the YAML re-dump would reformat
    # them); the pre-rename example fixtures are replaced by the template's
    # tests/fixtures rather than migrated.
    skip_dirs=(
        ".git",
        ".obsidian",
        "__pycache__",
        "node_modules",
        "00_sources",
        "examples",
        "tests",
    ),
    # Identity rows declare the types that already carry template names, so
    # the summary flags only a genuinely unknown type.
    type_map={
        "claim": "assertion",
        "representation": "representation",
        "distillate": "distillate",
        "moc": "moc",
        "glossary": "glossary",
    },
)

INSTANCES = {mapping.name: mapping for mapping in (KISUG, PROMPTOTYPING)}


def main() -> None:
    if sys.platform == "win32":
        sys.stdout.reconfigure(encoding="utf-8")
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("root", type=Path, help="vault root directory")
    parser.add_argument("--instance", required=True, choices=sorted(INSTANCES))
    parser.add_argument(
        "--vcs",
        choices=("git", "none"),
        default="git",
        help="git mv keeps history; none is for a rehearsal on a working copy",
    )
    parser.add_argument(
        "--only",
        choices=("all", "folders", "content"),
        default="all",
        help="run one phase; folders then content, committed apart, keeps renames pure",
    )
    args = parser.parse_args()

    summary = migrate(
        args.root.resolve(), INSTANCES[args.instance], args.vcs, args.only
    )
    for old, new in summary.moved:
        print(f"moved {old} -> {new}")
    print(
        f"{summary.files_rewritten} file(s) rewritten, "
        f"{summary.paths_rewritten} path reference(s), "
        f"{summary.headings_rewritten} heading(s), "
        f"{summary.footnotes_rewritten} footnote keyword(s), "
        f"{summary.frontmatter_changed} frontmatter block(s)"
    )
    for label, table in (
        ("type not in the mapping table", summary.unmapped_types),
        ("status fell through to the default", summary.unmapped_status),
    ):
        for value, count in sorted(table.items()):
            print(f"note: {label}: {value!r} ({count})")

    if summary.stale:
        print(
            f"\nwarning: {len(summary.stale)} reference(s) to a renamed folder "
            "survive outside the rewritten content:"
        )
        for ref in summary.stale:
            print(f"  {ref.path}:{ref.line}: {ref.old}: {ref.text}")
        print(
            "Point every instance tool, workflow and config at the new folder names, "
            "then rerun each of them and check the file count it reports, "
            "because a run over zero files reports zero problems and is not a pass."
        )

    if summary.dead_commands:
        print(
            f"\nwarning: {len(summary.dead_commands)} command(s) documented in "
            f"{INSTANCE_ACTION_LAYER} name a path the instance does not have:"
        )
        for ref in summary.dead_commands:
            print(f"  {ref.path}:{ref.line}: {ref.old}: {ref.text}")
        print(
            "Correct the action layer, because an agent runs what it documents "
            "and a path that is not there fails as a broken vault rather than as "
            "an outdated instruction."
        )


if __name__ == "__main__":
    main()
