---
title: Specification
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
expected-warnings: [W-NO-OUTPUT, W-PLACEHOLDER]
related: [index, schema, operations]
---

# Specification

Purpose, parameters and settled decisions of this vault instance. The invariant architecture (layer model, anchor mechanics, check contracts, status progression) lives in [[knowledge/schema]] and [[knowledge/operations]]; this document holds what this project decided.

## Purpose

<!-- One paragraph, whose first sentence names the overall topic of the vault: what
     output this vault produces, on what, for whom, under which evidence obligation. -->

{{PURPOSE}}

## Parameters

| Parameter | Value |
|---|---|
| Controlled topic set | {{TOPICS}} <!-- becomes the MOC set in 30_assertions/ --> |
| Active source types | {{SOURCE_TYPES}} <!-- document, publication, data --> |
| Output genre | {{GENRE}} <!-- strategy, proposal, report, scholarly synthesis --> |
| Chapter register | see [[knowledge/state]] |
| Working language of content | {{LANGUAGE}} |
| Verification role | {{VERIFICATION_ROLE}} <!-- role and institution --> |
| Validation mechanism | `tools/validate.py` |
| Machine review mechanism | {{REVIEW_MECHANISM}} <!-- reviewer model and pairing tooling --> |

## Style sheet

<!-- Rules for the output prose: register, citation display, terminology choices. -->

{{STYLE_SHEET}}

## Settled decisions

<!-- One line per decision with date; the reasoning behind each lives in the journal. -->

- {{DATE}}: Vault instantiated from the Grounded Vault template.
