# Grounded Vault Internal Manuscript Action Layer

This directory is a Grounded Vault instance nested inside the Grounded Vault reference repository. The invariant architecture and procedures live in `../knowledge/`. Instance parameters and provenance live in `knowledge/` below this directory.

## Session start

Read `../knowledge/index.md`, then `knowledge/specification.md` and `knowledge/state.md`. For content work, follow the task route in the root `knowledge/schema.md` and `knowledge/operations.md`.

## Output scope

The instance has one output line and one manuscript, `40_output/grounded-vault-method.md`. It is an internal method elaboration with no submission target. The Promptotyping paper is a separate publication project and remains the publication line intended for submission.

## Hard rules

The hard rules of the root `CLAUDE.md` apply unchanged, among them the footnote and posit contract of `../knowledge/schema.md` § 7 Chapter. This instance adds four.

- Chapter footnotes to assertions carry no alias.
- Anchors and statement IDs imported from the source instance remain unchanged.
- Before reporting manuscript work as complete, run `python tools/validate.py paper` and `python tools/validate.py paper --chapter 40_output/grounded-vault-method` from the repository root.
- Manuscript prose follows the style sheet in `knowledge/specification.md`.
