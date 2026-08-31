---
type: assertion
topics: ["[[Verification]]"]
status: validated
checked:
  validation: 2026-08-10
  machine-review: 2026-08-10
grounding:
  - "[[20_distillates/documents/generalization-bias-llm-summarization-2025#^s2]]"
  - "[[20_distillates/documents/generalization-bias-llm-summarization-2025#^s3]]"
  - "[[20_distillates/documents/generalization-bias-llm-summarization-2025#^s5]]"
contested-with: []
created: 2026-08-10
updated: 2026-08-10
---

# LLM summaries broaden the scope of findings

## Statement

Model written summaries of scientific texts state conclusions in a wider scope than the originals do. Across all models combined the summaries were twice as likely to contain generalized conclusions as the original abstracts, in a regression controlling for temperature, prompt and test condition, and most tested models produced broader generalizations even when explicitly prompted for accuracy, with DeepSeek, ChatGPT-4o and LLaMA 3.3 70B overgeneralizing in 26 to 73% of cases. The prompt asking for accuracy roughly doubled the likelihood of a generalized conclusion against the simple prompt, with an odds ratio of 1.90.

## Support

- [[20_distillates/documents/generalization-bias-llm-summarization-2025#^s2]] — establishes that most tested models generalize beyond the original text under an accuracy prompt and supplies the 26 to 73% range for three of them.
- [[20_distillates/documents/generalization-bias-llm-summarization-2025#^s3]] — supplies the aggregate effect, twice the likelihood of a generalized conclusion against the original abstracts, under the stated controls.
- [[20_distillates/documents/generalization-bias-llm-summarization-2025#^s5]] — supplies the counterintuitive prompt effect, the accuracy instruction roughly doubling the rate at an odds ratio of 1.90.

## Related

- [[30_assertions/source-binding-lowers-unsupported-citation-without-eliminating-it]]
