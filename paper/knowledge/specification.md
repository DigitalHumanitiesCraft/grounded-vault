---
title: Specification
project:
  name: "Grounded Vault Paper"
  repository: "DigitalHumanitiesCraft/grounded-vault"
method:
  name: Promptotyping
  url: https://dhcraft.org/Promptotyping/
status: draft
language: en
created: "2026-08-09"
updated: "2026-08-09"
expected-warnings: [W-EMPTY, W-NO-OUTPUT]
related: [index, schema, operations]
---

# Specification

Purpose, parameters and settled decisions of this vault instance. The invariant architecture (layer model, anchor mechanics, check contracts, status progression) lives in [[knowledge/schema]] and [[knowledge/operations]]; this document holds what this project decided.

## Purpose

This vault produces a scholarly article on the Grounded Vault architecture, the repository form in which every substantive statement carries a machine-resolvable anchor into the material that supports it. Its audience is digital humanities research together with the adjacent computer science that builds agentic knowledge systems. Every substantive statement the article makes about the architecture and about its two real instances carries an anchor into the recorded evidence of those instances, meaning their journals, their commit histories, their validator runs and their review reports, so that a reader can hold any claim about what the architecture did against the artifact that shows it. The construction is self-applying, because the article about the build form is written with the build form, and the article's own vault is therefore part of what it describes. A conclusion the vault cannot ground enters the article as a marked posit and stays visible as one.

## Claims

The argument the instance has to carry, as the article's list of claims. Each claim names the evidence that would carry it and the state of that evidence, where `recorded` means the material exists and awaits ingest into this vault, and `to be gathered` means it has to be produced or located first.

1. Provenance in model-assisted knowledge work can be enforced as a structural property of the artifact instead of being hoped for as a behavioural property of the model.
   - Evidence: the validator's finding catalogue together with runs over the two instances, showing that a missing or unresolvable anchor fails the artifact regardless of how the producing model behaved.
   - State: recorded. The validator, its finding codes and its own test suite lie in this repository; the instance runs still have to enter as sources.
2. The error curve of two real migrations shows that the enforcement holds, and it shows no quality gain in the finished text, because the controlled comparison against an unanchored text was never run.
   - Evidence: validator error counts per run across the migration of both instances, as a `data` source with a deterministic computation over the run log, plus the record that no control condition exists.
   - State: to be gathered. The run logs have to be assembled from the instances' histories into one dataset.
3. Full anchor depth cannot be produced retroactively once the sources were not archived at the time of distillation, so the build form is decided by the source situation at the outset.
   - Evidence: journal entries and commits of the instance that distilled from unarchived sources, showing which anchor depth remained unreachable afterwards and what was substituted for it.
   - State: recorded in the affected instance's journal; not yet ingested.
4. The separation of the producing instance from the reviewing instance is effective, and the human bottleneck at the top rung of the status ladder is left in place deliberately.
   - Evidence: verdict distributions of machine review runs over both instances for the effectiveness, and the dated decision record for the deliberateness of the bottleneck.
   - State: to be gathered for the verdict distributions; the decision itself is recorded in the architecture's own documents.
5. A body of knowledge that counts its unchecked places as unchecked is more usable scholarly than one that stays silent about them.
   - Evidence: the status distributions of the two instances as a `data` source, and the surrounding literature on provenance and declared uncertainty as `publication` sources.
   - State: to be gathered. Without a publication anchor this claim carries only as far as the architecture's own reasoning and would enter the article as a posit.
6. An anchor guarantees traceability to a source; the correctness of that source is a separate question, and checking it is a separate act.
   - Evidence: the definitions of grounding, evidence and the three checking instances in the architecture's own schema and operations documents, taken as `document` sources.
   - State: recorded. The documents lie in this repository and enter as ordinary sources.

## Parameters

| Parameter | Value |
|---|---|
| Controlled topic set | Provenance, Verification, Architecture, Agentic Workflow, Instances |
| Active source types | document, publication, data |
| Output genre | scholarly article |
| Chapter register | see [[knowledge/state]] |
| Working language of content | English |
| Verification role | The authoring role of the article, digital humanities research at the University of Graz and at Digital Humanities Craft |
| Validation mechanism | `tools/validate.py` |
| Machine review mechanism | `tools/review.py` of the template, run with a reviewer model from a different model family than the producing agent |

## Style sheet

The output is English scholarly prose, matter-of-fact and without ornament. Four rules bind every chapter.

- No dash and no colon as a connector between clauses, for emphasis, or ahead of a summary. A colon stands only before a quotation, a code block or a list whose items sit on their own lines.
- No trailing negative apposition, meaning the patterns "X, not Y" and "not X, but Y". The point is stated positively, and an excluded alternative gets its own sentence.
- No triadic figures as a stylistic device and no parallelism for its own sake. An antithesis stands only where it carries content.
- No paragraph built towards an aphorism and no closing platitude, including the balanced both-sides closer.

Citations appear as footnotes. A footnote that reports a source-supported statement reads `Grounded in [[30_assertions/<slug>]]` and carries the bibliographic reference in the same note where the assertion rests on a publication. A footnote that reports the vault's own conclusion reads `Posit: <rationale>. Open evidence question: <question>`. Terminology follows [[knowledge/index]] without variation, so that grounding, evidence, provenance chain, assertion and posit keep one meaning across all chapters.

## Settled decisions

- 2026-08-09: Vault instantiated from the Grounded Vault template.
- 2026-08-09: The instance lives in the `paper/` subdirectory of the template repository, so that the article is written with the same version of the template it describes.
- 2026-08-09: No copy of `tests/fixtures/` in this instance; the reasoning is in [[knowledge/journal]].
- 2026-08-09: All three source types are active, with documents carrying the instance histories, publications the related literature and data the counts taken from validator runs.
