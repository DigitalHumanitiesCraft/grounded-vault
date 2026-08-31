---
type: representation
source-type: data
data: "[[10_markdown/data/review-runs-2026-08-10.csv]]"
channel: handover
metadata:
  title: "Machine review runs of the Grounded Vault paper instance, first pass, 2026-08-10"
  creator: "Digital humanities research, University of Graz and Digital Humanities Craft"
  date: "2026-08-10"
  format: "text/csv"
  identifier: "grounded-vault-paper review runs 2026-08-10"
  license: "CC-BY-4.0"
  confidential: false
created: 2026-08-10
updated: 2026-08-10
---

# Machine review runs, first pass

How many pairs the adversarial machine review examined on 2026-08-10, per checked document. One row per document of the first pass over that document. The review followed the review contract of the template, with the reviewer seeing only the pair and never the producing agent's reasoning.

## Columns

- `layer`, the layer the checked document belongs to, one of `assertion`, `distillate`, `chapter`.
- `document`, the slug of the checked document without its folder.
- `pairs_reviewed`, the number of pairs the reviewer of that document reported a verdict for in the first pass.

## Scope and limitations

The table covers the first pass only. Later passes over reworked pairs are not counted here, because they cover a selection rather than a document and would make the column ambiguous.

A pair is one statement together with the one source location named for it. At the assertion layer the pair is an assertion and one of its grounding statements, at the distillate layer a distillate statement and its anchored block or verbatim quotation, at the chapter layer a footnoted sentence and the statement section of the assertion it names. Footnotes marked as posits carry no source location and are outside the count.

The counts are the reported figures of the reviewing agents, transcribed by the orchestrating agent from their reports. They were not recomputed from a machine-readable review log, because the review ran through subagents whose verdicts existed only as reports. This is the weakest point of the dataset and the reason the review contract should require a written verdict record.
