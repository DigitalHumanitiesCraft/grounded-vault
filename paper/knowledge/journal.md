---
title: Journal
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
related: [specification, state]
---

# Journal

Chronological decision history of the vault, append-only, newest entry last. Content documents carry only current state; the reasoning that led there lives here. An entry records a decision, a rejected alternative with the reason, or a calibration result of a check mechanism.

## Entry format

```markdown
## <ISO date> — <one-line subject>

<What was decided or found, why, and what it replaces. Link the affected
documents. Two to ten sentences.>
```

## 2026-08-09 — Vault instantiated

Instantiated from the Grounded Vault template (DigitalHumanitiesCraft/grounded-vault). Parameters recorded in [[knowledge/specification]]. The instance was placed in the `paper/` subdirectory of the template repository rather than in a repository of its own, so that the article is written against exactly the version of the template it describes and a change to the architecture is visible in the same commit history as the article that reports it. The validator reads only the content folders and the inventory register of the root it is handed, so a run over the repository root does not see this instance and a run over `paper/` does not see the empty vault at the root.

## 2026-08-09 — No fixture copy in this instance

`SETUP.md` step 5 tells an instance to leave `tests/fixtures/` in place, because the coverage tests of the validator run against it and deleting it leaves those tests pointed at directories that do not exist. That reasoning is about the repository holding the test suite. Here the test suite and its fixtures lie at the repository root, one level above this instance, and `python -m pytest tests` continues to run against them unchanged. A copy under `paper/tests/fixtures/` would duplicate the specimen vaults without any suite running over the copy, and the copy would drift silently from the specimens the coverage test actually holds the finding codes against. The instance therefore keeps no fixtures of its own, and the obligation from `SETUP.md` is met by the root copy.

## 2026-08-09 — Own analysis folder for data anchors

The source type `data` is active, and the validator resolves the script of a declared computation against the vault root it is handed. For this instance that root is `paper/`, so a data anchor has to name `tools/analysis/<script>.py` beneath it. `paper/tools/analysis/` is created empty for that purpose. The root `tools/` keeps the template's own executables, the validator, the reviewer, the migration helper and the page generator, and this instance calls them from the repository root rather than copying them.

## 2026-08-09 — W-EMPTY never fired in this instance

`SETUP.md` tells a fresh instance to declare three warnings, `W-PLACEHOLDER` until every placeholder is replaced, `W-NO-OUTPUT` until the first chapter exists, and `W-EMPTY` until the first document enters the production chain. Both `W-PLACEHOLDER` and `W-EMPTY` were satisfied by instantiation itself and were removed from the declaration, the first because every placeholder is filled and the second for a reason worth recording. `W-EMPTY` asks whether any document lies in `10_markdown` through `40_output`, and the five topic maps that instantiation creates lie in `30_assertions`, so the check counts the chain as populated while no content document exists. An instance that follows the prescribed order therefore never has an occasion to declare `W-EMPTY`. The declaration was dropped rather than kept, because a declaration that does not fire is itself reported as `W-STALE-EXPECTATION`. The mismatch between the instruction and the check is a finding about the template and belongs to the article's own material.

## 2026-08-09 — Claims fixed before the sources

The article's six claims were written into [[knowledge/specification]] ahead of any ingest, each with the evidence that would carry it and the state of that evidence. Fixing the argument first makes the source work directed, because a source enters for a named claim, and it makes the gap visible where a claim currently has no source, which is the case for the two claims resting on counts from validator runs and for the claim about declared uncertainty. Claim two carries its own negative finding, that the migration data shows enforceability while no controlled comparison exists that could show a quality gain in the finished text, and that limit stays in the claim rather than being softened during writing.
