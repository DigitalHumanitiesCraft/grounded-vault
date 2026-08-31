---
type: distillate
source-type: data
representation: "[[10_markdown/data/review-findings-2026-08-10]]"
topics: ["[[Instances]]", "[[Verification]]"]
status: validated
checked:
  validation: 2026-08-10
  machine-review: 2026-08-10
created: 2026-08-10
updated: 2026-08-10
---

# Distillate: Machine review verdicts

## Core statements

- The review of this vault on 2026-08-10 recorded 101 verdicts below full support, 76 at the distillate layer, 18 at the assertion layer and 7 at the chapter layer. ^s1
    - computation: `python tools/analysis/review_failed_verdicts.py` → `assertion 18, chapter 7, distillate 76, total 101`
- No recorded verdict was contradicts or not in the text. ^s2
    - computation: `python tools/analysis/review_contradictions.py` → `0`
- Among the recorded defects the most frequent category is modality drift with 32 cases, followed by scope mismatch with 19, a statement reaching into a neighbouring block with 18 and an unanchored detail with 17. ^s3
    - computation: `python tools/analysis/review_categories.py` → `modality drift 32, scope mismatch 19, neighbouring block 18, unanchored detail 17, overgeneralization 7, producer inference 5, distributive reading 1, unanchored evaluation 1, ordering claim 1`

## Terms

- **Modality drift**: a source hedge such as may, should, broadly or usually disappears in the statement built on the source, which turns a recommendation or a possibility into a fact.
- **Neighbouring block**: the statement carries information that stands in the source next to the anchored block rather than inside it, so the anchor is too narrow for the statement.

## Open questions

- Whether the same distribution of categories arises with a reviewer of a different model family is untested in this instance, since all reviewers came from the family of the producing agents.
- Whether the absence of contradicts reflects the material or the review setup cannot be decided from this dataset alone.

## Appraisal

The category counts are the most usable part of the dataset, because they name failure modes that recur across sources of very different kinds, from a W3C recommendation to a French methodological handbook of 1898. Modality drift alone accounts for roughly a third of the defects and appears at every layer, which suggests a systematic tendency of the producing agents rather than a property of individual sources. The absence of any contradicts verdict is the weakest figure of the three, since a reviewer sharing the producing family has the least chance of catching precisely the errors that family makes.

## Related

- [[20_distillates/data/review-runs-2026-08-10]]
