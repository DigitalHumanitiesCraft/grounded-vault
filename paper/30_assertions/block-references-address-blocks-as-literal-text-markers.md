---
type: assertion
topics: ["[[Architecture]]"]
status: validated
checked:
  validation: 2026-08-10
  machine-review: 2026-08-10
grounding:
  - "[[20_distillates/publications/obsidian-help-internal-links#^s9]]"
  - "[[20_distillates/publications/obsidian-help-internal-links#^s10]]"
  - "[[20_distillates/publications/obsidian-help-internal-links#^s11]]"
  - "[[20_distillates/publications/obsidian-help-internal-links#^s12]]"
  - "[[20_distillates/publications/obsidian-help-internal-links#^s14]]"
  - "[[20_distillates/publications/obsidian-help-internal-links#^s15]]"
contested-with: []
created: 2026-08-10
updated: 2026-08-10
---

# Block references address blocks as literal text markers

## Statement

A block in Obsidian is a unit of text in a note, such as a paragraph, a block quote or a list item, and a link addresses such a block by appending a hash and a caret to the link destination followed by a unique block identifier. The identifier the link names is written into the file itself as text. For a simple paragraph it stands at the end of the line after a blank space and a caret, and for a structured block, meaning a list, a quotation, a callout or a table, it stands on a separate line with a blank line before and after. A user may write such an identifier by hand as a human-readable one, in the same form. What may stand in it is restricted, since a block identifier may consist only of Latin letters, numbers and dashes.

## Support

- [[20_distillates/publications/obsidian-help-internal-links#^s9]] — defines the block as a unit of text in a note
- [[20_distillates/publications/obsidian-help-internal-links#^s10]] — gives the link form that addresses a block by a unique block identifier
- [[20_distillates/publications/obsidian-help-internal-links#^s11]] — gives the placement of the identifier in a simple paragraph, at the end of the line after a blank space and a caret
- [[20_distillates/publications/obsidian-help-internal-links#^s12]] — gives the placement in a structured block, on a separate line
- [[20_distillates/publications/obsidian-help-internal-links#^s14]] — states that an identifier may be written by hand as a human-readable one
- [[20_distillates/publications/obsidian-help-internal-links#^s15]] — gives the restricted character set, Latin letters, numbers and dashes

## Related

- [[30_assertions/block-references-are-specific-to-obsidian]]
- [[30_assertions/obsidian-link-registers-map-files-to-files]]
