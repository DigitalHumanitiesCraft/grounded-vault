---
type: assertion
topics: ["[[Architecture]]"]
status: validated
checked:
  validation: 2026-08-10
  machine-review: 2026-08-10
grounding:
  - "[[20_distillates/documents/grounded-vault-schema-c726eb5#^s7]]"
  - "[[20_distillates/documents/grounded-vault-schema-c726eb5#^s15]]"
  - "[[20_distillates/documents/grounded-vault-schema-c726eb5#^s16]]"
  - "[[20_distillates/documents/grounded-vault-schema-c726eb5#^s17]]"
  - "[[20_distillates/documents/grounded-vault-schema-c726eb5#^s28]]"
  - "[[20_distillates/documents/grounded-vault-schema-c726eb5#^s29]]"
  - "[[20_distillates/documents/grounded-vault-schema-c726eb5#^s30]]"
  - "[[20_distillates/documents/grounded-vault-operations-c726eb5#^s15]]"
contested-with: []
created: 2026-08-10
updated: 2026-08-10
---

# The profile knows three source types, document, publication and data, and the storability of a source decides which of them applies and which anchor form it permits

## Statement

The controlled vocabulary of the source type holds document, publication and data. Which of the three applies follows from whether the content of a source may be stored in the vault and from the anchor that this storage decision permits. A document is a source whose full text may be stored, and it is anchored by block reference into its Markdown representation, which is also the anchor form its distillate statements take. A publication is a source that is only cited, so what lies in the vault is the bibliographic record and the anchor is the verbatim quotation together with the identifier, the quotation having to appear character for character in the source and its intake check being recorded as `checked.quote`. A publication source receives no Markdown representation, because its CSL JSON record is the root of this source type. A data source is a file whose anchor is a deterministic computation over that file, named on an indented line and run from a script in the analysis folder of the tools, because an aggregate or a statistical finding exists at no single passage. The criterion is storability, and the publication status of a source decides nothing by itself, so an open-access article that may be stored is treated as a document, and wherever a full text may be stored the type document is preferred over publication, since its anchors resolve inside the vault.

## Support

- [[20_distillates/documents/grounded-vault-schema-c726eb5#^s7]] — gives the controlled vocabulary of the source-type field
- [[20_distillates/documents/grounded-vault-schema-c726eb5#^s15]] — ties the source type to storability and to the anchor that the storage decision permits
- [[20_distillates/documents/grounded-vault-schema-c726eb5#^s16]] — defines the three types with the anchor each one carries and the reason for the computation anchor
- [[20_distillates/documents/grounded-vault-schema-c726eb5#^s17]] — states storability as the criterion over publication status and the preference for document
- [[20_distillates/documents/grounded-vault-schema-c726eb5#^s28]] — gives the block reference as the statement anchor of the document type
- [[20_distillates/documents/grounded-vault-schema-c726eb5#^s29]] — gives the verbatim quotation with citation as the statement anchor of the publication type and its recorded check
- [[20_distillates/documents/grounded-vault-schema-c726eb5#^s30]] — gives the reproducible computation as the statement anchor of the data type and where its script lives
- [[20_distillates/documents/grounded-vault-operations-c726eb5#^s15]] — states that a publication source receives no Markdown representation because the bibliographic record is its root

## Related

- [[30_assertions/layer-model-assigns-each-layer-its-anchor-form]]
- [[30_assertions/markdown-representation-is-immutable-after-ingest]]
