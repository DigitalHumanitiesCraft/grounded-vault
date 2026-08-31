---
type: representation
source-type: data
data: "[[10_markdown/data/review-findings-2026-08-10.csv]]"
channel: handover
metadata:
  title: "Machine review verdicts of the Grounded Vault paper instance, 2026-08-10"
  creator: "Digital humanities research, University of Graz and Digital Humanities Craft"
  date: "2026-08-10"
  format: "text/csv"
  identifier: "grounded-vault-paper review findings 2026-08-10"
  license: "CC-BY-4.0"
  confidential: false
created: 2026-08-10
updated: 2026-08-10
---

# Machine review verdicts

The verdicts recorded on 2026-08-10 while the vault was built, one row per reviewed pair that was written down.

## Columns

- `layer`, one of `assertion`, `distillate`, `chapter`.
- `round`, the pass in which the verdict was given. Round one is the first review of that pair, round two a later review that still found something.
- `document`, the slug of the checked document.
- `anchor`, the source location of the pair. At the assertion layer the distillate statement, at the distillate layer the statement ID, at the chapter layer the assertion the footnote names.
- `verdict`, one of the five values of the review contract, `fully supports`, `partially supports`, `overreaches`, `contradicts`, `not in the text`. Only `fully supports` passes.
- `category`, the kind of defect, empty where the verdict passed. The values arose from the reports and were not fixed in advance, so they are a description of what occurred rather than a controlled vocabulary.

## Scope and limitations

Coverage differs by layer, and this asymmetry has to be carried into every reading of the table. At the assertion layer and at the chapter layer every pair of the first pass is recorded, passing verdicts included. At the distillate layer only the pairs below `fully supports` are recorded, because the reports listed passing verdicts as a keyword rather than a row. The count of reviewed pairs per document lives in the sibling dataset [[10_markdown/data/review-runs-2026-08-10]], and any rate over the distillate layer has to be computed against that table.

Category values were assigned by the orchestrating agent from the reviewers' justifications. Their boundaries are soft, in particular between `modality drift` and `overgeneralization`, where a dropped hedge and a widened scope can describe the same sentence.

The verdicts come from agents of the same model family as the producing agents, which the instance decided against the cross-family recommendation of the template. Self-preference of evaluators towards their own family is documented, so the passing rates of this table are an upper bound rather than a neutral measurement.
