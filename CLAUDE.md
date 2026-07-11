# {{PROJECT_NAME}} — Agent Action Layer

<!-- TEMPLATE NOTE: while this repository is the un-instantiated template, this file
     documents the action layer's shape. SETUP.md fills the placeholders. -->

This vault is a Grounded Vault instance. Every substantive statement you produce here must carry a grounding anchor; the rules live in `knowledge/`, and this file only routes you there. Do not duplicate rules here.

## Session start

Read in this order: `knowledge/index.md` (terminology), `knowledge/state.md` (where work stands), then the document your task routes to below.

## Task routing

| Task | Read first | Chain |
|---|---|---|
| Add a source | `knowledge/operations.md` § Acquire, Ingest | acquire → ingest |
| Distill a source | `knowledge/schema.md` § Distillate, `operations.md` § Distill | three-stage chain |
| Build or revise claims | `schema.md` § Claim, `operations.md` § Build claims | claims |
| Write a chapter | `schema.md` § Chapter, `operations.md` § Write chapters | chapters |
| Answer a question | `operations.md` § Query | query |
| Check the vault | `operations.md` § Check | validate → review |

## Hard rules

- Anchors are minted only at their own layer; never invent a block or statement ID that does not exist.
- A status is set only after its check ran; record the date in `checked`. Never set `verified`; that is the human verification role's alone.
- Own conclusions become posits in the deliverable, never claims.
- Run `python tools/validate.py .` before reporting any production task as done.
- Volatile state goes to `knowledge/state.md`, decisions to `knowledge/journal.md` (append-only).
- Working language of content: {{LANGUAGE}}. This action layer and `knowledge/` stay English.

## Harness block (exchangeable)

<!-- This block is specific to Claude Code and may be replaced for another harness. -->

- Commit at milestones with concise English imperative messages; stage explicit paths.
- {{HARNESS_RULES}}
