---
type: assertion
topics: ["[[Agentic Workflow]]"]
status: grounded
checked:
  validation: 2026-09-27
grounding:
  - "[[20_distillates/documents/grounded-vault-operations-c726eb5#^s47]]"
  - "[[20_distillates/documents/grounded-vault-operations-c726eb5#^s49]]"
  - "[[20_distillates/documents/grounded-vault-operations-c726eb5#^s52]]"
contested-with: []
created: 2026-09-27
updated: 2026-09-27
---

# At commit c726eb5 of 2026-08-10, Grounded Vault machine review judges a bare statement against its anchored location while the producing agent's reasoning stays hidden

## Statement

In the operations document of the Grounded Vault profile at commit c726eb5 of 2026-08-10, machine review judges per pair whether a source location actually supports the statement built on it, with the fixed verdict vocabulary fully supports, partially supports, overreaches, contradicts and not in the text, of which only fully supports passes. A pair consists of the anchored location, which is the block with its heading path for a document, the quotation for a publication and the computation with its result for data, together with the bare statement, and nothing else enters the pair. Anti-anchoring is mandatory, so the reviewer sees only the source location and the statement while the producing agent's reasoning stays hidden, and a reviewer from a different model family than the producer is recommended because it decorrelates error modes.

## Support

- [[20_distillates/documents/grounded-vault-operations-c726eb5#^s47]], supplies the object of the review, the support of a statement by its source location per pair, and the fixed verdict vocabulary
- [[20_distillates/documents/grounded-vault-operations-c726eb5#^s49]], makes anti-anchoring mandatory and recommends a reviewer from a different model family
- [[20_distillates/documents/grounded-vault-operations-c726eb5#^s52]], fixes what enters a pair, the anchored location in the form of its source type and the bare statement

## Related

- [[30_assertions/status-ladder-is-machine-enforced-and-takes-the-minimum-of-the-anchors]]
- [[30_assertions/llm-evaluators-favor-their-own-generations]]
- [[30_assertions/cross-family-evaluator-panels-reduce-intra-model-bias]]
