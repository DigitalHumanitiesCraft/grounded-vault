---
type: distillate
source-type: publication
reference: "anthropic2025context"
topics: ["[[Architecture]]", "[[Agentic Workflow]]"]
status: validated
checked:
  quote: 2026-08-10
  validation: 2026-08-10
  machine-review: 2026-08-10
created: 2026-08-10
updated: 2026-08-10
---

# Distillate: Anthropic, Effective context engineering for AI agents

An engineering post by the model vendor that fixes the term context engineering, sets it off against prompt engineering, and states why the context window is treated as a finite resource.

## Core statements

- The post defines context as the set of tokens that enter the model when it is sampled. ^s1
  > "Context refers to the set of tokens included when sampling from a large-language model (LLM)." (anthropic2025context, section "Effective context engineering for AI agents")

- The post defines context engineering as the strategies for curating and maintaining the set of tokens present during inference, and it counts information reaching the model outside the prompts as part of that set. ^s2
  > "Context engineering refers to the set of strategies for curating and maintaining the optimal set of tokens (information) during LLM inference, including all the other information that may land there outside of the prompts." (anthropic2025context, section "Context engineering vs. prompt engineering")

- The post places context engineering as the successor of prompt engineering and restricts prompt engineering to the writing and organising of model instructions. ^s3
  > "At Anthropic, we view context engineering as the natural progression of prompt engineering. Prompt engineering refers to methods for writing and organizing LLM instructions for optimal outcomes" (anthropic2025context, section "Context engineering vs. prompt engineering")

- The post separates the two by their temporal shape, calling prompt writing a discrete task and context curation a step that recurs at every handover to the model. ^s4
  > "In contrast to the discrete task of writing a prompt, context engineering is iterative and the curation phase happens each time we decide what to pass to the model." (anthropic2025context, section "Context engineering vs. prompt engineering")

- The post attributes the concept of context rot to needle-in-a-haystack benchmarking and states it as the decline of accurate recall from the context window as the number of tokens in it rises. ^s5
  > "Studies on needle-in-a-haystack style benchmarking have uncovered the concept of context rot: as the number of tokens in the context window increases, the model’s ability to accurately recall information from that context decreases." (anthropic2025context, section "Why context engineering is important to building capable agents")

- The post states the criterion for good context engineering as finding the smallest possible set of high-signal tokens that maximize the likelihood of some desired outcome. ^s6
  > "good context engineering means finding the smallest possible set of high-signal tokens that maximize the likelihood of some desired outcome." (anthropic2025context, section "The anatomy of effective context")

## Terms

- **Context**: the set of tokens included when sampling from a large language model.
- **Context engineering**: the strategies for curating and maintaining the optimal set of tokens during inference, including everything that reaches the model outside the prompts.
- **Prompt engineering**: methods for writing and organising model instructions for optimal outcomes.
- **Context rot**: the decline of recall accuracy from the context window as its token count grows.

## Open questions

- The post gives no measurement procedure for context rot and names no threshold at which the effect becomes practically relevant.
- It leaves open how the "smallest possible set of high-signal tokens" is to be determined for a concrete task other than by trial.

## Appraisal

A vendor engineering post, not peer-reviewed, and interested in the tools of its own house. Its value for this vault is terminological, because it is the reference statement much of the field cites for the term context engineering, and because it draws the boundary to prompt engineering explicitly rather than by implication. Its empirical claims, above all context rot, rest on studies it names without reproducing, so they carry as reported positions rather than as findings this vault can check.

## Related

- [[20_distillates/documents/promptotyping-specification-2026-07-31]]
