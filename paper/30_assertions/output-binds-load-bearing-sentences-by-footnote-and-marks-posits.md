---
type: assertion
topics: ["[[Architecture]]"]
status: validated
checked:
  validation: 2026-08-10
  machine-review: 2026-08-10
grounding:
  - "[[20_distillates/documents/grounded-vault-schema-c726eb5#^s4]]"
  - "[[20_distillates/documents/grounded-vault-schema-c726eb5#^s34]]"
  - "[[20_distillates/documents/grounded-vault-schema-c726eb5#^s40]]"
  - "[[20_distillates/documents/grounded-vault-schema-c726eb5#^s41]]"
  - "[[20_distillates/documents/grounded-vault-operations-c726eb5#^s31]]"
  - "[[20_distillates/documents/grounded-vault-operations-c726eb5#^s35]]"
contested-with: []
created: 2026-08-10
updated: 2026-08-10
---

# The output layer carries an anchor contract under which every load-bearing sentence footnotes an assertion and every own conclusion is marked as a posit

## Statement

A chapter is an output text in which every load-bearing sentence carries a footnote to an assertion and every own conclusion is marked as a posit. The contract sets two requirements, a footnote marker on every load-bearing sentence and a footnote that begins with one of two keywords, and nothing else counts. The one keyword names the assertion the sentence is grounded in, and the other opens a posit footnote that states its rationale and its open evidence question. The referenced assertions and the count of posit footnotes are mirrored in the frontmatter, and validation cross-checks the footnotes against that mirror and that count. The posit keyword is the place where a conclusion without source support enters the vault, since such a conclusion never becomes an assertion and is instead noted at the assertion layer as a posit candidate for the output. Footnotes are the reference notation of the profile, which an instantiation may substitute as long as marker, keyword and mirror survive.

## Support

- [[20_distillates/documents/grounded-vault-schema-c726eb5#^s4]] — defines the chapter as an output text with a footnote to an assertion on every load-bearing sentence and every own conclusion marked as a posit
- [[20_distillates/documents/grounded-vault-schema-c726eb5#^s34]] — states that a conclusion without source support enters the output as a posit and never becomes an assertion
- [[20_distillates/documents/grounded-vault-schema-c726eb5#^s40]] — gives the anchor contract, the marker on every load-bearing sentence and the two keywords
- [[20_distillates/documents/grounded-vault-schema-c726eb5#^s41]] — gives the cross-check against the mirror and the posit count and the substitutability of the notation
- [[20_distillates/documents/grounded-vault-operations-c726eb5#^s31]] — names the posit candidate that no distillate statement carries and keeps it out of the assertion layer
- [[20_distillates/documents/grounded-vault-operations-c726eb5#^s35]] — gives the two footnote forms and the mirroring of assertions and posit count in the frontmatter

## Related

- [[30_assertions/layer-model-assigns-each-layer-its-anchor-form]]
- [[30_assertions/status-ladder-is-machine-enforced-and-takes-the-minimum-of-the-anchors]]
