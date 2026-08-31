---
type: assertion
topics: ["[[Architecture]]"]
status: validated
checked:
  validation: 2026-08-10
  machine-review: 2026-08-10
grounding:
  - "[[20_distillates/documents/grounded-vault-operations-c726eb5#^s7]]"
  - "[[20_distillates/documents/grounded-vault-schema-c726eb5#^s21]]"
  - "[[20_distillates/documents/grounded-vault-schema-c726eb5#^s44]]"
contested-with: []
created: 2026-08-10
updated: 2026-08-10
---

# A converted Markdown representation is never edited again after ingest, and for the source type document a revised source enters as a new file with a date-suffixed slug

## Statement

Ingest converts an original in two steps, a structure-preserving conversion in which headings, lists, tables and paragraph boundaries survive as the original had them, and the stamping of a block ID onto every anchor-relevant paragraph. After that the converted file is never edited again, because every later layer anchors into these blocks and an edit would move them. For the source type document the schema adds the version rule, one Markdown representation per source and a new file with a date-suffixed slug for a revised source, so that existing anchors keep resolving against the old file. Date suffixes are the general naming device by which version rows of a speaking slug are distinguished.

## Support

- [[20_distillates/documents/grounded-vault-operations-c726eb5#^s7]] — gives the two ingest steps and the rule that the file is never edited afterwards, with the reason that an edit would move the blocks
- [[20_distillates/documents/grounded-vault-schema-c726eb5#^s21]] — gives, for the source type document, the one representation per source and the date-suffixed new file for a revised source
- [[20_distillates/documents/grounded-vault-schema-c726eb5#^s44]] — states that date suffixes distinguish version rows in the naming scheme

## Related

- [[30_assertions/anchors-are-minted-at-their-own-layer-and-bind-one-layer-down]]
- [[30_assertions/source-type-follows-storability-and-fixes-the-anchor-form]]
