---
type: distillate
source-type: document
representation: "[[10_markdown/documents/generalization-bias-llm-summarization-2025]]"
topics: ["[[Verification]]", "[[Provenance]]"]
status: validated
checked:
  validation: 2026-08-10
  machine-review: 2026-08-10
created: 2026-08-10
updated: 2026-08-10
---

# Distillate: Generalization bias in large language model summarization of scientific research

The source measures how far model-written summaries widen the scope of a study's conclusions beyond the source text, and it supplies the vault with a quantified failure mode that does not involve any invented reference.

## Core statements

- Over all conditions of prompt, temperature and retest, a total of 4900 model summaries were tested, 4300 summaries of abstracts and 600 of articles, and this total was pre-specified to keep data labelling tractable. [[10_markdown/documents/generalization-bias-llm-summarization-2025#^pc20]] ^s1
- Even when explicitly prompted for accuracy, most of the tested models produced broader generalizations of scientific results than the original texts, with DeepSeek, ChatGPT-4o and LLaMA 3.3 70B overgeneralizing in 26–73% of cases. [[10_markdown/documents/generalization-bias-llm-summarization-2025#^pc01]] ^s2
- Across all models combined, summaries were twice as likely to contain generalized conclusions as the original abstracts, in a regression controlling for temperature, prompt and test condition. [[10_markdown/documents/generalization-bias-llm-summarization-2025#^pc24]] ^s3
- The summaries of 6 of the 10 models were significantly more likely to contain generalized conclusions than the original texts, with about 2.6 times the likelihood for GPT-4 Turbo and LLaMA 2 70B, 9 times for ChatGPT-4o and 39 times for LLaMA 3.3 70B, while GPT-3.5 Turbo and the Claude versions did not differ significantly from the abstracts. [[10_markdown/documents/generalization-bias-llm-summarization-2025#^pc27]] ^s4
- The prompt asking for systematic step-by-step processing did not significantly change the likelihood of generalized conclusions, and the prompt asking for accuracy roughly doubled it against the simple prompt (OR = 1.90, 95% CI [1.11, 3.26], p = 0.02). [[10_markdown/documents/generalization-bias-llm-summarization-2025#^pc35]] ^s5
- At temperature 0, summaries containing generalized conclusions were 76% less likely to occur than at temperature 0.7. [[10_markdown/documents/generalization-bias-llm-summarization-2025#^pc28]] ^s6
- Human-authored NEJM Journal Watch summaries did not differ significantly from the original articles in their likelihood of containing generalized conclusions, while the article summaries of GPT-4 Turbo, ChatGPT-4o and DeepSeek were almost five times as likely to contain them as those human summaries (OR = 4.85, 95% CI [3.06, 7.70], p < 0.001). [[10_markdown/documents/generalization-bias-llm-summarization-2025#^pc37]] ^s7
- The material comprised 200 abstracts, 100 from the top four general medical journals and 100 from the top four multidisciplinary science journals, and a further 100 full-length articles from the four medical journals for the article summarization test, for which the corresponding NEJM Journal Watch summaries were collected as well. [[10_markdown/documents/generalization-bias-llm-summarization-2025#^pc39]] ^s8
- Two experts coded every text as containing restricted or generalized conclusions under preregistered criteria, a third researcher blinded to the summary source coded 100 texts by the same criteria, inter-rater agreement ranged from k = 0.79 to k = 0.95, and disagreements were resolved by discussion. [[10_markdown/documents/generalization-bias-llm-summarization-2025#^pc41]] ^s9
- The study did not assess whether the generalizations in the human-authored texts were warranted but used them as a baseline for comparison, took the faithful representation of the original text as the normative standard, and defined overgeneralizations as cases where a model broadened conclusions beyond those in the original scientific text. [[10_markdown/documents/generalization-bias-llm-summarization-2025#^pc17]] ^s10

## Terms

- **Overgeneralization**: a generalization in a summary that is broader than the one in the original text and therefore possibly unwarranted by the original findings. [[10_markdown/documents/generalization-bias-llm-summarization-2025#^pc04]]
- **Generic generalization**: a present tense generalization without a quantifier in the subject noun phrase, describing results as applying to whole categories rather than to specific or quantified sets of individuals. [[10_markdown/documents/generalization-bias-llm-summarization-2025#^pc11]]
- **Action guiding generalization**: a summary that turns a descriptive result claim into a recommendation for a policy or an action. [[10_markdown/documents/generalization-bias-llm-summarization-2025#^pc13]]

## Open questions

- The source measures the scope of a conclusion against the original text and does not say whether a broader conclusion was in fact false, so the reported rates count scope drift rather than error.
- Why the accuracy prompt raised rather than lowered the rate of generalized conclusions is not resolved in the text.

## Appraisal

The design is preregistered, the coding is doubly staffed with a blinded third coder and reported agreement, and the comparison against human expert summaries of the same articles is what gives the finding its force, because it separates a model-specific tendency from the ordinary looseness of science communication. For this vault the finding matters at the distillate layer, where a statement is taken from a passage and can silently widen while every anchor still resolves.

## Related

- [[20_distillates/documents/fabricated-citations-chatgpt-2023]]
- [[20_distillates/documents/legal-ai-research-tools-hallucination-2025]]
