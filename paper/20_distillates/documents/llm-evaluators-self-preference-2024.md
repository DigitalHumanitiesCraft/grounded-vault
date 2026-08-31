---
type: distillate
source-type: document
representation: "[[10_markdown/documents/llm-evaluators-self-preference-2024]]"
topics: ["[[Verification]]", "[[Agentic Workflow]]"]
status: validated
checked:
  validation: 2026-08-10
  machine-review: 2026-08-10
created: 2026-08-10
updated: 2026-08-10
---

# Distillate: LLM Evaluators Recognize and Favor Their Own Generations

The source measures whether a model scores its own outputs higher than others' and ties that preference to the model's ability to recognize its own text, which is the empirical ground for keeping producer and reviewer apart in this vault.

## Core statements

- Out of the box, models such as GPT-4 and Llama 2 distinguish their own outputs from those of other models and of humans with non-trivial accuracy, and fine-tuning reveals a linear correlation between self-recognition capability and the strength of self-preference bias. [[10_markdown/documents/llm-evaluators-self-preference-2024#^pk01]] ^s1
- Self-preference is the phenomenon in which a model favours its own outputs over texts from other models and from humans. [[10_markdown/documents/llm-evaluators-self-preference-2024#^pk10]] ^s2
- Self-recognition is the capability of a model to distinguish its own outputs from texts by other models or by humans. [[10_markdown/documents/llm-evaluators-self-preference-2024#^pk11]] ^s3
- On two summarization tasks, GPT-3.5 Turbo, GPT-4 and Llama 2 disproportionately favour summaries written by themselves over those written by other models and by humans. [[10_markdown/documents/llm-evaluators-self-preference-2024#^pk06]] ^s4
- All three evaluated models exceed 50% accuracy at distinguishing their own outputs from other sources using simple prompts without fine-tuning, and GPT-4 reaches 73.5% accuracy at distinguishing itself from two other models and from humans. [[10_markdown/documents/llm-evaluators-self-preference-2024#^pk07]] ^s5
- After fine-tuning on 500 examples, GPT-3.5 and Llama 2 each exceed 90% accuracy at self-recognition. [[10_markdown/documents/llm-evaluators-self-preference-2024#^pk08]] ^s6
- In the pairwise setting, fine-tuning for self-recognition produces a strong linear correlation between a model's self-recognition ability and its self-preference, and the effect of fine-tuning on one dataset transfers to the other. [[10_markdown/documents/llm-evaluators-self-preference-2024#^pk39]] ^s7
- At the level of individual examples and before fine-tuning, the GPT-3.5 evaluator on XSUM shows a correlation of 0.41 in Kendall's tau between correctly recognizing its own summary in a pair and preferring that summary, and every fine-tuning configuration yields a positive correlation on this metric. [[10_markdown/documents/llm-evaluators-self-preference-2024#^pk40]] ^s8
- Excluding the fine-tuning runs with degraded generation quality, evaluators show an average preference of 0.46 for the fine-tuned models' generations, a slight preference against them. [[10_markdown/documents/llm-evaluators-self-preference-2024#^pk42]] ^s9
- Models fine-tuned on tasks unrelated to self-recognition, namely length, vowel count, readability score, always answering "1" and answering randomly, fall on the same linear trend as the models fine-tuned on self-recognition. [[10_markdown/documents/llm-evaluators-self-preference-2024#^pk43]] ^s10
- When the source labels in the pairwise self-preference question are reversed, the GPT-4 and GPT-3.5 evaluators reverse their self-preference on the XSUM dataset and prefer the summary labelled as their own generation. [[10_markdown/documents/llm-evaluators-self-preference-2024#^pk44]] ^s11
- All three evaluator models display ordering bias, reversing their pairwise preferences when the order of the options is reversed at rates of 25% for GPT-4, 58% for GPT-3.5 and 89% for Llama, averaged across tasks and datasets. [[10_markdown/documents/llm-evaluators-self-preference-2024#^pk30]] ^s12
- In the pairwise setting all models show their greatest self-preference against the human-written summary. [[10_markdown/documents/llm-evaluators-self-preference-2024#^pk28]] ^s13
- Weaker models struggle to distinguish themselves from stronger ones, with Llama 2 wholly unable to distinguish itself from GPT-3.5 and GPT-4. [[10_markdown/documents/llm-evaluators-self-preference-2024#^pk25]] ^s14

## Terms

- **Self-preference**: an evaluator model scoring its own outputs higher than texts from other models or humans that human annotators judge to be of equal quality. [[10_markdown/documents/llm-evaluators-self-preference-2024#^pk03]]
- **Prosaic interpretation of "self"**: the empirical use of the term, which claims no notion or representation of a self in the model and allows preference and recognition to exist independently of one another. [[10_markdown/documents/llm-evaluators-self-preference-2024#^pk12]]

## Open questions

- The source establishes correlation and rules out one inverse explanation, and states that validating the causal hypothesis would require mechanistic tools that do not yet exist for these models.
- The measurements cover summarization on two news datasets and three model families, so the transfer to an evaluator judging whether a passage supports a statement is open.

## Appraisal

A careful correlational study with the confounder controls a causal claim needs, and honest about the causal claim it cannot make. For this vault it carries the machine review contract rather than a content finding: if preference tracks recognition, then a reviewer drawn from the model family that produced the statement is systematically the wrong instance to refute it, which is why the review role here is filled from a different family than the producing agent.

## Related

- [[20_distillates/publications/llm-jury-panel-evaluation-2024]]
