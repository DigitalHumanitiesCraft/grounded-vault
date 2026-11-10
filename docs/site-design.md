# Site design

The public page `docs/index.html` explains Grounded Vault to readers without prior knowledge of Git, Obsidian or coding agents, in English by default and in German with `?lang=de`. A reader should be able to say what a vault is and how a statement stays checkable, read off the figure which layer anchors into which and which check covers what, start a vault, and run the worked example. The page follows the shared page structure of the DHCraft method sites and the owner's decisions of 2026-11-10, both in `brand-assets/web/design.md`, with the Promptotyping start page as the reference for layout and look.

## Parts

| Part | Question it answers | Form |
|---|---|---|
| Title and abstract | What is it and for whom? | Name and three sentences, no button row |
| Main figure | Which layers, anchors, checks and statuses exist? | `images/grounded-vault-provenance-chain.svg` directly under the abstract, then three paragraphs of prose that define its terms in sentences with links into `knowledge/index.md` |
| Origin | Where does it come from and what is cited? | One paragraph, Promptotyping profile and lineage after `docs/concept.md` |
| Reuse | How do I start a vault? | Four numbered steps with commands and prompts, then the download block |
| Example | How does one source travel through every layer? | Ten numbered steps on the public PROV-DM example, each with its prompt or command and a result line naming the file it yields |
| Limits, licence and citation | What does it not establish, under which terms, how to cite? | Five list items, one licence paragraph, the citation from `CITATION.cff` |

## Figure

The figure is a standalone SVG of 1600 by 900 with fixed light colours and its own paper ground, so it serves the page, papers and slides unchanged. `images/grounded-vault-provenance-chain.png` is its rendering for slides. The page embeds it as an image, in which the browser does not load the SVG's web fonts, so on the page it is set in the system sans serif while the PNG shows Sora and Instrument Sans. Below 56rem the figure scrolls sideways inside its frame so that its text stays legible.

- The left column holds the five layers from output down to sources, each with its folder, and the anchor between each pair of layers with its notation. The posit stands beside the output as a dashed box.
- The right column holds the three checks as bands over the layers they cover. Validation and verification span output to Markdown representations, machine review spans assertions to Markdown representations. Validation reaches originals only through the optional manifest.
- The status ladder stands below the checks, with `contested` and `superseded` named beside it.
- The three checks carry three of the four hues of the mark, validation blue, machine review orange and verification green, always with their label. The same hues underline the check names in the prose. Purple stays the accent for actions, and anchors are drawn in ink.

## Example

The example uses the committed public example `examples/prov-entity/`, a selected excerpt of the W3C PROV-DM Recommendation, because the repository holds no other complete example on public or invented material. The prompts route into `SETUP.md` and the sections of `knowledge/operations.md` that `CLAUDE.md` names, and each result line names the committed file the step yields. The repository does not record the prompts with which the committed example was produced, so the prompts on the page are a reconstruction from the procedures, read against `CLAUDE.md`, `SETUP.md`, `knowledge/operations.md` and `tools/review.py`, and not yet run end to end by an agent in a fresh copy.

## Visual system

Tokens, fonts, mark, header, footer, buttons and code blocks come from the shared DHCraft files in `assets/dhcraft/`, copied unchanged from `brand-assets/web` at commit `32565e2`. The page opens light whatever the system setting, and the toggle in the header switches to dark and stores the choice. The header carries the four hues of the mark as a hairline. Prompts are set in the text face on a white card and wrap, commands stay monospace and scroll sideways. Steps carry a circled number.

## Terms

| English | German |
|---|---|
| assertion | Assertion |
| distillate | Destillat |
| Markdown representation | Markdown-Fassung |
| core statement | Kernaussage |
| source passage | Quellstelle |
| machine-resolvable | maschinell auflösbar |
| validation | Validierung |
| machine review | Maschinenprüfung |
| verification, verification role | Verifikation, Verifikationsrolle |
| evidence | Beleg |
| posit | Posit |

Status values, verdicts, prompts, commands and file names stay English, carry `lang="en"` and are not translated.

## Publication boundary

GitHub Pages builds `docs/` with Jekyll. `_config.yml` excludes the field report, this document and the decision record, so the delivered set is `index.html`, `page.js`, `site.css`, `concept.md`, `assets/` and `images/`. The page loads no data files and serves no `knowledge/` material. The archive download is GitHub's archive of the repository.

## Evidence

On 2026-11-10 the page was checked with headless Chromium at 1440 and 1600 pixels, at 375 and 320 pixels in both languages, at 720 by 450 for 200 percent zoom, with a dark system setting, which leaves the page light, and without JavaScript, where the English page is complete and only the language link, the toggle and the copy buttons are absent. No viewport scrolls the page sideways. A Jekyll build delivered the paths named above. A separate model reviewer read the page against the canonical documents, and its findings on the chapter's status record, the split of the review commands, the reviewer folder outside the repository, the coverage of verification, unsupported limit statements and the German term for resolvable were worked in.

Still open are a run of the example prompts by an agent in a fresh copy, a real screen reader and touch input, a human reading and the owner's acceptance.

## Decisions

- 2026-11-04: the hand-written method page replaced the page generated by `tools/build_docs.py`, and the generator was removed. See `docs/decisions.md`.
- 2026-11-04: the layer paths and anchor codes stay visible in the example, although two model readers called them noise, because they show what the method is made of. The operator decided this.
- 2026-11-10: the page follows the seven-part structure and the review decisions of the DHCraft method sites. The playable trace on an invented city archive and the generated text module are removed, and the example moves to the committed PROV-DM example. See `docs/decisions.md`.
