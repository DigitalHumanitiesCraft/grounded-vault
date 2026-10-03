---
title: Specification
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
related: [index, schema, operations]
---

# Specification

Purpose, parameters and settled decisions are what this vault instance decided. The invariant architecture (layer model, anchor mechanics, check contracts, status progression) lives in [[knowledge/schema]] and [[knowledge/operations]].

## Purpose

<!-- One paragraph, whose first sentence names the overall topic of the vault, meaning
     what output this vault produces, on what, for whom and under which evidence obligation. -->

The entity definition in the PROV Data Model supplies a public source for a complete Grounded Vault example. A reader follows the selected passage through its Markdown representation and source-bound statement to an assertion and a short output paragraph. The example demonstrates traceability under the template contracts.

## Parameters

| Parameter | Value |
|---|---|
| Controlled topic set | Provenance <!-- becomes the MOC set in 30_assertions/ --> |
| Active source types | document <!-- document, publication, data --> |
| Output genre | Worked example <!-- strategy, proposal, report, scholarly synthesis --> |
| Chapter register | see [[knowledge/state]] |
| Working language of content | English |
| Verification role | The reader designated to verify this example. Human verification has not been performed. <!-- role and institution --> |
| Validation mechanism | `tools/validate.py` |
| Machine review mechanism | Repository tools/review.py exports source and assertion pairs for an independently instructed reviewer. The reviewer returns content-bound judgements for import. <!-- reviewer model and pairing tooling --> |

## Style sheet

<!-- Rules for the output prose, covering register, citation display and terminology choices. -->

Use concise English prose. Preserve the scope of the quoted definition and attribute it to PROV-DM. Cite the assertion through a grounded footnote in the output.

## Settled decisions

<!-- One line per decision with date. The reasoning behind each lives in the journal. -->

- 2026-10-03: Vault instantiated from the Grounded Vault template.
