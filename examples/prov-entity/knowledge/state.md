---
title: State
project:
  name: "PROV-DM entity worked example"
  repository: "https://github.com/DigitalHumanitiesCraft/grounded-vault/tree/main/examples/prov-entity"
method:
  name: Promptotyping
  url: https://dhcraft.org/Promptotyping/
status: draft
language: en
created: "2026-10-03"
updated: "2026-10-03"
related: [operations, journal]
---

# State

Everything volatile is kept here, so the rule documents stay stable. Update rows here as work proceeds, and never record processing state anywhere else.

## Source inventory

One row per source. The processing status runs `new` → `ingested` → `distilled`. This section is generated from the real file state by `python tools/inventory.py . --write` and is never edited by hand. Everything between the two markers is overwritten on each run.

<!-- inventory:begin -->
| Source | Type | Channel | Markdown representation | Distillate | Coverage | Status |
|---|---|---|---|---|---|---|
| PROV-DM: The PROV Data Model, section 5.1.1 Entity | document | collection | [[10_markdown/documents/prov-entity]] | [[20_distillates/documents/prov-entity]] | 1/1 | distilled |
<!-- inventory:end -->

## Chapter register

One row per chapter of the output. Writing status mirrors the chapter's frontmatter.

| Chapter | File | Status | Notes |
|---|---|---|---|
| Entity definition | [[40_output/01-entity-definition]] | validated | Formal validation and machine review passed. Human verification has not been performed. |

## Open work

<!-- Short, current list. Done items are deleted, and decisions go to the journal. -->

- Human verification of the source support remains with the designated example reader.
