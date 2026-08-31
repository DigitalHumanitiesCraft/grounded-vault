---
type: assertion
topics: ["[[Verification]]"]
status: validated
checked:
  validation: 2026-08-10
  machine-review: 2026-08-10
grounding:
  - "[[20_distillates/documents/llm-evaluators-self-preference-2024#^s4]]"
  - "[[20_distillates/documents/llm-evaluators-self-preference-2024#^s1]]"
  - "[[20_distillates/documents/llm-evaluators-self-preference-2024#^s7]]"
contested-with: []
created: 2026-08-10
updated: 2026-08-10
---

# LLM evaluators favor their own generations

## Statement

On two summarization tasks GPT-3.5 Turbo, GPT-4 and Llama 2 disproportionately favour summaries written by themselves over summaries written by other models and by humans. The strength of that preference moves with the model's ability to recognize its own text. Fine-tuning for self-recognition produces a strong linear correlation between self-recognition ability and self-preference in the pairwise setting, and the effect transfers across the two datasets. The measured relation is a correlation.

## Support

- [[20_distillates/documents/llm-evaluators-self-preference-2024#^s4]] — establishes the preference itself for three models on two summarization tasks, against other models and against humans.
- [[20_distillates/documents/llm-evaluators-self-preference-2024#^s1]] — establishes that the models distinguish their own outputs with non-trivial accuracy and that fine-tuning reveals a linear correlation between recognition and preference.
- [[20_distillates/documents/llm-evaluators-self-preference-2024#^s7]] — supplies the pairwise result with the transfer of the fine-tuning effect between datasets.

## Related

- [[30_assertions/cross-family-evaluator-panels-reduce-intra-model-bias]]
