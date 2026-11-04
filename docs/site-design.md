# Site design

The public page `docs/index.html` explains Grounded Vault to readers without prior knowledge of Git, Obsidian or coding agents, in English by default and in German with `?lang=de`. It should let such a reader say what a vault is and for whom, follow one statement from a report down to its source and up through the three checks, and start a vault of their own. The page follows the Second Brain method page (`chpollin/second-brain-vault`, `docs/` and `knowledge/design.md` there) in design and structure.

## Sections

| Section | Question it answers | Form |
|---|---|---|
| Hero | What is this, for whom, and how does a statement stay checkable? | Title, one sentence on what it physically is, audience line, two actions, and the playable trace |
| Start | How do I start a vault? | Honest line about the terminal, tool list, six steps with a sentence each and a command or prompt to copy |
| Good to know | What does it not do, what leaves my computer, what does it cost? | Two columns of sentences with source links, and a short reading list into the repository |

## The trace

One sentence of a synthetic annual report of a city archive is followed down the five layers and then checked. The seven steps are named and grouped as trace down (sentence, assertion, distillate, source passage), machine checks (validation, machine review) and human check (verification).

- Each step is a complete state, so any step can be shown directly. Play advances with a delay derived from the caption length.
- The layers form one column. The vertical thread is the anchor path and lights up as layers are reached. A layer shows its excerpt once reached and its gloss before.
- The caption stands under the layer it explains. The controls stick to the foot of the viewport, and a computed scroll keeps the caption between header and controls.
- Step pills distinguish done (check mark), current (filled) and next (plain). The human step has its own group and a green outline once reached.
- The status ladder shows `grounded`, `validated` and `verified` with a gloss each. Reached statuses keep a check mark and are never struck through, because they accumulate.
- The machine review step shows a real catch. Minutes that only announce the reopening would make “has been open again” overreach, which is why the example's source is the April minutes recorded after the reopening.
- Anchors use the full layer paths of the schema, so the assertion visibly points into `20_distillates/` and the distillate into `10_markdown/`.

## Visual system

Tokens, fonts (Sora, Instrument Sans, vendored under `docs/assets/fonts/` with their licences), pill buttons and the white DHCraft mark are those of the Second Brain page. The hero stands on the navy night ground, reading sections on paper. Lines appear only on interactive elements and as the anchor thread. Check results carry the colour of their authority (script blue, language model amber, person green) together with a symbol, so they do not rest on colour alone.

## Terms

| English | German |
|---|---|
| assertion | Assertion |
| distillate | Destillat |
| Markdown copy | Markdown-Fassung |
| source passage | Quellstelle |
| validation | Validierung |
| machine review | Maschinenprüfung |
| verification, verification role | Verifikation, Verifikationsrolle |
| posit | Posit |

Status values and verdicts (`grounded`, `fully supports`, `overreaches`) stay English as field values. The German page glosses them in parentheses or in the ladder.

## Publication boundary

GitHub Pages builds `docs/` with Jekyll. The page loads no data files and serves no `knowledge/` material, and the reading list links into the repository on GitHub instead. `_config.yml` excludes the field report and this document. The example is invented.

## Evidence

On 2026-11-04 three model readers (separate subagents in the roles of a historian, a quality officer in public administration reading German on a phone, and a data librarian before a workshop) and one UI reviewer against the vault's interface yardstick judged screenshots and page text. They are models, not people.

- All three retold the trace correctly and understood that only a person sets `verified`.
- The librarian found that the first example's February minutes only announced the reopening, so the report sentence overreached its source while the page showed “fully supports”. The source became April minutes, and the overreach became the review step's counter-example.
- Two readers could not tell assertion from distillate. The assertion caption now says that a distillate belongs to a source and an assertion to the matter.
- The readers stopped at cloning, uv and step 5 of the start section. The section now names the terminal, links GitHub Desktop and the uv installer, and says where `verdicts.jsonl` comes from and where `verified` is written.
- The reviewer found moving controls, too short autoplay, struck-through statuses and a caption far from its layer on phones. These were changed as described above.

Still open from these readings are time and cost per source, and a human reading and the operator's acceptance.

## Decisions

- 2026-11-04: the hand-written method page replaced the page generated by `tools/build_docs.py`, and the generator was removed. See `docs/decisions.md`.
- 2026-11-04: the layer paths and anchor codes stay visible in the example, although two model readers called them noise, because they show what the method is made of. The operator decided this.
