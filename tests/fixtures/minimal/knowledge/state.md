---
title: State
status: draft
language: en
created: "2026-07-25"
updated: "2026-08-10"
---

# State

The volatile state of the minimal example. The source inventory below is what
`python tools/inventory.py tests/fixtures/minimal --write` generates from the
file state; the validator does not read it, so nothing here is a check.

## Source inventory

<!-- inventory:begin -->
| Source | Type | Channel | Markdown representation | Distillate | Status |
|---|---|---|---|---|---|
| Quarterly water meter readings 2024–2025 | data | handover | [[10_markdown/data/water-readings-2025]] | [[20_distillates/data/water-readings-2025]] | distilled |
| Annual Water Report of the Example Community Garden 2026 | document | handover | [[10_markdown/documents/report-garden-water-2026]] | [[20_distillates/documents/report-garden-water-2026]] | distilled |
| Water Metering in Community Gardens: A Fictional Review | publication | import | — | [[20_distillates/publications/example-2024-metering]] | distilled |
<!-- inventory:end -->
