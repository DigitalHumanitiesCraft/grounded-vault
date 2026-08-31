---
type: distillate
source-type: data
representation: "[[10_markdown/data/review-runs-2026-08-10]]"
topics: ["[[Instances]]", "[[Verification]]"]
status: validated
checked:
  validation: 2026-08-10
  machine-review: 2026-08-10
created: 2026-08-10
updated: 2026-08-10
---

# Distillate: Machine review runs, first pass

## Core statements

- In its first pass over this vault on 2026-08-10 the adversarial machine review reported verdicts for 501 pairs of a statement and its named source location, 405 of them at the distillate layer, 87 at the assertion layer and 9 at the chapter layer. ^s1
    - computation: `python tools/analysis/review_pairs_by_layer.py` → `assertion 87, chapter 9, distillate 405, total 501`
- The first pass covered 46 documents, 25 distillates, 20 assertions and one chapter. ^s2
    - computation: `python tools/analysis/review_documents_reviewed.py` → `assertion 20, chapter 1, distillate 25, total 46`

## Terms

- **Pair**: one statement together with the single source location named for it, which is the unit the review contract judges.

## Open questions

- How many pairs a second and third pass covered is not recorded, because later passes examined a selection of reworked pairs rather than whole documents.
- Whether the reported pair counts match the number of pairs actually cut cannot be checked, since the reviewing agents produced no machine-readable log.

## Appraisal

The dataset is a transcription of agent reports rather than a log written by the reviewing process itself, which is its central weakness and the reason it should not be read as a measurement. Its value lies in the order of magnitude and in the distribution across layers, both of which show where the checking effort of an instance actually falls. The distillate layer carries four fifths of the pairs, which follows from the schema, since every statement of every source is a pair while an assertion binds only a handful of them.

## Related

- [[20_distillates/data/review-findings-2026-08-10]]
