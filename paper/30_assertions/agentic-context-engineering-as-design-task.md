---
type: assertion
topics: ["[[Agentic Workflow]]"]
status: grounded
checked:
  validation: 2026-09-27
grounding:
  - "[[20_distillates/publications/anthropic-2025-context-engineering#^s2]]"
  - "[[20_distillates/publications/anthropic-2025-context-engineering#^s4]]"
  - "[[20_distillates/publications/anthropic-2025-context-engineering#^s6]]"
  - "[[20_distillates/documents/liu-2024-lost-in-the-middle#^s1]]"
  - "[[20_distillates/documents/liu-2024-lost-in-the-middle#^s2]]"
  - "[[20_distillates/documents/liu-2024-lost-in-the-middle#^s17]]"
contested-with: []
created: 2026-08-10
updated: 2026-09-27
---

# In the engineering post of the model vendor Anthropic, as accessed on 2026-08-10, context engineering treats the assembly of the model context as an engineering task with its own criterion

## Statement

In its engineering post of 2025, as accessed on 2026-08-10, the model vendor Anthropic handles the assembly of what reaches the model as work with a stated goal under the practice term context engineering. The post defines the term as the set of strategies for curating and maintaining the optimal set of tokens during inference, counting the information that lands in the context outside the prompts, and it states the criterion of doing it well as the smallest possible set of high-signal tokens that maximises the likelihood of some desired outcome. In the post, the curation phase recurs each time something is passed to the model, so the assembly is a repeated decision under that criterion. Experiments that vary the input context size and the position of the relevant information within it supply the empirical subject matter of such a decision, because model performance can degrade significantly when the position of the relevant information within the input context changes, with performance often highest when that information stands at the beginning or the end, and because a longer input context trades the added information against the added content the model must reason over.

## Support

- [[20_distillates/publications/anthropic-2025-context-engineering#^s2]], supplies the definition of context engineering as strategies for curating and maintaining the token set during inference
- [[20_distillates/publications/anthropic-2025-context-engineering#^s4]], gives the temporal shape, a curation phase recurring at every handover to the model
- [[20_distillates/publications/anthropic-2025-context-engineering#^s6]], states the optimisation criterion, the smallest set of high-signal tokens for the desired outcome
- [[20_distillates/documents/liu-2024-lost-in-the-middle#^s1]], reports the measured dependence of performance on the position of the relevant information
- [[20_distillates/documents/liu-2024-lost-in-the-middle#^s2]], carries the experimental variation of context size and position
- [[20_distillates/documents/liu-2024-lost-in-the-middle#^s17]], states the trade-off that more context brings more content to reason over

## Related

- [[30_assertions/agentic-promptotyping-knowledge-base-artifact]]
