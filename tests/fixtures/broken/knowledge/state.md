---
title: State
status: draft
language: en
created: "2026-07-25"
updated: "2026-08-10"
---

# State

The volatile state of the broken example. The source inventory below is what
`python tools/inventory.py` generates from the file state of this fixture; the
validator does not read it, so nothing here is a check.

## Source inventory

<!-- inventory:begin -->
| Source | Type | Channel | Markdown representation | Distillate | Coverage | Status |
|---|---|---|---|---|---|---|
| Data representation with a dead data link | data | handover | [[10_markdown/data/dead-data]] | — | — | ingested |
| Data representation without data | data | handover | [[10_markdown/data/no-data]] | — | — | ingested |
| Broken fixture note | document | handover | [[10_markdown/documents/note]] | [[20_distillates/data/computation-defects]] | 1/1 | distilled |
| Broken fixture note | document | handover | [[10_markdown/documents/note]] | [[20_distillates/data/missing-script]] | 1/1 | distilled |
| Broken fixture note | document | handover | [[10_markdown/documents/note]] | [[20_distillates/data/outside-analysis]] | 1/1 | distilled |
| Broken fixture note | document | handover | [[10_markdown/documents/note]] | [[20_distillates/documents/appraisal-anchor]] | 1/1 | distilled |
| Broken fixture note | document | handover | [[10_markdown/documents/note]] | [[20_distillates/documents/checked-bad-date]] | 1/1 | distilled |
| Broken fixture note | document | handover | [[10_markdown/documents/note]] | [[20_distillates/documents/checked-not-a-map]] | 1/1 | distilled |
| Broken fixture note | document | handover | [[10_markdown/documents/note]] | [[20_distillates/documents/duplicate-statements]] | 1/1 | distilled |
| Broken fixture note | document | handover | [[10_markdown/documents/note]] | [[20_distillates/documents/illegal-source-type]] | 1/1 | distilled |
| Broken fixture note | document | handover | [[10_markdown/documents/note]] | [[20_distillates/documents/no-core-statements]] | 1/1 | distilled |
| Broken fixture note | document | handover | [[10_markdown/documents/note]] | [[20_distillates/documents/no-statement-id]] | 1/1 | distilled |
| Broken fixture note | document | handover | [[10_markdown/documents/note]] | [[20_distillates/documents/note]] | 1/1 | distilled |
| Broken fixture note | document | handover | [[10_markdown/documents/note]] | [[20_distillates/documents/sideways]] | 1/1 | distilled |
| Broken fixture note | document | handover | [[10_markdown/documents/note]] | [[20_distillates/documents/stale]] | 1/1 | distilled |
| Broken fixture note | document | handover | [[10_markdown/documents/note]] | [[20_distillates/documents/statement-defects]] | 1/1 | distilled |
| Broken fixture note | document | handover | [[10_markdown/documents/note]] | [[20_distillates/documents/unquoted-topics]] | 1/1 | distilled |
| dead-representation | document | — | — | [[20_distillates/documents/dead-representation]] | — | distilled |
| Duplicate block fixture note | document | handover | [[10_markdown/documents/duplicate-blocks]] | — | — | ingested |
| incomplete-representation | document | handover | [[10_markdown/documents/incomplete-representation]] | — | — | ingested |
| no-representation | document | — | — | [[20_distillates/documents/no-representation]] | — | distilled |
| Placeholder fixture note | document | handover | [[10_markdown/documents/placeholder-note]] | — | — | ingested |
| representation-wrong-layer | document | — | — | [[20_distillates/documents/representation-wrong-layer]] | — | distilled |
| malformed-quotation | publication | — | — | [[20_distillates/publications/malformed-quotation]] | — | distilled |
| no-quote-check | publication | — | — | [[20_distillates/publications/no-quote-check]] | — | distilled |
| no-reference | publication | — | — | [[20_distillates/publications/no-reference]] | — | distilled |
| Publication representation fixture | publication | import | [[10_markdown/documents/publication-representation]] | — | — | ingested |
| unversioned-quote | publication | — | — | [[20_distillates/publications/unversioned-quote]] | — | distilled |
<!-- inventory:end -->
