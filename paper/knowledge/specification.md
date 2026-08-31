---
title: Specification
project:
  name: "Grounded Vault internal method manuscript"
  repository: "https://github.com/DigitalHumanitiesCraft/grounded-vault"
method:
  name: Promptotyping
  url: https://dhcraft.org/Promptotyping/
status: active
language: en
created: 2026-08-21
updated: 2026-08-21
related: [state, journal]
---

# Specification

This instance maintains the internal methodological account of Grounded Vault in one manuscript. It combines the former research blog with the planned article while retaining their common source, distillate, and assertion foundation. Every load-bearing manuscript sentence resolves through that foundation to a source passage, quotation, or computation.

## Publication status

The manuscript is an internal research artefact. It is not prepared for submission and carries no publication workflow. The Promptotyping paper is a separate project and remains the publication line intended for submission.

## Parameters

| Parameter | Value |
|---|---|
| Controlled topic set | Provenance, Verification, Architecture, Agentic Workflow, Instances |
| Active source types | document, publication, data |
| Output genre | internal methodological manuscript |
| Canonical output | `40_output/grounded-vault-method.md` |
| Working language | English |
| Verification role | authoring role in digital humanities research |
| Validation mechanism | root `tools/validate.py`, called with `paper` as vault root |
| Machine review mechanism | root `tools/review.py` under the shared review contract |

## Style sheet

The manuscript uses English scholarly prose. Every sentence carries concrete information. Colons, semicolons, and dashes are excluded from continuous prose. A colon remains permitted in the technical `Posit:` footnote contract. Trailing negative appositions, rhetorical triads, parallelism for effect, and aphoristic conclusions are excluded. Footnote wikilinks remain unaliased so the complete assertion title stays inspectable.

## Source provenance

The research foundation comes from the read-only repository `chpollin/grounded-vault-paper` at commit `3045fb48b4ca4570498ff8628ca9995d40aa9374`. Its Markdown representations, distillates, assertions, glossary, reference records, and analysis scripts were copied without content changes. The former validated blog chapter remains at that source commit and was used as an earlier synthesis of the same assertion layer.

## Settled decisions

- 2026-08-21. The former blog line and planned article line become one manuscript line in this repository.
- 2026-08-21. The canonical manuscript is an internal method elaboration with no submission target.
- 2026-08-21. The Promptotyping paper remains the separate publication line intended for submission.
- 2026-08-21. Imported anchors and statement IDs keep their source bytes and identifiers.
- 2026-08-21. Invariant governance and executable tools stay at the repository root. The nested instance stores only its parameters, state, provenance, and production layers.
