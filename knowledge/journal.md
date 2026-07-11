---
title: Journal
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
related: [specification, state]
---

# Journal

Chronological decision history of the vault, append-only, newest entry last. Content documents carry only current state; the reasoning that led there lives here. An entry records a decision, a rejected alternative with the reason, or a calibration result of a check mechanism.

## Entry format

```markdown
## {{DATE}} — <one-line subject>

<What was decided or found, why, and what it replaces. Link the affected
documents. Two to ten sentences.>
```

## {{DATE}} — Vault instantiated

Instantiated from the Grounded Vault template ({{REPOSITORY}}). Parameters recorded in [[knowledge/specification]].
