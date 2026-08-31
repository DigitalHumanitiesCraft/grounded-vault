# Grounded Vault Internal Manuscript Action Layer

This directory is a Grounded Vault instance nested inside the Grounded Vault reference repository. The invariant architecture and procedures live in `../knowledge/`. Instance parameters and provenance live in `knowledge/` below this directory.

## Session start

Read `../knowledge/index.md`, then `knowledge/specification.md` and `knowledge/state.md`. For content work, follow the task route in the root `knowledge/schema.md` and `knowledge/operations.md`.

## Output scope

The instance has one output line and one manuscript, `40_output/grounded-vault-method.md`. It is an internal method elaboration with no submission target. The Promptotyping paper is a separate publication project and remains the publication line intended for submission.

## Hard rules

- Every load-bearing sentence in the manuscript carries an unaliased footnote to an assertion.
- Every own conclusion is marked as a posit with its rationale and open evidence question.
- Anchors and statement IDs imported from the source instance remain unchanged.
- New decisions go to `knowledge/journal.md`, which is append-only. Volatile state goes to `knowledge/state.md`.
- Set a status only after the corresponding check ran. Human verification alone may set `verified`.
- Run `python tools/validate.py paper` and the chapter-scoped validation before reporting manuscript work as complete.
- Manuscript prose follows the style sheet in `knowledge/specification.md`.
