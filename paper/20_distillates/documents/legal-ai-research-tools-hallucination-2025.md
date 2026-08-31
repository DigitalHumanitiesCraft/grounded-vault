---
type: distillate
source-type: document
representation: "[[10_markdown/documents/legal-ai-research-tools-hallucination-2025]]"
topics: ["[[Verification]]", "[[Provenance]]", "[[Architecture]]"]
status: validated
checked:
  validation: 2026-08-10
  machine-review: 2026-08-10
created: 2026-08-10
updated: 2026-08-10
---

# Distillate: Hallucination-Free? Assessing the Reliability of Leading AI Legal Research Tools

The source measures three commercial retrieval-augmented legal research systems against hand-scored expert judgment and is the vault's evidence that retrieval over a closed, authoritative corpus reduces but does not remove unsupported statements.

## Core statements

- The AI research tools made by LexisNexis (Lexis+ AI) and Thomson Reuters (Westlaw AI-Assisted Research and Ask Practical Law AI) each hallucinate between 17% and 33% of the time, while hallucinations are reduced relative to the general-purpose chatbot GPT-4. [[10_markdown/documents/legal-ai-research-tools-hallucination-2025#^mg01]] ^s1
- More than one in six queries caused Lexis+ AI and Ask Practical Law AI to respond with misleading or false information, and one third of Westlaw's responses contained a hallucination. [[10_markdown/documents/legal-ai-research-tools-hallucination-2025#^mg50]] ^s2
- Answers were accurate, that is both correct and grounded, for 65% of queries with Lexis+ AI, 41% with Westlaw and 19% with Ask Practical Law AI, and the three systems gave incomplete answers 18%, 25% and 62% of the time respectively. [[10_markdown/documents/legal-ai-research-tools-hallucination-2025#^mg51]] ^s3
- A response counts as grounded when its key factual propositions make valid references to relevant legal documents, as ungrounded when key propositions are not cited, and as misgrounded when key propositions are cited but the citation misinterprets the source or names an inapplicable one. [[10_markdown/documents/legal-ai-research-tools-hallucination-2025#^mg24]] ^s4
- A response counts as hallucinated when it is either incorrect or misgrounded, so that falsely asserting that a source supports a statement is a hallucination in the same sense as making a false statement. [[10_markdown/documents/legal-ai-research-tools-hallucination-2025#^mg26]] ^s5
- The source judges the errors it discusses under its heading on hallucination to be potentially more dangerous than fabricating a case outright, because they are subtler and more difficult to spot, and checking for them requires users to click through to the cited references, read and understand the sources, assess their authority and compare them with the propositions the model seeks to support. [[10_markdown/documents/legal-ai-research-tools-hallucination-2025#^mg28]] ^s6
- The benchmark dataset was designed to represent real-life legal research scenarios without prior knowledge of whether a query would succeed or fail, and its queries are grouped into four broad categories, the first of which is general legal research questions. [[10_markdown/documents/legal-ai-research-tools-hallucination-2025#^mg32]] ^s7
- Each response was hand-scored against the rubric of correctness, groundedness and hallucination using the authors' own expert domain knowledge in law. [[10_markdown/documents/legal-ai-research-tools-hallucination-2025#^mg47]] ^s8
- Many failures in the three systems stem from poor retrieval, the system failing to find the most relevant sources available to address the user's query. [[10_markdown/documents/legal-ai-research-tools-hallucination-2025#^mg91]] ^s9
- An inapplicable authority error occurs when a system cites or discusses a document that is not legally applicable to the query, because it belongs to the wrong jurisdiction, statute or court, or has been overruled. [[10_markdown/documents/legal-ai-research-tools-hallucination-2025#^mg96]] ^s10
- Although sycophancy, the tendency to agree with a mistaken user, can cause hallucinations, Lexis+ AI, Westlaw AI-Assisted Research and GPT-4 navigated the false premise queries well and often corrected the false premise without hallucinating. [[10_markdown/documents/legal-ai-research-tools-hallucination-2025#^mg97]] ^s11

## Terms

- **Misgrounded**: cited but wrong in the relation between citation and claim, where the key propositions are supported by a reference that misinterprets its source or is inapplicable. [[10_markdown/documents/legal-ai-research-tools-hallucination-2025#^mg24]]
- **Naive retrieval**: a failure in which the retrieval step does not surface the most relevant source available for the query, so the generation step reasons over the wrong material. [[10_markdown/documents/legal-ai-research-tools-hallucination-2025#^mg91]]

## Open questions

- The evaluation covers three commercial products at one point in time, and the systems changed during the study, so the reported rates hold for the versions tested.
- The source does not report how much of the residual hallucination rate is attributable to retrieval and how much to generation, only which contributing causes appear among the hallucinated responses.

## Appraisal

A preregistered evaluation of closed commercial systems, hand-scored by domain experts, which is the only method available where no API and no ground-truth corpus can be had. Its most transferable contribution to this vault is conceptual rather than numeric: the separation of correctness from groundedness, and with it the error class of the real, resolvable citation that does not support the claim built on it. That class is precisely what a validator checking anchor resolution cannot see, and it is the reason this vault treats grounding as a structural property and evidence as a human verdict.

## Related

- [[20_distillates/documents/fabricated-citations-chatgpt-2023]]
- [[20_distillates/documents/generalization-bias-llm-summarization-2025]]
