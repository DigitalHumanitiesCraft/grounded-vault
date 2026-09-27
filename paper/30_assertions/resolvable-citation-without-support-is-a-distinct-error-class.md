---
type: assertion
topics: ["[[Verification]]"]
status: grounded
checked:
  validation: 2026-08-10
  machine-review: 2026-08-10
grounding:
  - "[[20_distillates/documents/legal-ai-research-tools-hallucination-2025#^s4]]"
  - "[[20_distillates/documents/legal-ai-research-tools-hallucination-2025#^s5]]"
  - "[[20_distillates/documents/legal-ai-research-tools-hallucination-2025#^s6]]"
  - "[[20_distillates/documents/liu-2023-evaluating-verifiability-generative-search-engines#^s2]]"
contested-with: []
created: 2026-08-10
updated: 2026-08-10
---

# A resolvable citation that fails to support its statement is a distinct and harder to detect error class

## Statement

Where a system cites real documents, the citation relation can still break. A response counts as misgrounded when its key propositions are cited but the citation misinterprets its source or names an inapplicable one, and a misgrounded response counts as a hallucination in the same sense as an incorrect statement. Detecting this class costs the user more than detecting an outright fabricated case, because it requires opening the cited references, reading and understanding them, assessing their authority and comparing them with the propositions they are meant to support. In the audited generative search engines only 74.5% of citations support the sentence they are attached to.

## Support

- [[20_distillates/documents/legal-ai-research-tools-hallucination-2025#^s4]] — supplies the definition of misgrounded as cited but misinterpreting or inapplicable, which separates this class from the missing citation.
- [[20_distillates/documents/legal-ai-research-tools-hallucination-2025#^s5]] — establishes that a misgrounded response is a hallucination on a par with an incorrect statement.
- [[20_distillates/documents/legal-ai-research-tools-hallucination-2025#^s6]] — supplies the detection cost that makes this class harder to catch than a fabricated case.
- [[20_distillates/documents/liu-2023-evaluating-verifiability-generative-search-engines#^s2]] — supplies the measured share of citations that support their sentence, without separating the error classes.

## Related

- [[30_assertions/generated-citations-often-fail-to-support-their-sentences]]
- [[30_assertions/source-binding-lowers-unsupported-citation-without-eliminating-it]]
