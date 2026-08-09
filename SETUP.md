# Setup

Instantiate the template by setting a small number of parameters. Everything else, the layer model, the anchor mechanics, the check contracts and the status progression, is invariant and stays untouched.

## Placeholders

Every `{{…}}` marker in the repository belongs to one of two classes. Class A is instance data that follows from the repository itself. Class B is a project decision that has to be taken before anything is filled. A third group is derived content, produced from the class B decisions rather than substituted for a marker.

### Class A, instance data

| Marker | Definition |
|---|---|
| `{{PROJECT_NAME}}` | The name of this vault instance, used as the title of `HOME.md` and `CLAUDE.md` and in the Promptotyping header of every knowledge document. |
| `{{REPOSITORY}}` | The repository this instance lives in, as a URL or an `owner/name` slug. |
| `{{DATE}}` | The instantiation date in ISO 8601, written into `created` and `updated` and into the first entry of the settled decisions. |

### Class B, project decisions

| Marker | Definition |
|---|---|
| `{{PURPOSE}}` | One paragraph on what deliverable this vault produces, for whom and under which evidence obligation, whose first sentence names the overall topic of the vault. |
| `{{TOPICS}}` | The controlled topic set, meaning the closed list of topics that claims may be filed under; each topic becomes one `MOC-<Topic>.md` in `30_claims/`. |
| `{{SOURCE_TYPES}}` | The source types this project activates out of `document`, `publication` and `data`. |
| `{{GENRE}}` | The genre of the deliverable, such as strategy, proposal, report or scholarly synthesis. |
| `{{LANGUAGE}}` | The working language of the content, meaning deliverable, claims and distillates; `knowledge/` and `CLAUDE.md` stay English. |
| `{{VERIFICATION_ROLE}}` | The role and institution holding the authority to establish evidence. |
| `{{REVIEW_MECHANISM}}` | The mechanism fulfilling the machine review contract, meaning the reviewer model and the pairing tooling; a reviewer from a different model family than the producing agent decorrelates error modes. |
| `{{STYLE_SHEET}}` | The rules for the deliverable prose, covering register, citation display and terminology choices. |
| `{{HARNESS_RULES}}` | The harness-specific rules of the exchangeable block at the end of `CLAUDE.md`, such as which commands an agent may run unasked. |

### Derived content

Three things are written rather than substituted. One `MOC-<Topic>.md` per topic of the controlled topic set in `30_claims/`, schema in `knowledge/schema.md` § Topic map. The topic map link list under "Explore the knowledge" in `HOME.md`, one wikilink per MOC file. The chapter register in `knowledge/state.md`, one row per chapter of the deliverable.

## Fill-in order

1. Replace the class B markers in `knowledge/specification.md`; this is the single place the decisions live.
2. Replace the class A markers in `knowledge/index.md`, `schema.md`, `operations.md`, `state.md`, `journal.md`, `specification.md`, `CLAUDE.md` and `HOME.md`, plus `{{LANGUAGE}}` and `{{HARNESS_RULES}}` in `CLAUDE.md`.
3. Create one `MOC-<Topic>.md` per topic in `30_claims/` and write the matching link list into `HOME.md`.
4. Write the chapter register into `knowledge/state.md`.
5. Keep `examples/`, because `tests/test_validate.py` runs against those fixtures and proves the validator catches anything at all; delete `docs/` if unwanted.
6. Run `python tools/validate.py .` and `python -m pytest tests`. The template declares the two warnings a fresh instance raises under `expected-warnings` in `knowledge/specification.md`, `W-NO-DELIVERABLE` until the first chapter exists and `W-PLACEHOLDER` until every placeholder is replaced. Once instantiation has satisfied a declaration, the validator reports it as `W-STALE-EXPECTATION`; remove the satisfied entry then, so that any further warning stands out as a finding.
7. Commit as the instantiation milestone; note it in `knowledge/journal.md`.

## Prompt for the first agent session

Start an agent session in the repository root and give it this prompt.

```
Instantiate this Grounded Vault template for my project.

Read SETUP.md, knowledge/index.md and knowledge/schema.md first, then work in
this order and stop for me where the instructions say so.

1. Ask me for the class B decisions from SETUP.md, one question at a time, in
   the order PURPOSE, TOPICS, SOURCE_TYPES, GENRE, LANGUAGE, VERIFICATION_ROLE,
   REVIEW_MECHANISM, STYLE_SHEET, HARNESS_RULES. Propose a concrete default
   where my answer allows one, and do not invent a decision I have not given.
2. Read the class A values off the repository and the current date, and confirm
   them with me in one step.
3. Replace every {{...}} placeholder in the repository with the agreed values.
   Do not touch examples/, tests/ or tools/.
4. Create one MOC-<Topic>.md file in 30_claims/ per topic of the controlled
   topic set, following the topic map schema, and replace the topic map line in
   HOME.md with one wikilink per MOC file.
5. Write the chapter register into knowledge/state.md, one row per chapter of
   the deliverable, all rows at writing status planned.
6. Run `python tools/validate.py .`. Fix every error. Then check the declared
   expected-warnings in knowledge/specification.md against the run and remove
   every declaration the validator reports as W-STALE-EXPECTATION.
7. Commit the instantiation as one milestone and append a dated entry to
   knowledge/journal.md naming the decisions taken.

Report what you filled, which MOC files you created and the final validator
output.
```

## Installing the dependencies

The validator needs PyYAML, the test suite additionally pytest. With uv, `uv sync` installs both from `pyproject.toml`. Without uv, `pip install pyyaml pytest` covers the same set.

## First production cycle

Acquire one source, ingest it, distill it, build one claim, write one paragraph with one grounded footnote and, where the synthesis calls for one, one posit. Run the validator after each step. This smallest full pass exercises every layer and every rule before scale does.
