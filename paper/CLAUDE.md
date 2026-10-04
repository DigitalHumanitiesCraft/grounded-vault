# Grounded Vault Internal Manuscript Action Layer

This directory is a Grounded Vault instance nested inside the Grounded Vault reference repository. Its `knowledge/` holds the six project knowledge documents, of which index, schema and operations are copies of the root documents held equal to them by `tests/test_instances.py`, and specification, state and journal are the instance's own.

## Session start

Read `knowledge/index.md`, then `knowledge/specification.md` and `knowledge/state.md`. For content work, follow the task routing table of the root `CLAUDE.md`, reading its rows against this instance's `knowledge/schema.md` and `knowledge/operations.md`.

## Output scope

The instance has one output line and one manuscript, `40_output/grounded-vault-method.md`. It is an internal method elaboration with no submission target. The Promptotyping paper is a separate publication project and remains the publication line intended for submission.

## Hard rules

The hard rules of the root `CLAUDE.md` apply with `paper` as the vault root in every command, among them the footnote and posit contract of `knowledge/schema.md` § Chapter. The working language of this instance is English, as `knowledge/specification.md` records. This instance adds four rules.

- Chapter footnotes to assertions carry no alias.
- Anchors and statement IDs imported from the source instance remain unchanged.
- Before reporting manuscript work as complete, run `uv run python tools/validate.py paper` and `uv run python tools/validate.py paper --chapter 40_output/grounded-vault-method` from the repository root.
- Manuscript prose follows the style sheet in `knowledge/specification.md`.
