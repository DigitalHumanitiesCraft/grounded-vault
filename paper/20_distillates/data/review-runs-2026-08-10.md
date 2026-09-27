---
type: distillate
source-type: data
representation: "[[10_markdown/data/review-runs-2026-08-10]]"
topics: ["[[Instances]]", "[[Verification]]"]
status: grounded
checked:
  validation: 2026-09-27
created: 2026-08-10
updated: 2026-09-27
---

# Distillate: Machine review runs, first pass

The first-pass review runs recorded on 2026-08-10 by the Grounded Vault paper instance chpollin/grounded-vault-paper, the source instance from which this vault imported its research foundation. The core statements were written there, so "this vault" in them names that source instance.

## Core statements

- In its first pass over this vault on 2026-08-10 the adversarial machine review reported verdicts for 501 pairs of a statement and its named source location, 405 of them at the distillate layer, 87 at the assertion layer and 9 at the chapter layer. ^s1
    - computation: `python tools/analysis/review_pairs_by_layer.py` → `assertion 87, chapter 9, distillate 405, total 501`
- The first pass covered 46 documents, 25 distillates, 20 assertions and one chapter. ^s2
    - computation: `python tools/analysis/review_documents_reviewed.py` → `assertion 20, chapter 1, distillate 25, total 46`

## Terms

- **Pair**: one statement together with the single source location named for it, which is the unit the review contract judges.

## Open questions

- How many pairs did the second and third review pass cover?
- Do the reported pair counts match the number of pairs the reviewing agents actually cut?

## Appraisal

The dataset is a transcription of agent reports rather than a log written by the reviewing process itself, which is its central weakness and the reason it should not be read as a measurement. Its value lies in the order of magnitude and in the distribution across layers, both of which show where the checking effort of an instance actually falls. The distillate layer carries four fifths of the pairs, which follows from the schema, since every statement of every source is a pair while an assertion binds only a handful of them.

## Related

- [[20_distillates/data/review-findings-2026-08-10]]
