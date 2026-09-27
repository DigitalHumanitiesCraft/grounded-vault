---
title: Operations
project:
  name: "{{PROJECT_NAME}}"
  repository: "{{REPOSITORY}}"
method:
  name: Promptotyping
  url: https://dhcraft.org/Promptotyping/
status: draft
language: en
created: "{{DATE}}"
updated: "{{DATE}}"
related: [schema, state, journal]
---

# Operations

This document defines the procedures of the vault, one section per chain. Every chain produces or checks artifacts defined in [[knowledge/schema]] and updates the registers in [[knowledge/state]]. Decisions made along the way go to [[knowledge/journal]].

## Production order

The first production cycle runs vertically. One source is carried through every chain below, from acquisition to a written paragraph of a chapter, and validated after each step, before a second source is touched. The tempting order is the horizontal one, converting every original first and then writing every distillate, because each step feels cheaper when repeated. That order produces nothing checkable until the last layer is reached, and a defect in the anchor mechanics then sits in every file at once instead of in one. Agents left to themselves choose it, so the rule has to be explicit.

## Acquire

How a source enters the vault is orthogonal to its type; the channel is recorded in the `channel` field of the Markdown representation and changes nothing about checking.

- **handover** and **collection**: place the original in `00_sources/`.
- **import**: export records from the reference library as CSL JSON into `references/`, one file per batch of records.
- **deep-research**: run the research prompt below. Capture every located publication in the reference manager and export it as CSL JSON into `references/`. The research report itself never becomes a source; all anchors bind to the located publications.

Originals in `00_sources/` stay out of version control by default, because third-party rights usually forbid redistribution. An original whose rights the project holds is committed by force-adding it past `.gitignore`.

### Deep research prompt skeleton

> Research the topic **{topic from the controlled topic set}** for the project **{project}**.
> Search broadly, then prioritize: peer-reviewed and official sources first;
> exclude: {project exclusion list}. Evaluate candidates at full text.
> Counter-check adversarially: for each candidate finding, search for sources
> that contradict it. Deliver a list of publications with full bibliographic
> data and, per publication, the two or three passages that matter for the
> topic, quoted verbatim. Do not deliver synthesis; the vault synthesizes.

## Ingest

Per source, produce the Markdown representation. The operation is the **Markdown conversion**, and it runs in two steps. The first step converts the original into structure-preserving Markdown, so that headings, lists, tables and paragraph boundaries survive as the original had them. The second step stamps a block ID onto every anchor-relevant paragraph. After the second step the file is never edited again, because every later layer anchors into these blocks and an edit would move them.

Which converter performs the first step is decided per source, along this list. The chosen converter is recorded in the `converter` field of the Markdown representation as before, so that a later run can be reproduced or repeated with a different tool.

- Short, simply structured texts are converted by the agent itself, because a tool adds nothing where the structure is already flat.
- Standard office and PDF formats go through MarkItDown or pandoc.
- Complex layouts and scanned documents go through Docling, which works markedly faster when a GPU is available.
- Image sources that require OCR are a named extension point of this profile and are not yet worked out.

1. **document**: run the Markdown conversion into `10_markdown/documents/`, note the converter in the frontmatter, set the H1 from the original, fill the metadata block.
2. **data**: place the data file in `10_markdown/data/`, write the schema description of the same slug, fill the metadata block.
3. **publication**: no Markdown representation, because the CSL JSON record in `references/` is the root of this source type.

Then run `python tools/inventory.py . --write`, which rewrites the source inventory in [[knowledge/state]] from the real file state.

## Distill

One distillate per source, produced as a three-stage chain:

1. **Extraction**: an LLM extracts the core statements with the canonical prompt (one statement per anchor, no evaluation, no cross-source merging).
2. **Formatting**: deterministic pass that enforces the section skeleton, statement IDs and anchor syntax from [[knowledge/schema]].
3. **Fidelity check**: compare each statement against its anchor; for publications run the quotation check now, while the source text is at hand, record it as `checked.quote` and name the text version it ran on in `checked-against`.

### Canonical extraction prompt skeleton

> Extract the core statements of the source **{source short title}**, and of this
> source alone. Work only from the text given below.
> One statement per anchor. Each statement stands on its own, is understandable
> without its neighbours, and stays within the literal sense of the source.
> Do not evaluate, do not interpret, do not infer, and do not merge this source
> with any other; the vault synthesizes at a later layer.
> No statement without a nameable source location. Where you cannot name one,
> drop the statement.
> Deliver per statement the statement itself and its source location, in the form
> the source type requires: for a document the block it was taken from, for a
> publication the verbatim quotation with page, for data the computation that
> yields the stated result.
>
> SOURCE: {Markdown representation, quotation set, or data schema description}

The chain iterates. A statement that fails the fidelity check is reformulated or discarded, and the check runs again, until every remaining statement passes.

Extraction is judged in both directions. The fidelity check asks whether every statement has its passage. The coverage figure in the source inventory asks whether the passages were used, and `W-COVERAGE` names a source whose blocks the distillate mostly leaves unanchored. Such a finding is answered by extending the distillate, or by a journal entry stating why the rest of the source is out of scope for this vault.

Where the source is to be judged as well as reproduced, the appraisal is written after the chain has run, so that no evaluation can leak into the extraction the chain checks. It goes into the optional Appraisal section defined in [[knowledge/schema]] and stays outside the fidelity check, which has nothing to compare it against.

The distillate enters at `status: grounded`. Run `python tools/inventory.py . --write` again, so that the source inventory in [[knowledge/state]] carries the new file state.

## Build assertions

Assertions are where the vault synthesizes, one file per assertion, and the work proceeds by topic in these steps.

1. **Read in**: enter through the topic map of the topic and read every distillate registered there, so that synthesis covers the sources the topic actually holds rather than the ones at hand.
2. **Group**: gather the distillate statements that concern the same matter, across sources and across source types. A group is the unit an assertion is written from.
3. **Formulate**: write one atomic assertion per group, carried jointly by the sources of that group. Atomic means one statement that cannot be split without losing its point.
4. **Ground**: list in `grounding` every statement ID that supports the assertion, one per supporting source, and say in the Support section what each anchor contributes.
5. **Contradictions**: where a group holds statements that cannot be reconciled, write two assertions instead of one, set both to `contested`, and link them to each other in `contested-with` on both sides.
6. **Posit candidates**: a conclusion that no distillate statement carries is noted for the output as a posit candidate and never becomes an assertion. The appraisal sections of the distillates are read at this step as posit candidates, never as support, because they hold the vault's judgment of a source rather than its content.
7. **Register**: enter every assertion in its topic map with a half-sentence of orientation, and record questions the sources leave open under the map's open questions.

Machine review then runs over every pair of assertion and supporting statement, under the contract below. A verdict below *fully supports* means the assertion is reformulated to the width its sources actually carry, or the grounding is corrected by dropping the anchor that does not carry it and naming one that does. Review repeats on the changed pair.

### Assertion review prompt skeleton

> You are an adversarial reviewer. Below are a distillate statement and an
> assertion that claims to be supported by it. Your task is to refute the
> assertion. Judge only whether this statement supports this assertion; whether
> the assertion is true is out of scope. Answer with exactly one verdict: fully supports
> | partially supports | overreaches | contradicts | not in the text. Then give
> one sentence of justification, and where the verdict is not *fully supports*,
> name the part of the assertion that the statement does not carry.
>
> STATEMENT: {distillate statement, without its own grounding anchor}
> ASSERTION: {assertion as one sentence}

## Write chapters

Write per chapter, in the working language and style sheet set in [[knowledge/specification]]. Every load-bearing sentence gets a footnote `Grounded in [[assertion]]`; every own conclusion gets a footnote `Posit: <rationale>. Open evidence question: <question>`. Mirror the referenced assertions and the posit count in the frontmatter. Update the chapter register in [[knowledge/state]].

A chapter that reports the state of research across the sources of a topic is written with the same means and needs no type of its own. Enter through the topic map, and let the three parts fall on the mechanics that already carry them. What the sources agree on becomes sentences grounded in the assertions of the topic. What they disagree on becomes sentences grounded in both sides of a contested pair, which is why taking one side alone raises `W-CONTESTED`. The gap that the vault's own work closes carries no source and becomes a posit footnote with its open evidence question; the topic map's open questions are the register such a gap is read off. A synthesis chapter that later feeds another chapter stays an ordinary row in the chapter register.

## Query

To answer a question from the vault, enter through the topic maps, follow assertions to their distillate statements and, where exactness matters, down to the source passage. Quote assertions by wikilink so the answer stays anchored. Questions the vault cannot answer are recorded as open questions in the topic's map.

## Check

Three instances check the vault. The architecture fixes their contracts; the mechanism fulfilling each contract is an instantiation decision recorded in [[knowledge/specification]].

### Contract: validation

- Judges: formal conformance of every file against [[knowledge/schema]].
- Authority: gates everything; no other check runs on a file that fails validation. Sets no status by itself except enforcing the discipline.
- Conditions: deterministic, same input, same verdict. Runs on every change.
- Record: `checked.validation: <date>` on every file that passes. `tools/validate.py` reports and writes no file, so the agent sets the date after a clean run.
- Reference mechanism: `python tools/validate.py .`, with the finding codes listed in the table below. Data anchors are re-run by default, and the output of each computation is compared with its stated result after surrounding whitespace is trimmed. `--no-computations` switches the re-run off for a fast run. A computation script is executed only from `tools/analysis/`, because the validator executes whatever the vault names. `--min-coverage` sets the share of blocks below which a source counts as unexhausted. The default is half, and an instance that decides otherwise records its value in [[knowledge/specification]] and passes it in its harness rules.
- Chapter scope: `python tools/validate.py . --chapter 40_output/<slug>` judges one chapter and, transitively, the assertions, distillates and Markdown representations it grounds in, so that a chapter can be reported ready while other parts of the vault are still in progress. The scope walk follows only anchors pointing one layer down, so a neighbouring branch of the vault stays out of the verdict. The vault-level warnings stay out too, because they are decidable only over the whole vault, and the run names them in its closing lines. In this mode any warning inside the scope fails the run alongside an error, because the question the run answers is whether this chapter is ready for acceptance.
- A run without errors is not by itself the success criterion. Every warning is printed, counted and to be acted on; a warning names either a check that found no subject or a defect the schema does not make an error, and both are the failure modes a silent green run hides. Over the whole vault a warning never changes the exit code, so that work in progress stays runnable. In chapter mode a warning fails the run, because there the run decides acceptance.

The finding codes of the reference mechanism are these.

| Code | Level | Fires when | Scope |
|---|---|---|---|
| `E-FRONTMATTER` | error | The frontmatter of a content file is missing, unterminated, not valid YAML or not a mapping, names an unknown type, lacks a required field of its type, sits outside the folder of its type, holds a `status`, `source-type` or `channel` value outside its vocabulary, or gives a link field (`representation`, `data`, `superseded-by`, `contested-with`, `grounding`, `assertions`, `topics`) other than as quoted wikilinks. A document representation also fails without `source` or `converter`, a data representation without `data`, a representation whose `metadata` is not a mapping, and any representation of the source type `publication`. A publication distillate fails without `reference`, any other distillate without `representation`. | vault and chapter |
| `E-ANCHOR` | error | An anchor does not resolve, whether in the body or in the frontmatter link fields `representation`, `data`, `superseded-by`, `contested-with`, `grounding` and `assertions`. Links into `00_sources/` are exempt. It also fires for a grounding entry without a statement ID and for a publication `reference` that no record in `references/` carries. | vault and chapter |
| `E-LAYER` | error | An anchor skips a layer instead of binding to the layer directly beneath its own, meaning a distillate's `representation` or statement anchor outside `10_markdown/`, a grounding outside `20_distillates/`, or a `Grounded in` footnote target outside `30_assertions/`. | vault and chapter |
| `E-DUPLICATE` | error | A block ID in a representation or a statement ID in the core statements of a distillate occurs more than once in the file. | vault and chapter |
| `E-STATEMENT` | error | A distillate has no core statements, mints an ID outside its Core statements section, or has a core statement without statement ID. A document statement carries other than exactly one block anchor or anchors into a representation other than the distillate's own, a publication statement lacks a quotation block in the form `"<verbatim>" (<identifier>)`, or a data statement declares no computation. | vault and chapter |
| `E-QUOTE` | error | A publication distillate records no `checked.quote`. | vault and chapter |
| `E-COMPUTATION` | error | A declared computation names no script, passes arguments after the script, names a script path that does not resolve into `tools/analysis/`, or names a script that does not exist. While computations run, it also fires when the script fails, exceeds its timeout or prints a result that differs from the stated one. | vault and chapter |
| `E-TOPIC` | error | A distillate or an assertion names a topic in `topics` for which no topic map exists. | vault and chapter |
| `E-GROUNDING` | error | A document that owes grounding, an assertion, carries an empty `grounding`. | vault and chapter |
| `E-CONTESTED` | error | An assertion at status `contested` has no `contested-with` link, or a counterpart named there does not exist, is not itself `contested` or does not link back. | vault and chapter |
| `E-FOOTNOTE` | error | A chapter footnote is used but never defined or defined but never used, starts with neither `Grounded in` nor `Posit:`, or is a `Grounded in` footnote that names no assertion or targets a document that is not an assertion. | vault and chapter |
| `E-MIRROR` | error | The `assertions` field of a chapter differs from the set of assertions its `Grounded in` footnotes name, or `posits` differs from the number of posit footnotes. | vault and chapter |
| `E-ORPHAN` | error | An assertion is registered in no topic map. | vault and chapter |
| `E-STATUS` | error | A status lacks a check its rung requires, `checked` is not a map, or an entry of `checked` records no date in strict ISO form. | vault and chapter |
| `E-LADDER` | error | An assertion or a chapter stands higher on the status ladder than an anchor it rests on, against the rule that a status is the minimum of the states of its anchors. | vault and chapter |
| `E-SCOPE` | error | `--chapter` names no chapter document. | chapter only |
| `W-PLACEHOLDER` | warning | An unreplaced template placeholder in double braces remains in a content folder, in `knowledge/`, in `CLAUDE.md` or in `HOME.md`. | vault, and in chapter mode the files of the scope |
| `W-VERSION` | warning | A publication distillate records `checked.quote` without naming in `checked-against` the text version the check ran on. | vault and chapter |
| `W-STALE` | warning | The `updated` date of a document is later than the latest of its `checked` dates. A document without any check date does not fire. | vault and chapter |
| `W-DUPLICATE-GROUNDING` | warning | Two assertions carry the same grounding set, or the grounding set of one contains that of the other. | vault, and in chapter mode the assertions of the scope |
| `W-CONTESTED` | warning | A chapter grounds in a contested assertion without grounding in any of its counterparts. | vault and chapter |
| `W-ALIAS` | warning | The alias of a `Grounded in` footnote wikilink differs from the H1 title of the assertion it points to. | vault and chapter |
| `W-UNANCHORED` | warning | A paragraph of a chapter, headings and footnote definitions aside, carries no footnote marker. | vault and chapter |
| `W-COVERAGE` | warning | A document representation that has a distillate carries a smaller share of anchored blocks than `--min-coverage` sets. | vault only |
| `W-EMPTY` | warning | The production chain from `10_markdown` to `40_output` holds no document apart from topic maps, so no content check had a subject. | vault only |
| `W-NO-OUTPUT` | warning | The vault holds no chapter document. | vault only |

### Contract: machine review

- Judges: whether a source location actually supports the statement built on it, per pair, with the fixed verdict vocabulary: **fully supports** | **partially supports** | **overreaches** | **contradicts** | **not in the text**. Only *fully supports* passes.
- Authority: together with validation lifts a document to `validated`, never higher.
- Conditions: anti-anchoring is mandatory. The reviewer sees only the source location and the statement; the producing agent's reasoning stays hidden. A reviewer from a different model family than the producer decorrelates error modes and is recommended.
- Record: `checked.machine-review: <date>`; verdicts below *fully supports* trigger rework and are noted in the journal when they reveal a systematic pattern.
- Reference mechanism: `python tools/review.py` with the subcommands `stats`, `emit`, `judge` and `run`. `stats` counts the pairs, `emit` writes one prompt per pair as a JSONL batch, and `judge` reads the verdicts back and, with `--apply`, books `checked.machine-review` on every document whose pairs all came back *fully supports*. `run` judges each pair through the local `claude -p` command line, which in the Claude Code harness calls a model of the producer's own family, so a reviewer from another family goes through `emit` and `judge`.
- Reference prompt skeleton:

  > You are an adversarial reviewer. Below are a source passage and a statement
  > that claims to be supported by it. Your task is to refute the statement.
  > Judge only whether this passage supports this statement. Answer with exactly
  > one verdict: fully supports | partially supports | overreaches | contradicts
  > | not in the text. Then give one sentence of justification.
  >
  > PASSAGE: {source location, with its heading path}
  > STATEMENT: {statement}

- Pair cutting: a pair consists of the anchored location (for documents the block plus its heading path, for publications the quotation, for data the computation and its result) and the bare statement. Nothing else enters the pair.
- Displaced subject: where the passage supports the statement while its subject is not the matter the assertion is about, the reviewer adds one line naming the displacement. In **self-report** the source speaks about itself, about its own priority, reach or achievement; the verdict stays *fully supports* when the statement reports the claim as the source's own, and it is *overreaches* when the statement asserts the matter the claim is about. In **state report** the source shows the matter in one state at one time, such as a restored object, a dated inventory or a plan; the verdict stays *fully supports* when the statement names that state with its date, and it is *overreaches* when the statement asserts the property of the matter as such. These are the cases the coverage relation cannot separate on its own.

### Contract: verification

- Judges: whether a grounding relation holds as evidence, by human expert judgment. The authority is the verification role named in [[knowledge/specification]].
- Authority: alone lifts to `verified`. Machine checks prepare, never replace it.
- Conditions: proceeds passage by passage on the prepared pairs; may sample where the machine review pass rate justifies it, with the sampling rule noted in the journal.
- Record: `checked.verification: <date>` set by or on behalf of the verifying role.

### Status discipline

`grounded` → (validation and machine review passed) → `validated` → (expert passed) → `verified`. `contested` is set by assertion building or review when sources conflict, and resolved only by verification. A document's status is the minimum of its anchors' states.
