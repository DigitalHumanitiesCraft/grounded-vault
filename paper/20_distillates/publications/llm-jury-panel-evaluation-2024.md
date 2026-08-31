---
type: distillate
source-type: publication
reference: "verga2024juries"
topics: ["[[Verification]]", "[[Agentic Workflow]]"]
status: validated
checked:
  quote: 2026-08-10
  validation: 2026-08-10
  machine-review: 2026-08-10
created: 2026-08-10
updated: 2026-08-10
---

# Distillate: Replacing Judges with Juries

The source replaces the single large judge model with a panel drawn from disjoint model families and reports that the panel correlates better with human judgment while showing less intra-model bias, which is the design argument behind this vault's machine review role.

## Core statements

- A panel of several smaller evaluator models outperforms a single large judge, shows less intra-model bias because its members come from disjoint model families, and costs over seven times less. ^s1
  > "Across three distinct judge settings and spanning six different datasets, we find that using a PoLL composed of a larger number of smaller models outperforms a single large judge, exhibits less intra-model bias due to its composition of disjoint model families, and does so while being over seven times less expensive." (arXiv:2404.18796v2, p. 1)
- The paper names intra-model bias as one of the largest issues with relying on a single judge model such as GPT-4. ^s2
  > "one of the largest issues with relying on a single model J, such as GPT-4, is that it introduces intra-model bias." (arXiv:2404.18796v2, p. 2)
- Pooling judgments across a panel of heterogeneous evaluator models reduces intra-model scoring bias. ^s3
  > "Intra-model scoring bias is reduced by pooling judgements across a panel of heterogeneous evaluator models (Section 4.4)." (arXiv:2404.18796v2, p. 2)
- The panel used in the experiments consists of three models drawn from three different model families. ^s4
  > "In our experiments, We construct a PoLL from three models being drawn from three disparate model families (Command R, Haiku, and GPT3.5)." (arXiv:2404.18796v2, p. 3)
- Overall the panel correlates most strongly across the tasks compared, while GPT-4 is one of the weaker evaluators in that task setup. ^s5
  > "We see that overall, PoLL has the strongest correlation across various tasks, while GPT-4 is one of the weaker evaluators on this particular task setup" (arXiv:2404.18796v2, p. 4)
- Measured against human annotators on the multi-hop datasets, the panel has the smallest spread in scores, with a standard deviation of 2.2 against exact match and the individual judges, while GPT-3.5 has the highest spread at 6.1. ^s6
  > "we compared the delta in absolute accuracy score for our individual judges and PoLL relative to scores by human annotators across our multi-hop datasets. Figures 3 and 4 show results on HotPotQA and Bamboogle. We can see how the different judges score different models and how far those predictions deviate from human annotator decisions (the dotted line at 0). We observe that overall, PoLL has the smallest spread in scores, with a standard deviation of 2.2, compared to EM and individual judges. GPT-3.5 has the highest spread, with a standard deviation of 6.1." (arXiv:2404.18796v2, p. 5)
- For each individual model being scored, the highest positive delta occurs when it is judged by itself. ^s7
  > "We also see in Figure 4 that the highest positive delta for each individual model being scored occurs when it is judged by itself." (arXiv:2404.18796v2, p. 5)
- The GPT-4 judge ranks another GPT-4 variant in position 2, two positions above its actual position 4, which the paper reads as intra-model bias. ^s8
  > "We can clearly observe intra-model bias as the GPT-4 judge ranks another GPT-4 variant in position 2, higher than its actual position 4" (arXiv:2404.18796v2, p. 5)
- Running the three-model panel is seven to eight times cheaper than running a single large judge, depending on the ratio of input to output tokens. ^s9
  > "Depending on the ratio of input-to-output tokens in a given task, running the entire three model PoLL is seven to eight times less expensive than running a single GPT-4 judge." (arXiv:2404.18796v2, p. 6)
- The work investigated only three evaluator settings and a limited number of judges and panel compositions. ^s10
  > "In this work we investigated only three evaluator settings and a limited number of judges and panel compositions." (arXiv:2404.18796v2, p. 6)

## Terms

- **Panel of LLM evaluators (PoLL)**: a set of judge models from different families, each scoring an output independently, whose individual scores are combined by a voting function into the final score.
  > "To calculate the PoLL score, each evaluator model independently scores a given model output just as they would in any of the scenarios outlined above." (arXiv:2404.18796v2, p. 2)
- **Intra-model bias**: the tendency of an evaluator model to recognize and prefer its own outputs over those of other models.
  > "it has also been observed that evaluator models tend to have their own biases; often recognizing and preferring their own outputs over those of other models" (arXiv:2404.18796v2, p. 2)

## Open questions

- The source shows that a heterogeneous panel reduces intra-model bias without giving a rule for composing one, and names panel selection as open work.
- The judge settings are question answering and pairwise chat comparison, so whether the result carries over to judging whether a passage supports a statement is untested here.

## Appraisal

An industry preprint by the vendor of one of the panel models, which is a standing reason for caution about the cost argument, and the bias finding is the part that does not depend on that interest, because it reproduces on a third-party ranking with a third-party judge. For this vault the paper supplies the constructive counterpart to the self-preference finding: separating the reviewer from the producer by model family is a design one can implement, and pooling several reviewers is the stronger version of it.

## Related

- [[20_distillates/documents/llm-evaluators-self-preference-2024]]
