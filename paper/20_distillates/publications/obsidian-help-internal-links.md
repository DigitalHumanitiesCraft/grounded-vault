---
type: distillate
source-type: publication
reference: "obsidianhelplinks"
topics: ["[[Architecture]]", "[[Provenance]]"]
status: validated
checked:
  quote: 2026-08-10
  validation: 2026-08-10
  machine-review: 2026-08-10
created: 2026-08-10
updated: 2026-08-10
---

# Distillate: Obsidian Help, Internal links

The Obsidian help page on internal links sets out the link formats, the character restrictions on link targets and identifiers, and the syntax by which a link addresses a heading or a single block inside a note.

## Core statements

- Obsidian can automatically update the internal links of a vault when a file is renamed. ^s1
  > "Obsidian can automatically update internal links in your vault when you rename a file." (obsidianhelplinks, Internal links, § lead)
- Obsidian supports two link formats for internal links, the wikilink and the Markdown link. ^s2
  > "Obsidian supports the following link formats:
  > - Wikilink: `\[\[Three laws of motion\]\]` or `\[\[Three laws of motion.md\]\]`
  > - Markdown: `[Three laws of motion](Three%20laws%20of%20motion)` or `[Three laws of motion](Three%20laws%20of%20motion.md)`" (obsidianhelplinks, Internal links, § Supported formats for internal links; the square brackets of the wikilink examples are backslash-escaped here, because a literal wikilink in a vault document is read by the validator as an anchor of this vault)
- The two link forms appear the same way in the editor and link to the same note. ^s20
  > "The examples above are equivalent, and they appear the same way in the editor and links to the same note." (obsidianhelplinks, Internal links, § Supported formats for internal links)
- A link into a folder carries the folder path before the note name, and folder paths start at the vault root and use forward slashes even on Windows. ^s3
  > "To link to a note in a folder, include the folder path before the note name. Folder paths start at the vault root and use forward slashes (`/`), even on Windows" (obsidianhelplinks, Internal links, § Supported formats for internal links)
- Obsidian generates links in the wikilink format by default because that format is more compact, and the Markdown format can be selected instead where interoperability matters. ^s4
  > "By default, due to its more compact format, Obsidian generates links using the Wikilink format. If interoperability is important to you, you can disable Wikilinks and use Markdown links instead." (obsidianhelplinks, Internal links, § Supported formats for internal links)
- A string containing any of the characters `#`, `|`, `^`, `:`, `%%`, `[[` or `]]` may fail to work as a link. ^s5
  > "A string which contains the following characters may not work as a link: `# | ^ : %% [[ ]]`." (obsidianhelplinks, Internal links, § Supported formats for internal links, callout "Invalid characters")
- A link to a file of a format other than Markdown must include the file extension. ^s6
  > "While you can link to any of the [[Accepted file formats]], links to file formats other than Markdown needs to include a file extension, such as `[[Figure 1.png]]`." (obsidianhelplinks, Internal links, § Link to a file)
- Prefixing an internal link with an exclamation mark embeds the linked content instead of linking to it. ^s7
  > "Prefixing an internal link with an exclamation mark (!) allows you to embed the linked content." (obsidianhelplinks, Internal links, § Link to a file, callout)
- A link to a heading in another note is written by appending a hash to the link destination followed by the heading text. ^s8
  > "To link to a heading in another note, add a hash (`#`) at the end of the link destination, followed by the heading text." (obsidianhelplinks, Internal links, § Link to a heading in a note)
- Multiple hash symbols can be added for each subheading. ^s19
  > "You can add multiple hash symbols for each subheading." (obsidianhelplinks, Internal links, § Link to a heading in a note)
- A block is a unit of text in a note, such as a paragraph, a block quote or a list item. ^s9
  > "A block is a unit of text in your note, such as a paragraph, block quote, or list item." (obsidianhelplinks, Internal links, § Link to a block in a note)
- A link to a block is written by appending `#^` to the link destination followed by a unique block identifier. ^s10
  > "You can link to a block by adding `#^` at the end of your link destination, followed by a unique block identifier." (obsidianhelplinks, Internal links, § Link to a block in a note)
- For a simple paragraph the block identifier stands at the end of the line, preceded by a blank space and a caret. ^s11
  > "For *simple paragraphs*, place a blank space followed by a caret `^` and the block identifier at the end of the line:" (obsidianhelplinks, Internal links, § Link to a block in a note)
- For a structured block, meaning a list, quotation, callout or table, the block identifier stands on a separate line with a blank line before and after it. ^s12
  > "For *structured blocks* (lists, quotations, callouts, tables), the block identifier should be on a separate line, with a blank line before and after:" (obsidianhelplinks, Internal links, § Link to a block in a note)
- Obsidian does not support links to specific parts of quotations, callouts and tables. ^s13
  > "We do not support links to specific parts of quotations, callouts, and tables." (obsidianhelplinks, Internal links, § Link to a block in a note, callout)
- A block identifier may be written by hand as a human-readable identifier, again as a blank space followed by a caret and the identifier. ^s14
  > "You can also create human-readable block identifiers by adding a blank space followed by a caret (`^`) and the identifier." (obsidianhelplinks, Internal links, § Link to a block in a note)
- A block identifier may consist only of Latin letters, numbers and dashes. ^s15
  > "Block identifiers can only consist of Latin letters, numbers, and dashes." (obsidianhelplinks, Internal links, § Link to a block in a note)
- Block references are specific to Obsidian and are not part of the standard Markdown format, so links containing them do not work outside Obsidian. ^s16
  > "Block references are specific to Obsidian and not part of the standard Markdown format. Links containing block references won't work outside of Obsidian." (obsidianhelplinks, Internal links, § Link to a block in a note, callout "Interoperability")
- In the wikilink format a vertical bar changes the display text of a link. ^s17
  > "Use a vertical bar (`|`) to change the display text." (obsidianhelplinks, Internal links, § Change the link display text)
- Custom link display text is meant for customizing how a link looks in a specific place. ^s18
  > "Use [[#Change the link display text|link display text]] when you want to customize how a link looks *in a specific place*." (obsidianhelplinks, Internal links, § Change the link display text, callout "Tip")

## Terms

- **block**: a unit of text in a note, such as a paragraph, block quote or list item
  > "A block is a unit of text in your note, such as a paragraph, block quote, or list item." (obsidianhelplinks, Internal links, § Link to a block in a note)
- **block identifier**: the unique string appended to a block after a caret, restricted to Latin letters, numbers and dashes, by which a link addresses that block
  > "Block identifiers can only consist of Latin letters, numbers, and dashes." (obsidianhelplinks, Internal links, § Link to a block in a note)
- **anchor link**: the page's own name for a link to a specific heading in a note
  > "You can link to specific headings in notes, also known as _anchor links_." (obsidianhelplinks, Internal links, § Link to a heading in a note)

## Open questions

- The page states that a block identifier must be unique, without saying over which scope, the file or the vault, uniqueness is required or what happens when it is violated.
- The page restricts block identifiers to Latin letters, numbers and dashes, without saying whether an identifier outside that set is rejected, silently ignored, or merely unsupported.
- The page states that Obsidian can update internal links on rename, without saying whether a block reference survives an edit that moves or rewrites the block it points to.

## Appraisal

The page is the operator's user documentation and therefore the authoritative statement of the syntax, while it is silent on the resolution behaviour behind that syntax, which the developer documentation covers separately. Its value for this vault lies in two constraints that decide how an anchor may be minted at all, the restricted character set of a block identifier and the vendor's own statement that a block reference leaves the standard Markdown format. Its limit is that it describes authoring, so it says what a user types and not what the application does with a reference whose target has disappeared.

## Related

- [[20_distillates/publications/obsidian-help-obsidian-flavored-markdown]]
- [[20_distillates/publications/obsidian-docs-metadatacache]]
- [[30_assertions/MOC-Architecture]]
