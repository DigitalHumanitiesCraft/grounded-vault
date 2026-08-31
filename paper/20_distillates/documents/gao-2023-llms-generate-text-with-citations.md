---
type: distillate
source-type: document
representation: "[[10_markdown/documents/gao-2023-llms-generate-text-with-citations]]"
topics: ["[[Verification]]", "[[Architecture]]"]
status: validated
checked:
  validation: 2026-08-10
  machine-review: 2026-08-10
created: 2026-08-10
updated: 2026-08-10
---

# Distillate: Enabling Large Language Models to Generate Text with Citations

The source builds ALCE, a benchmark that scores a generated answer with citations along separate axes, keeping whether the answer is correct apart from whether its citations carry it.

## Core statements

- The source proposes ALCE as a benchmark for automatic evaluation of citations produced by large language models, and reports that on the ELI5 dataset even the best models lack complete citation support 50% of the time. [[10_markdown/documents/gao-2023-llms-generate-text-with-citations#^b01]] ^s1

- The source states that citations let users verify a model's claims and that generating text which follows the cited passages holds the promise of improving correctness and reducing hallucination. [[10_markdown/documents/gao-2023-llms-generate-text-with-citations#^b03]] ^s2

- The source argues that prior work on citation-producing systems mainly experiments with commercial search engines and closed-source models and mostly relies on human evaluation, and that the absence of automated evaluation hinders the advances of such systems. [[10_markdown/documents/gao-2023-llms-generate-text-with-citations#^b04]] ^s3

- The source formalizes the task as returning an output that consists of statements, each of which cites a list of passages from the corpus, and segments model output into statements at sentence boundaries. [[10_markdown/documents/gao-2023-llms-generate-text-with-citations#^b09]] ^s4

- The source divides the retrieval corpus into 100-word passages, on the grounds that such a passage is easier for humans to verify and allows more retrieved passages to fit into the limited context of an LLM. [[10_markdown/documents/gao-2023-llms-generate-text-with-citations#^b10]] ^s5

- The source states that its benchmark measures three dimensions of a system response. [[10_markdown/documents/gao-2023-llms-generate-text-with-citations#^b16]] ^s6

- The source defines correctness as whether the answer is accurate and covers all aspects of interest. [[10_markdown/documents/gao-2023-llms-generate-text-with-citations#^b18]] ^s7

- The source defines citation quality as whether the answer is well supported by the cited passages and no irrelevant passages are cited. [[10_markdown/documents/gao-2023-llms-generate-text-with-citations#^b19]] ^s8

- The source operationalizes correctness as agreement with a ground truth answer and treats it as a proxy for the informativeness and utility of the generation. [[10_markdown/documents/gao-2023-llms-generate-text-with-citations#^b22]] ^s9

- The source splits citation quality into citation recall, which asks whether the output is entirely supported by the cited passages, and citation precision, which identifies irrelevant citations. [[10_markdown/documents/gao-2023-llms-generate-text-with-citations#^b26]] ^s10

- The source computes citation recall per statement as a binary value and ties it to the AIS framework, in that entailment of the statement by the concatenated citations means the statement is true based solely on those passages. [[10_markdown/documents/gao-2023-llms-generate-text-with-citations#^b28]] ^s11

- The source states that its citation precision detects irrelevant citations without requiring a minimal citing set, because human writing also cites redundant sources. [[10_markdown/documents/gao-2023-llms-generate-text-with-citations#^b29]] ^s12

- The source shows that its combination of metrics resists two shortcut responses, copying the top retrieved passage and citing it, and copying its first two sentences, because each shortcut fails on fluency or on correctness while scoring almost perfectly on citations. [[10_markdown/documents/gao-2023-llms-generate-text-with-citations#^b32]] ^s13

- The source reports that summarizing or snippeting retrieved passages raises correctness while costing citation quality on ASQA and ELI5, which it attributes to lossy compression. [[10_markdown/documents/gao-2023-llms-generate-text-with-citations#^b35]] ^s14

- The source reports that utility scores in its human evaluation differ little between models, ranging from 3.7 to 3.9 on ASQA and from 3.5 to 3.6 on ELI5. [[10_markdown/documents/gao-2023-llms-generate-text-with-citations#^b38]] ^s15

- The source reports that its automatic citation metrics agree with human judgments at a Cohen's kappa of 0.698 for citation recall and 0.525 for citation precision, and reach an accuracy of 85.1% for citation recall and 77.6% for citation precision against human annotations. [[10_markdown/documents/gao-2023-llms-generate-text-with-citations#^b39]] ^s16

- The source names, among others, enhancing retrieval, developing long-context models and advancing the ability to synthesize multiple sources as promising research directions its experiments point to. [[10_markdown/documents/gao-2023-llms-generate-text-with-citations#^b41]] ^s17

## Terms

- **Citation recall**: the per-statement binary judgment of whether the concatenation of a statement's citations entails the statement, averaged over all statements of a response [[10_markdown/documents/gao-2023-llms-generate-text-with-citations#^b28]]
- **Citation precision**: the per-citation binary judgment of whether a citation is not irrelevant, given that its statement already has recall 1, averaged over all citations of a response [[10_markdown/documents/gao-2023-llms-generate-text-with-citations#^b30]]
- **Correctness**: whether the answer is accurate compared to a ground truth answer, used as a proxy for informativeness and utility [[10_markdown/documents/gao-2023-llms-generate-text-with-citations#^b22]]

## Open questions

- The source measures entailment with an NLI model and reports in its limitations that the model cannot detect partial support, so the relation between machine-judged and human-judged citation quality remains approximate.
- The source segments output at sentence boundaries and does not settle how to score a sentence carrying several independently verifiable claims.
- The source evaluates prompting only and leaves open whether a model trained to cite behaves differently on these axes.

## Appraisal

The source matters to this vault less for its benchmark scores than for the separation it enforces in its metric design: an answer can be correct and badly cited, or well cited and wrong, and the evaluation refuses to collapse the two. That is the same cut this vault draws between a statement and its anchor, arrived at independently and from the direction of automatic evaluation. The shortcut analysis is the strongest part of the argument, because it shows that citation quality alone is gameable by copying, which is the failure mode a purely structural grounding check also has. The correlation with human judgment is reported as substantial for recall and merely moderate for precision, which supports keeping a human instance in the loop rather than treating an automatic entailment verdict as final.

## Related

- [[20_distillates/publications/rashkin-2023-measuring-attribution]]
- [[20_distillates/documents/liu-2023-evaluating-verifiability-generative-search-engines]]
