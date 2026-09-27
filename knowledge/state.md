---
title: State
project:
  name: "{{PROJECT_NAME}}"
  repository: "{{REPOSITORY}}"
method:
  name: Promptotyping
  url: https://dhcraft.org/Promptotyping/
status: draft
language: en
created: "{{DATE}}"
updated: "{{DATE}}"
related: [operations, journal]
---

# State

Everything volatile is kept here, so the rule documents stay stable. Update rows here as work proceeds, and never record processing state anywhere else.

## Source inventory

One row per source. The processing status runs `new` → `ingested` → `distilled`. This section is generated from the real file state by `python tools/inventory.py . --write` and is never edited by hand. Everything between the two markers is overwritten on each run.

<!-- inventory:begin -->
| Source | Type | Channel | Markdown representation | Distillate | Coverage | Status |
|---|---|---|---|---|---|---|
<!-- inventory:end -->

## Chapter register

One row per chapter of the output. Writing status mirrors the chapter's frontmatter.

| Chapter | File | Status | Notes |
|---|---|---|---|
| | | | |

## Open work

<!-- Short, current list. Done items are deleted, and decisions go to the journal. -->

- Instantiate the template (see SETUP.md).
