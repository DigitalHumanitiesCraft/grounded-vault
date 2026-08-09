"""Generate the project page docs/index.html from the repository's own documents.

Data flow: README.md, docs/concept.md and the knowledge documents are read in a
fixed order, their YAML frontmatter is stripped, their Markdown is converted to
HTML and the sections are wrapped in one self-contained page with inline CSS.

The Markdown subset covers what these documents actually use: headings,
paragraphs, lists (nested, with block content in an item), tables, blockquotes,
fenced code, inline code, bold, italic, ordinary links and wikilinks. Complete
CommonMark coverage is deliberately out of scope; a document that needs more
syntax is the wrong input for this page.

The generation date is a required argument rather than the system date, so that
a rebuild of an older state stays reproducible.

Usage: python tools/build_docs.py --date 2026-08-09
"""

from __future__ import annotations

import argparse
import html
import re
import sys
from pathlib import Path

REPOSITORY_URL = "https://github.com/DigitalHumanitiesCraft/grounded-vault"

# (anchor id, section title, source file relative to the vault root)
SECTIONS = [
    ("start", "Start", "README.md"),
    ("concept", "Concept", "docs/concept.md"),
    ("terminology", "Terminology", "knowledge/index.md"),
    ("schema", "Schema", "knowledge/schema.md"),
    ("operations", "Operations", "knowledge/operations.md"),
]

CHAIN = [
    ("00_sources", "the originals exactly as they arrived"),
    ("10_markdown", "one Markdown form per source, carrying block IDs"),
    ("20_distillates", "one distillate per source, anchored into it"),
    ("30_assertions", "atomic statements grounded in distillates"),
    ("40_output", "chapters footnoted to assertions"),
]

_FRONTMATTER = re.compile(r"\A---\r?\n.*?\r?\n---\r?\n", re.DOTALL)
_CODE_SPAN = re.compile(r"`([^`]+)`")
_WIKILINK = re.compile(r"\[\[([^\]]+)\]\]")
_LINK = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")
_BOLD = re.compile(r"\*\*(.+?)\*\*")
_ITALIC = re.compile(r"(?<![\w*])\*([^*\n]+)\*(?![\w*])")
_HEADING = re.compile(r"^(#{1,6})\s+(.*)$")
_ITEM = re.compile(r"^(\s*)([-*]|\d+[.)])\s+(.*)$")
_TABLE_RULE = re.compile(r"^\s*\|[\s:|-]+\|\s*$")


def _inline(text: str) -> str:
    """Convert inline Markdown, keeping code spans free of further markup."""
    parts = _CODE_SPAN.split(text)
    out = []
    for index, part in enumerate(parts):
        if index % 2:
            out.append(f"<code>{html.escape(part)}</code>")
            continue
        piece = html.escape(part)
        piece = _WIKILINK.sub(lambda m: f"<code>{m.group(1)}</code>", piece)
        piece = _LINK.sub(lambda m: f'<a href="{m.group(2)}">{m.group(1)}</a>', piece)
        piece = _BOLD.sub(r"<strong>\1</strong>", piece)
        piece = _ITALIC.sub(r"<em>\1</em>", piece)
        out.append(piece)
    return "".join(out)


def _starts_block(line: str) -> bool:
    stripped = line.lstrip()
    return (
        not stripped
        or stripped.startswith(("```", ">", "|"))
        or bool(_HEADING.match(line))
        or bool(_ITEM.match(line))
    )


def _split_row(line: str) -> list[str]:
    return [cell.strip() for cell in line.strip().strip("|").split("|")]


def _dedent(lines: list[str]) -> list[str]:
    indents = [len(line) - len(line.lstrip()) for line in lines if line.strip()]
    cut = min(indents) if indents else 0
    return [line[cut:] if line.strip() else "" for line in lines]


def _render_fence(lines: list[str], start: int) -> tuple[str, int]:
    index = start + 1
    body = []
    while index < len(lines) and not lines[index].lstrip().startswith("```"):
        body.append(lines[index])
        index += 1
    code = html.escape("\n".join(_dedent(body)))
    return f"<pre><code>{code}</code></pre>", index + 1


def _render_table(lines: list[str], start: int) -> tuple[str, int]:
    header = _split_row(lines[start])
    index = start + 2
    rows = []
    while index < len(lines) and lines[index].lstrip().startswith("|"):
        rows.append(_split_row(lines[index]))
        index += 1
    head = "".join(f"<th>{_inline(cell)}</th>" for cell in header)
    body = "".join(
        "<tr>" + "".join(f"<td>{_inline(cell)}</td>" for cell in row) + "</tr>"
        for row in rows
    )
    table = f"<table><thead><tr>{head}</tr></thead><tbody>{body}</tbody></table>"
    return f'<div class="scroll">{table}</div>', index


def _render_quote(lines: list[str], start: int) -> tuple[str, int]:
    index = start
    body = []
    while index < len(lines) and lines[index].lstrip().startswith(">"):
        body.append(lines[index].lstrip()[1:].removeprefix(" "))
        index += 1
    return f"<blockquote>{_render_blocks(body)}</blockquote>", index


def _render_item(buffer: list[str]) -> str:
    first = _inline(buffer[0].strip())
    rest = _dedent(buffer[1:])
    inner = _render_blocks(rest) if any(line.strip() for line in rest) else ""
    return f"<li>{first}{inner}</li>"


def _render_list(lines: list[str], start: int) -> tuple[str, int]:
    match = _ITEM.match(lines[start])
    if match is None:
        raise ValueError(f"not a list item: {lines[start]!r}")
    base = len(match.group(1))
    ordered = match.group(2)[0].isdigit()
    index = start
    items: list[str] = []
    buffer: list[str] = []
    while index < len(lines):
        line = lines[index]
        item = _ITEM.match(line)
        indent = len(line) - len(line.lstrip())
        if item and indent == base:
            if buffer:
                items.append(_render_item(buffer))
            buffer = [item.group(3)]
        elif not line.strip():
            # A blank line ends the list unless an indented continuation or a
            # further item at the same level follows (loose list).
            following = next((x for x in lines[index + 1 :] if x.strip()), "")
            following_indent = len(following) - len(following.lstrip())
            continues = following_indent > base or (
                following_indent == base and _ITEM.match(following)
            )
            if not following or not continues:
                break
            buffer.append("")
        elif indent > base and buffer:
            buffer.append(line)
        else:
            break
        index += 1
    if buffer:
        items.append(_render_item(buffer))
    tag = "ol" if ordered else "ul"
    return f"<{tag}>{''.join(items)}</{tag}>", index


def _render_blocks(lines: list[str]) -> str:
    out: list[str] = []
    index = 0
    while index < len(lines):
        line = lines[index]
        if not line.strip():
            index += 1
        elif line.lstrip().startswith("```"):
            block, index = _render_fence(lines, index)
            out.append(block)
        elif heading := _HEADING.match(line):
            level = min(len(heading.group(1)), 6)
            out.append(f"<h{level}>{_inline(heading.group(2))}</h{level}>")
            index += 1
        elif (
            line.lstrip().startswith("|")
            and index + 1 < len(lines)
            and _TABLE_RULE.match(lines[index + 1])
        ):
            block, index = _render_table(lines, index)
            out.append(block)
        elif line.lstrip().startswith(">"):
            block, index = _render_quote(lines, index)
            out.append(block)
        elif _ITEM.match(line):
            block, index = _render_list(lines, index)
            out.append(block)
        else:
            paragraph = [line.strip()]
            index += 1
            while index < len(lines) and not _starts_block(lines[index]):
                paragraph.append(lines[index].strip())
                index += 1
            out.append(f"<p>{_inline(' '.join(paragraph))}</p>")
    return "".join(out)


def _prepare(text: str) -> list[str]:
    """Strip frontmatter, drop the document H1 and demote the remaining headings."""
    body = _FRONTMATTER.sub("", text).replace("\r\n", "\n")
    lines = body.split("\n")
    out = []
    seen_title = False
    for line in lines:
        heading = _HEADING.match(line)
        if heading and len(heading.group(1)) == 1 and not seen_title:
            seen_title = True
            continue
        if heading:
            out.append("#" + line)
        else:
            out.append(line)
    return out


def _render_section(anchor: str, title: str, path: Path) -> str:
    if not path.is_file():
        raise FileNotFoundError(f"source document missing: {path}")
    body = _render_blocks(_prepare(path.read_text(encoding="utf-8")))
    return (
        f'<section id="{anchor}">\n<h2>{html.escape(title)}</h2>\n{body}\n</section>\n'
    )


def _render_chain() -> str:
    steps = []
    for position, (name, note) in enumerate(CHAIN):
        if position:
            steps.append('<div class="chain-arrow" aria-hidden="true">&#8594;</div>')
        steps.append(
            f'<div class="chain-step"><span class="chain-name">{name}</span>'
            f'<span class="chain-note">{note}</span></div>'
        )
    return (
        '<div class="chain" role="img" aria-label="The chain of the five layers: '
        f'{"; ".join(name + ", " + note for name, note in CHAIN)}">'
        f"{''.join(steps)}</div>"
    )


CSS = """
:root {
  color-scheme: light dark;
  --bg: #fdfdfc; --fg: #1c1c1a; --muted: #63635d; --rule: #dcdcd5;
  --accent: #3a5a78; --code-bg: #f2f2ee; --box: #f7f7f4;
}
@media (prefers-color-scheme: dark) {
  :root {
    --bg: #16171a; --fg: #e6e6e2; --muted: #9b9b95; --rule: #33353a;
    --accent: #93b4d0; --code-bg: #202227; --box: #1d1f23;
  }
}
* { box-sizing: border-box; }
body {
  margin: 0; background: var(--bg); color: var(--fg);
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
  font-size: 1.02rem; line-height: 1.7; text-rendering: optimizeLegibility;
}
.wrap { max-width: 46rem; margin: 0 auto; padding: 0 1.25rem 6rem; }
header.page { padding: 3.5rem 0 1.5rem; }
h1 { font-size: 2.1rem; line-height: 1.25; margin: 0 0 0.6rem; letter-spacing: -0.01em; }
.tagline { font-size: 1.1rem; color: var(--muted); margin: 0 0 1.4rem; }
.generated { font-size: 0.85rem; color: var(--muted); border-top: 1px solid var(--rule); padding-top: 0.9rem; margin: 0; }
nav.toc {
  position: sticky; top: 0; z-index: 5; background: var(--bg);
  border-bottom: 1px solid var(--rule); margin-bottom: 2.5rem;
}
nav.toc ul { display: flex; gap: 1.4rem; list-style: none; margin: 0; padding: 0.7rem 0; overflow-x: auto; }
nav.toc a { color: var(--muted); text-decoration: none; font-size: 0.86rem; letter-spacing: 0.04em; text-transform: uppercase; white-space: nowrap; }
nav.toc a:hover { color: var(--accent); }
a { color: var(--accent); }
h2 { font-size: 1.55rem; margin: 3.2rem 0 1rem; padding-top: 1.4rem; border-top: 1px solid var(--rule); }
h3 { font-size: 1.2rem; margin: 2.2rem 0 0.7rem; }
h4 { font-size: 1.02rem; margin: 1.6rem 0 0.5rem; }
p { margin: 0 0 1.1rem; }
ul, ol { margin: 0 0 1.1rem; padding-left: 1.4rem; }
li { margin-bottom: 0.4rem; }
li > ul, li > ol { margin: 0.4rem 0 0; }
blockquote { margin: 0 0 1.1rem; padding-left: 1rem; border-left: 3px solid var(--rule); color: var(--muted); }
code { background: var(--code-bg); padding: 0.1em 0.35em; border-radius: 3px; font-size: 0.88em; }
pre { background: var(--code-bg); padding: 0.9rem 1rem; border-radius: 4px; overflow-x: auto; margin: 0 0 1.2rem; }
pre code { background: none; padding: 0; font-size: 0.82rem; line-height: 1.55; }
.scroll { overflow-x: auto; margin: 0 0 1.4rem; }
table { border-collapse: collapse; width: 100%; font-size: 0.92rem; }
th, td { text-align: left; vertical-align: top; padding: 0.5rem 0.7rem; border-bottom: 1px solid var(--rule); }
th { font-weight: 600; }
.chain { display: flex; align-items: stretch; gap: 0.5rem; margin: 0 0 3rem; }
.chain-step {
  flex: 1 1 0; display: flex; flex-direction: column; gap: 0.3rem;
  background: var(--box); border: 1px solid var(--rule); border-radius: 4px; padding: 0.7rem 0.6rem;
}
.chain-name { font-size: 0.78rem; font-weight: 600; letter-spacing: 0.02em; font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace; }
.chain-note { font-size: 0.75rem; line-height: 1.4; color: var(--muted); }
.chain-arrow { align-self: center; color: var(--muted); font-size: 0.9rem; }
@media (max-width: 40rem) {
  .chain { flex-direction: column; }
  .chain-arrow { transform: rotate(90deg); }
  h1 { font-size: 1.7rem; }
}
"""


def build_page(root: Path, date: str) -> str:
    nav = "".join(
        f'<li><a href="#{anchor}">{html.escape(title)}</a></li>'
        for anchor, title, _ in SECTIONS
    )
    sections = "".join(
        _render_section(anchor, title, root / relative)
        for anchor, title, relative in SECTIONS
    )
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Grounded Vault</title>
<meta name="description" content="A provenance-complete knowledge base architecture for humans and AI agents.">
<style>{CSS}</style>
</head>
<body>
<div class="wrap">
<header class="page">
<h1>Grounded Vault</h1>
<p class="tagline">A provenance-complete knowledge base architecture for humans and AI agents.</p>
<p class="generated">This page is generated from the documents of the
<a href="{REPOSITORY_URL}">grounded-vault repository</a> and reflects their state of {html.escape(date)}.</p>
</header>
<nav class="toc" aria-label="Sections"><ul>{nav}</ul></nav>
{_render_chain()}
{sections}</div>
</body>
</html>
"""


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--date", required=True, help="generation date, ISO 8601")
    parser.add_argument(
        "--root",
        type=Path,
        default=Path(__file__).resolve().parent.parent,
        help="vault root (default: the repository this script lives in)",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=None,
        help="target file (default: <root>/docs/index.html)",
    )
    args = parser.parse_args()

    root: Path = args.root.resolve()
    output: Path = args.output or root / "docs" / "index.html"
    try:
        page = build_page(root, args.date)
    except FileNotFoundError as error:
        print(f"FEHLER: {error}", file=sys.stderr)
        return 1
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(page, encoding="utf-8")
    print(f"OK: {output} ({len(page)} bytes, {len(SECTIONS)} sections)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
