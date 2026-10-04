# Agent Action Layer of PROV-DM entity worked example

This vault is a Grounded Vault instance. Every source-supported statement you produce here carries a grounding anchor, and every conclusion of your own is marked as a posit. The rules are defined in `knowledge/`, and this file routes you there. The hard rules below are the imperative short form of rules defined there, each with a pointer to its section.

## Session start

Read `knowledge/index.md` (terminology) first, then `knowledge/state.md` (where work stands), then the document your task routes to below.

## Task routing

| Task | Read first | Chain |
|---|---|---|
| Add a source | `knowledge/operations.md` § Acquire, Ingest | acquire → ingest |
| Replace a source by a revised version | `operations.md` § Supersede | ingest → distill → supersede |
| Distill a source | `knowledge/schema.md` § Distillate, `operations.md` § Distill | three-stage chain |
| Build or revise assertions | `schema.md` § Assertion, `operations.md` § Build assertions | assertions |
| Write a chapter | `schema.md` § Chapter, `operations.md` § Write chapters | chapters |
| Answer a question | `operations.md` § Query | query |
| Check the vault | `operations.md` § Check | validate → review |

## Hard rules

- Anchors are minted only at their own layer. Never invent a block or statement ID that does not exist (`knowledge/schema.md` § Layer model).
- A Markdown representation is never edited after ingest. A revised source enters as a new file with a date-suffixed slug (`operations.md` § Ingest, § Supersede, `schema.md` § Document types).
- A status is set only after its check ran, with the date recorded in `checked`. Never set `verified`, which only the human verification role sets (`schema.md` § Audit trail, `operations.md` § Check).
- Never file an own conclusion as an assertion. It enters the output as a posit (`operations.md` § Build assertions, § Write chapters).
- Run `uv run python tools/validate.py examples/prov-entity` before reporting any production task as done, and act on every warning as well as every error (`operations.md` § Validation contract).
- Volatile state goes to `knowledge/state.md`, decisions to `knowledge/journal.md`, which is append-only (`knowledge/index.md` § The six project knowledge documents).
- Content is written in English. This action layer and `knowledge/` stay English (`knowledge/specification.md` § Parameters, row Working language).

## Harness block (exchangeable)

This block is specific to Claude Code and may be replaced for another harness. For Claude Code the three skills `ingest-source`, `distill-source` and `build-assertions` live under `.claude/skills/` and route to the corresponding sections of `knowledge/operations.md`, which stays the single place the rules are written down. The `run` subcommand of `tools/review.py` judges through the local `claude -p` command line, which in this harness calls a model of the producer's own family, so a reviewer from another family goes through `emit` and `judge`.

- Commit at milestones with concise English imperative messages, and stage explicit paths.
- Run every command from the repository root with `examples/prov-entity` as the vault root, as `README.md` of this example lists them.
- Keep `manifest.json` in step with `00_sources/` and `10_markdown/`, and record returned review batches under `checks/`.
