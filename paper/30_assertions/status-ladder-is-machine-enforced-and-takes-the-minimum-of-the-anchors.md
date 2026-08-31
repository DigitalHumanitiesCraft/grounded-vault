---
type: assertion
topics: ["[[Architecture]]"]
status: validated
checked:
  validation: 2026-08-10
  machine-review: 2026-08-10
grounding:
  - "[[20_distillates/documents/grounded-vault-schema-c726eb5#^s9]]"
  - "[[20_distillates/documents/grounded-vault-schema-c726eb5#^s11]]"
  - "[[20_distillates/documents/grounded-vault-schema-c726eb5#^s12]]"
  - "[[20_distillates/documents/grounded-vault-operations-c726eb5#^s45]]"
  - "[[20_distillates/documents/grounded-vault-operations-c726eb5#^s48]]"
  - "[[20_distillates/documents/grounded-vault-operations-c726eb5#^s54]]"
  - "[[20_distillates/documents/grounded-vault-operations-c726eb5#^s57]]"
contested-with: []
created: 2026-08-10
updated: 2026-08-10
---

# The status of a document runs on a machine-enforced ladder from grounded through validated to verified and never rises above the minimum of the states of its anchors

## Statement

A status records the outcome of checks that actually ran, and every check writes its date into the `checked` map of the document it checked. The controlled vocabulary holds grounded, validated and verified, plus contested for assertions and superseded for distillates. Grounded is the entry status of every freshly produced document and requires no entry. Validated is reached when validation and machine review have passed and requires both dates to be recorded, and those two checks together lift a document that far and never higher. Verified additionally requires a recorded verification, which alone lifts a document to that step and which the machine checks prepare without ever replacing it, and the ladder reaches verified when the expert has passed. Every entry of the map carries an ISO date, because a record without one cannot be held against the content it judges. The status of a document is the minimum of the states of its anchors, so one unreviewed anchor keeps the whole document at grounded, and a document resting on a contested or superseded anchor stays at grounded as well, since those two states lie beside the ladder. The discipline is enforced by machine, and the validation checks carry codes for a status lacking a required check, for a check recorded without a date, and for a document standing higher on the ladder than an anchor it rests on.

## Support

- [[20_distillates/documents/grounded-vault-schema-c726eb5#^s9]] — gives the controlled vocabulary of the status field with the two states restricted by document type
- [[20_distillates/documents/grounded-vault-schema-c726eb5#^s11]] — ties a status to checks that actually ran and to the dated entry in the checked map
- [[20_distillates/documents/grounded-vault-schema-c726eb5#^s12]] — states the machine enforcement, the required entries per rank, the ISO date requirement, the minimum rule and the position of contested and superseded beside the ladder
- [[20_distillates/documents/grounded-vault-operations-c726eb5#^s45]] — names the validation codes for a missing check, an undated check and a document above the rank of its anchor
- [[20_distillates/documents/grounded-vault-operations-c726eb5#^s48]] — bounds machine review together with validation at validated
- [[20_distillates/documents/grounded-vault-operations-c726eb5#^s54]] — reserves the lift to verified for human verification
- [[20_distillates/documents/grounded-vault-operations-c726eb5#^s57]] — gives the ladder with the condition of each rung and repeats the minimum rule

## Related

- [[30_assertions/layer-model-assigns-each-layer-its-anchor-form]]
- [[30_assertions/anchors-are-minted-at-their-own-layer-and-bind-one-layer-down]]
