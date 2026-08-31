---
type: assertion
topics: ["[[Architecture]]"]
status: validated
checked:
  validation: 2026-08-10
  machine-review: 2026-08-10
grounding:
  - "[[20_distillates/documents/grounded-vault-schema-c726eb5#^s5]]"
  - "[[20_distillates/documents/grounded-vault-schema-c726eb5#^s23]]"
  - "[[20_distillates/documents/grounded-vault-schema-c726eb5#^s27]]"
  - "[[20_distillates/documents/grounded-vault-operations-c726eb5#^s45]]"
contested-with: []
created: 2026-08-10
updated: 2026-08-10
---

# Two rules constrain the chain, that anchors are minted only at the layer they belong to and that each layer references only the layer directly beneath it

## Statement

The schema states two rules over the layer chain. The first fixes where an anchor comes into existence, so a Markdown representation mints block IDs and a distillate mints statement IDs, and no higher layer creates anchors into material below its direct predecessor. Block IDs are short, stable and unique per file, and they are minted in the Markdown representation alone. Every core statement of a distillate ends with a statement ID, and that ID is the anchor assertions bind to. The second rule fixes what an anchor may point at, so each layer references only the layer directly beneath it. The validation checks of the profile carry their own codes, among them one for layer skipping, so a reference that jumps a layer is a defect the checking instance names.

## Support

- [[20_distillates/documents/grounded-vault-schema-c726eb5#^s5]] — states both rules, the minting at the own layer and the reference to the layer directly beneath
- [[20_distillates/documents/grounded-vault-schema-c726eb5#^s23]] — restricts the minting of block IDs to the Markdown representation and gives their properties
- [[20_distillates/documents/grounded-vault-schema-c726eb5#^s27]] — gives the statement ID as the anchor assertions bind to, one grounding anchor per core statement
- [[20_distillates/documents/grounded-vault-operations-c726eb5#^s45]] — names layer skipping among the coded validation checks

## Related

- [[30_assertions/layer-model-assigns-each-layer-its-anchor-form]]
- [[30_assertions/markdown-representation-is-immutable-after-ingest]]
