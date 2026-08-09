# Setup

Instantiate the template by setting a small number of parameters. Everything else, the layer model, the anchor mechanics, the check contracts and the status progression, is invariant and stays untouched.

## Parameters

Decide these before filling anything:

1. **Topic and topic backbone** — the controlled list of topics; each becomes one `MOC-<Topic>.md` in `30_claims/`.
2. **Active source types** — `document`, `publication`, `data`; activate what the project needs.
3. **Deliverable genre and chapter register** — strategy, proposal, report or scholarly synthesis, and its chapters.
4. **Working language of content** — deliverable, claims and distillates; `knowledge/` and `CLAUDE.md` stay English.
5. **Verification role** — who holds the authority to establish evidence (role and institution).
6. **Check mechanisms** — validation is `tools/validate.py`; choose the machine review mechanism (reviewer model, ideally from a different family than the producing agent).

## Fill-in order

1. Replace the `{{…}}` placeholders in `knowledge/specification.md` with the parameters; this is the single place they live.
2. Fill the remaining placeholders in `knowledge/index.md`, `state.md`, `journal.md`, `CLAUDE.md`, `HOME.md` (project name, repository, date, language).
3. Create one `MOC-<Topic>.md` per backbone topic in `30_claims/` (schema in `knowledge/schema.md` § Topic map).
4. Write the chapter register into `knowledge/state.md`.
5. Keep `examples/`, because `tests/test_validate.py` runs against those fixtures and proves the validator catches anything at all; delete `docs/` if unwanted.
6. Run `python tools/validate.py .` and `python -m pytest tests`. A fresh instance raises two warnings, `W-NO-INVENTORY` until the register lists its first documents and `W-NO-DELIVERABLE` until the first chapter exists. Once you know which of them your instance will keep, enter them under `expected-warnings` in `knowledge/specification.md`, so that any further warning stands out as a finding.
7. Commit as the instantiation milestone; note it in `knowledge/journal.md`.

## First production cycle

Acquire one source, ingest it, distill it, build one claim, write one paragraph with one grounded footnote and, if honest, one posit. Run the validator after each step. This smallest full pass exercises every layer and every rule before scale does.
