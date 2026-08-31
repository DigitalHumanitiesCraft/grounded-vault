---
type: distillate
source-type: publication
reference: "obsidianhelpofm"
topics: ["[[Architecture]]"]
status: validated
checked:
  quote: 2026-08-10
  validation: 2026-08-10
  machine-review: 2026-08-10
created: 2026-08-10
updated: 2026-08-10
---

# Distillate: Obsidian Help, Obsidian Flavored Markdown

The Obsidian help page on Obsidian Flavored Markdown names the standards Obsidian supports and lists, in a table of supported Markdown extensions, the syntax that goes beyond them, block definition and block reference among it.

## Core statements

- Obsidian aims at maximum capability without breaking existing formats and therefore uses a combination of Markdown flavors. ^s1
  > "Obsidian strives for maximum capability without breaking any existing formats. As a result, we use a combination of flavors of [[Basic formatting syntax|Markdown]]." (obsidianhelpofm, Obsidian Flavored Markdown, § lead)
- Obsidian supports CommonMark, GitHub Flavored Markdown and LaTeX. ^s2
  > "Obsidian supports [CommonMark](https://commonmark.org/), [GitHub Flavored Markdown](https://github.github.com/gfm/), and [LaTeX](https://www.latex-project.org/)." (obsidianhelpofm, Obsidian Flavored Markdown, § lead)
- The page lists the syntax `^id` as defining a block, in its table of supported Markdown extensions. ^s3
  > "| `^id`           | [[Internal links#Link to a block in a note\|Defining a block]]        |" (obsidianhelpofm, Obsidian Flavored Markdown, § Supported Markdown extensions)
- The same table lists the wikilink `[[Link]]` as an internal link. ^s4
  > "| `[[Link]]`      | [[Internal links]]                                                    |" (obsidianhelpofm, Obsidian Flavored Markdown, § Supported Markdown extensions)
- The same table carries a row for block references whose description cell points to the internal links page, section on linking to a block. ^s5
  > "[[Internal links#Link to a block in a note\|Block references]]" (obsidianhelpofm, Obsidian Flavored Markdown, § Supported Markdown extensions, description cell of the block-reference row; its syntax cell is not reproduced here, see Open questions)
- The same table lists the highlight syntax `==Text==` among the supported Markdown extensions. ^s6
  > "| `==Text==`      | [[Basic formatting syntax#Bold, italics, highlights\|Highlights]]     |" (obsidianhelpofm, Obsidian Flavored Markdown, § Supported Markdown extensions)
- Obsidian does not render Markdown syntax inside HTML elements, as an intentional design choice for performance and for keeping parser complexity low in large documents. ^s7
  > "Obsidian does not render Markdown syntax inside HTML elements. This is an intentional design choice for performance optimization and to keep parser complexity low when managing large documents." (obsidianhelpofm, Obsidian Flavored Markdown, § lead, callout "Markdown inside HTML")
- Markdown formatting is not processed inside HTML tags such as `<div>`, `<span>` or `<table>`. ^s8
  > "For example, Markdown formatting like `**bold**` or `` `code` `` will not be processed inside `<div>`, `<span>`, `<table>`, or any other HTML tags." (obsidianhelpofm, Obsidian Flavored Markdown, § lead, callout "Markdown inside HTML")

## Terms

- **Obsidian Flavored Markdown**: the combination of Markdown flavors Obsidian uses, comprising the supported standards and the extensions the page's table enumerates
  > "Obsidian strives for maximum capability without breaking any existing formats. As a result, we use a combination of flavors of [[Basic formatting syntax|Markdown]]." (obsidianhelpofm, Obsidian Flavored Markdown, § lead)

## Open questions

- The page places block definition and block reference in a table headed "Supported Markdown extensions" without stating in its prose which of the listed rows lie outside CommonMark and GitHub Flavored Markdown, so the extension status of an individual row has to be read off the table heading.
- The syntax cell of the block-reference row gives the embedding form, an exclamation mark before a wikilink whose subpath is a caret identifier, and the table does not list the plain linking form without the exclamation mark, although the internal links page describes that plain form as the way to link to a block. The cell is not reproduced verbatim in this distillate, because a literal block-reference wikilink in a vault document is read by the validator as an anchor of this vault and would resolve nowhere.
- The page names LaTeX beside CommonMark and GitHub Flavored Markdown without saying which subset of it is supported or by which renderer.

## Appraisal

The page is the operator's own map of where its dialect sits relative to the standards it claims to support, and that map is a table rather than a specification, so it fixes the inventory of extensions and not their semantics. Its value for this vault is that the vendor itself files block definition and block reference under extensions, which is the point at which a vault anchor stops being portable Markdown. Its limit is the missing distinction inside the table, since it lists rows that CommonMark or GitHub Flavored Markdown already cover next to genuinely Obsidian-specific ones without marking which is which.

## Related

- [[20_distillates/publications/obsidian-help-internal-links]]
- [[30_assertions/MOC-Architecture]]
