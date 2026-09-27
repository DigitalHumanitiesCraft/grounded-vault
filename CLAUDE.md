# Agent Action Layer of {{PROJECT_NAME}}

<!-- TEMPLATE NOTE: while this repository is the un-instantiated template, this file
     documents the action layer's shape. SETUP.md fills the placeholders. -->

This vault is a Grounded Vault instance. Every substantive statement you produce here must carry a grounding anchor. The rules are defined in `knowledge/`, and this file routes you there. The hard rules below are the imperative short form of rules defined there, each with a pointer to its section.

## Session start

Read `knowledge/index.md` (terminology) first, then `knowledge/state.md` (where work stands), then the document your task routes to below.

## Task routing

| Task | Read first | Chain |
|---|---|---|
| Instantiate the vault | `SETUP.md` | setup |
| Add a source | `knowledge/operations.md` § Acquire, Ingest | acquire → ingest |
| Distill a source | `knowledge/schema.md` § Distillate, `operations.md` § Distill | three-stage chain |
| Build or revise assertions | `schema.md` § Assertion, `operations.md` § Build assertions | assertions |
| Write a chapter | `schema.md` § Chapter, `operations.md` § Write chapters | chapters |
| Answer a question | `operations.md` § Query | query |
| Check the vault | `operations.md` § Check | validate → review |
| Work on the internal method manuscript | `paper/CLAUDE.md` | paper instance |

## Hard rules

- Anchors are minted only at their own layer. Never invent a block or statement ID that does not exist (`knowledge/schema.md` § Layer model).
- A Markdown representation is never edited after ingest. A revised source enters as a new file with a date-suffixed slug (`operations.md` § Ingest, `schema.md` § Document types).
- A status is set only after its check ran, with the date recorded in `checked`. Never set `verified`, which only the human verification role sets (`schema.md` § Audit trail, `operations.md` § Check).
- Never file an own conclusion as an assertion. It enters the output as a posit (`operations.md` § Build assertions, § Write chapters).
- Run `python tools/validate.py .` before reporting any production task as done, and act on every warning as well as every error (`operations.md` § Check, Contract: validation).
- Volatile state goes to `knowledge/state.md`, decisions to `knowledge/journal.md`, which is append-only (`knowledge/index.md` § The six project knowledge documents).
- Content is written in {{LANGUAGE}}. This action layer and `knowledge/` stay English (`knowledge/specification.md` § Parameters).

## Harness block (exchangeable)

This block is specific to Claude Code and may be replaced for another harness. For Claude Code the three skills `ingest-source`, `distill-source` and `build-assertions` live under `.claude/skills/` and route to the corresponding sections of `knowledge/operations.md`, which stays the single place the rules are written down. After a milestone commit that changes `README.md`, `docs/concept.md`, `knowledge/index.md`, `knowledge/schema.md` or `knowledge/operations.md`, run `python tools/build_docs.py --date <YYYY-MM-DD>` to regenerate the project page `docs/index.html` from exactly these files.

- Commit at milestones with concise English imperative messages, and stage explicit paths.
- {{HARNESS_RULES}}
