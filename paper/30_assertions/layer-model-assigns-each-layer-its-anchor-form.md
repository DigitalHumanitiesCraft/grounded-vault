---
type: assertion
topics: ["[[Architecture]]"]
status: validated
checked:
  validation: 2026-08-10
  machine-review: 2026-08-10
grounding:
  - "[[20_distillates/documents/grounded-vault-schema-c726eb5#^s2]]"
  - "[[20_distillates/documents/grounded-vault-schema-c726eb5#^s4]]"
  - "[[20_distillates/documents/grounded-vault-schema-c726eb5#^s33]]"
  - "[[20_distillates/documents/grounded-vault-operations-c726eb5#^s25]]"
contested-with: []
created: 2026-08-10
updated: 2026-08-10
---

# The architecture runs over five layers, and each layer carries its own anchor form

## Statement

The Grounded Vault profile arranges its material in five layers, and each layer carries the anchor form the schema assigns to it. Sources are the ground and carry no anchor, since the original file is kept exactly as it arrived so that every later form of its content can be checked against it. The Markdown representation holds archived full texts and datasets with schema, and it carries block IDs together with the file plus schema pairing, the block IDs being stamped once so that later layers anchor into passages that never change afterwards. Distillates hold the single statements extracted from one source, each carrying a grounding anchor into that source, and they mint statement IDs. Assertions carry grounding anchors into distillate statements, and each assertion is a single source-supported statement synthesized from the distillates of a topic and grounded in at least one such statement. The output carries footnote anchors into assertions with posits marked, and its chapter type requires a footnote to an assertion on every load-bearing sentence. The assertion layer is the point where the source types converge and where the vault synthesizes, one file per assertion.

## Support

- [[20_distillates/documents/grounded-vault-schema-c726eb5#^s2]] — gives the five layers with the content and the anchor each one carries
- [[20_distillates/documents/grounded-vault-schema-c726eb5#^s4]] — defines source, Markdown representation, distillate, assertion and chapter and states why each form is held that way
- [[20_distillates/documents/grounded-vault-schema-c726eb5#^s33]] — names the assertion layer as the place where the source types converge, one file per assertion
- [[20_distillates/documents/grounded-vault-operations-c726eb5#^s25]] — names assertions as the layer where the vault synthesizes and the work proceeds by topic

## Related

- [[30_assertions/anchors-are-minted-at-their-own-layer-and-bind-one-layer-down]]
- [[30_assertions/source-type-follows-storability-and-fixes-the-anchor-form]]
- [[30_assertions/output-binds-load-bearing-sentences-by-footnote-and-marks-posits]]
