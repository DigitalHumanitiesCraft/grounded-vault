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

Chronological decision history of the vault, append-only, newest entry last. Content documents carry only current state, and the reasoning that led there lives here. An entry records a decision, a rejected alternative with the reason, or a calibration result of a check mechanism.

## Entry format

```markdown
## {{DATE}}, <one-line subject>

<What was decided or found, why, and what it replaces. Link the affected
documents. Two to ten sentences.>
```

## {{DATE}}, vault instantiated

Instantiated from the Grounded Vault template ({{REPOSITORY}}). Parameters recorded in [[knowledge/specification]].

## 2026-10-03, template review and public example

The public [PROV-DM example](../examples/prov-entity/README.md) now preserves a selected original excerpt and follows its anchor chain through a reviewed statement to output. Fresh-context machine review is recorded separately from formal validation and human verification. Review judgements are bound to the exact prompt, full assertion prose is paired, ambiguous imports fail and each check retains its own freshness. Fresh checkouts installed the locked dependencies and passed lint, formatting, regression tests, example validation and review import. Inventory and documentation regeneration reproduced the committed files without a diff. Template code follows the author's MIT instruction while authored text stays CC BY 4.0 and source terms remain unchanged. The root remains an uninstantiated template, and the internal paper's existing selective source coverage remains distinct from the example's checks.
