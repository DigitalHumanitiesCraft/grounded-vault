---
title: Journal
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
related: [specification, state]
---

# Journal

Chronological decision history of the vault, append-only, newest entry last. Content documents carry only current state, and the reasoning that led there lives here. An entry records a decision, a rejected alternative with the reason, or a calibration result of a check mechanism.

## Entry format

```markdown
## 2026-10-03, <one-line subject>

<What was decided or found, why, and what it replaces. Link the affected
documents. Two to ten sentences.>
```

## 2026-10-03, vault instantiated

Instantiated from the Grounded Vault template (https://github.com/DigitalHumanitiesCraft/grounded-vault/tree/main/examples/prov-entity). Parameters recorded in [[knowledge/specification]].

## 2026-10-03, bounded public source

The example retains only the entity definition selected from the dated W3C Recommendation. The original copyright notice, status and source URL accompany the excerpt. Source material retains W3C document terms, while authored example prose uses CC BY 4.0. Content starts at grounded with no fabricated review records.

## 2026-10-03, recorded machine review

A fresh-context Codex subagent judged only the exported source and assertion prompts and returned fully-supporting verdicts. The original results and prompt hashes are preserved in `checks/review-2026-10-03.jsonl`, and the review tool booked them after matching the current pairs. Clean validation was recorded before the distillate, assertion and chapter advanced to validated. Model-family independence was not established, and human verification remains unperformed.
