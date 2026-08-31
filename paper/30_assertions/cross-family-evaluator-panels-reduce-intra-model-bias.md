---
type: assertion
topics: ["[[Verification]]"]
status: validated
checked:
  validation: 2026-08-10
  machine-review: 2026-08-10
grounding:
  - "[[20_distillates/publications/llm-jury-panel-evaluation-2024#^s1]]"
  - "[[20_distillates/publications/llm-jury-panel-evaluation-2024#^s3]]"
  - "[[20_distillates/publications/llm-jury-panel-evaluation-2024#^s4]]"
contested-with: []
created: 2026-08-10
updated: 2026-08-10
---

# Cross-family evaluator panels reduce intra-model bias

## Statement

A panel of several smaller evaluator models, composed of members drawn from disjoint model families, exhibits less intra-model bias than a single large judge, and it outperforms that judge across three judge settings and six datasets. The mechanism claimed for the reduction is the pooling of judgments across heterogeneous evaluator models. The panel used in the reported experiments consists of three models from three different families.

## Support

- [[20_distillates/publications/llm-jury-panel-evaluation-2024#^s1]] — establishes that the panel shows less intra-model bias than a single large judge and attributes that to its composition from disjoint model families.
- [[20_distillates/publications/llm-jury-panel-evaluation-2024#^s3]] — names the pooling of judgments across heterogeneous evaluator models as what reduces intra-model scoring bias.
- [[20_distillates/publications/llm-jury-panel-evaluation-2024#^s4]] — fixes the panel composition the result was measured on, three models from three disparate families.

## Related

- [[30_assertions/llm-evaluators-favor-their-own-generations]]
