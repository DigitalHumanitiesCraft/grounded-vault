# Grounded Vault Paper — Agent Action Layer

This vault is a Grounded Vault instance. Every substantive statement you produce here must carry a grounding anchor; the rules live in `knowledge/`, and this file only routes you there. Do not duplicate rules here.

The instance lives in the `paper/` subdirectory of the template repository `DigitalHumanitiesCraft/grounded-vault`. Paths in `knowledge/` are relative to this directory, and the executables in `tools/` lie one level up at the repository root, so a command is run from the repository root with `paper` as its vault argument.

## Session start

Read in this order: `knowledge/index.md` (terminology), `knowledge/state.md` (where work stands), then the document your task routes to below.

## Task routing

| Task | Read first | Chain |
|---|---|---|
| Add a source | `knowledge/operations.md` § Acquire, Ingest | acquire → ingest |
| Distill a source | `knowledge/schema.md` § Distillate, `operations.md` § Distill | three-stage chain |
| Build or revise assertions | `schema.md` § Assertion, `operations.md` § Build assertions | assertions |
| Write a chapter | `schema.md` § Chapter, `operations.md` § Write chapters | chapters |
| Answer a question | `operations.md` § Query | query |
| Check the vault | `operations.md` § Check | validate → review |

## Hard rules

- Anchors are minted only at their own layer; never invent a block or statement ID that does not exist.
- A Markdown representation is never edited after ingest; a revised source enters as a new file with a date-suffixed slug.
- A status is set only after its check ran; record the date in `checked`. Never set `verified`; that is the human verification role's alone.
- Own conclusions become posits in the output, never assertions.
- Run `python tools/validate.py paper` from the repository root before reporting any production task as done. Zero errors alone is not the criterion; a warning marked `*` is undeclared and is a finding, not background noise.
- Volatile state goes to `knowledge/state.md`, decisions to `knowledge/journal.md` (append-only).
- Working language of content: English. This action layer and `knowledge/` stay English.

## Self-application

The subject of this vault is the architecture this vault is built in. Two things follow. A statement about the architecture is grounded like any other, so the architecture's own documents enter as ordinary sources through `00_sources/` and are never cited from their live location in the repository, because a live file changes and an anchor into it would not hold. And a finding this instance produces about the architecture while working belongs in `knowledge/journal.md` as a dated entry, so that the article can later ingest it as a source instead of relying on memory.

## Harness block (exchangeable)

This block is specific to Claude Code and may be replaced for another harness. The three skills `ingest-source`, `distill-source` and `build-assertions` live in `.claude/skills/` at the repository root and route to the corresponding sections of `knowledge/operations.md`, which stays the single place the rules are written down. They apply to this instance unchanged; where a skill names a path, read it relative to `paper/`.

- Commit at milestones with concise English imperative messages; stage explicit paths.
- Never stage the repository root's `tools/`, `tests/` or `knowledge/` from a session working on this instance; the root is the template and is versioned separately from the article.
