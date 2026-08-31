---
type: moc
topic: "Verification"
created: 2026-08-10
updated: 2026-08-10
---

# MOC: Verification

The judgment side of the method, the evidence question. It covers how and by whom it is established that a source location supports a statement, the three checking instances with their objects and authority, the status ladder with its audit trail, and human verification as the act that turns grounding into evidence. Supporting strands hold the attribution literature that founds the separation of attributability from truth, the documented weaknesses of machine generated text that make checking necessary, and the reliability of machine checkers, which justifies the design choices of the LLM review and stays a side matter.

- [[30_assertions/attribution-is-separate-from-correctness]], whether a source supports a statement is judged apart from whether the statement is true.
- [[30_assertions/generated-citations-often-fail-to-support-their-sentences]], measured support rates of citations in generative search engines.
- [[30_assertions/source-binding-lowers-unsupported-citation-without-eliminating-it]], fabrication without binding and the measured residual under retrieval.
- [[30_assertions/resolvable-citation-without-support-is-a-distinct-error-class]], the misgrounded citation resolves and still fails its statement, and is harder to detect.
- [[30_assertions/llm-evaluators-favor-their-own-generations]], self preference correlates with self recognition.
- [[30_assertions/cross-family-evaluator-panels-reduce-intra-model-bias]], panels of disjoint families judge with less intra model bias.
- [[30_assertions/historical-method-separates-origin-check-from-credibility]], the two stage critique of the historical method and its order.
- [[30_assertions/llm-summaries-broaden-the-scope-of-findings]], scope drift in machine summaries and the accuracy prompt that worsens it.

## Open questions

- What sampling density does human verification need before a vault counts as reviewed?
- Do panel and self preference findings transfer to the judgment whether a passage supports a statement, which both sources leave untested?
- Does a broadened conclusion also become a false one, which the generalization study does not measure?
- Why does an accuracy prompt raise the rate of overgeneralization instead of lowering it?
