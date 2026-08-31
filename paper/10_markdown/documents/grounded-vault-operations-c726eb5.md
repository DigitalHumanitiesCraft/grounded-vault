---
type: representation
source-type: document
source: "[[00_sources/grounded-vault-knowledge-operations-c726eb5.md]]"
converter: "none; the original is Markdown, the agent selected the representation and stamped the block IDs"
channel: collection
metadata:
  title: "Grounded Vault, knowledge/operations.md, the procedure document of the profile this vault instantiates"
  creator: "Digital Humanities Craft; Christopher Pollin, Department of Digital Humanities, University of Graz (vault operator)"
  date: "2026-08-10"
  format: "markdown"
  identifier: "https://github.com/DigitalHumanitiesCraft/grounded-vault, knowledge/operations.md at commit c726eb53445f69f4d33a80fb7c986a89b222fd05 of 2026-08-10"
  license: "CC-BY-4.0"
  confidential: false
created: 2026-08-10
updated: 2026-08-10
---

# Operations

Scope: the full body of `knowledge/operations.md` of the Grounded Vault template repository, taken at commit `c726eb5` of 2026-08-10. The Promptotyping header of the original, a YAML block of project, method and status fields with unreplaced template placeholders, is not represented here; everything from the H1 onwards is. Wikilink brackets of the original appear escaped as `\[\[` and `\]\]`, because this vault would otherwise read the cross-references of the template as anchors of its own. No word of the text is changed.

This document defines the procedures of the vault, one section per chain. Every chain produces or checks artifacts defined in \[\[knowledge/schema\]\] and updates the registers in \[\[knowledge/state\]\]. Decisions made along the way go to \[\[knowledge/journal\]\]. ^ops01

## Acquire

How a source enters the vault is orthogonal to its type; the channel is recorded in the `channel` field of the Markdown representation and changes nothing about checking. ^ops02

- **handover** and **collection**: place the original in `00_sources/`. ^ops03
- **import**: export records from the reference library as CSL JSON into `references/`, one file per batch of records. ^ops04
- **deep-research**: run the research prompt below. Capture every located publication in the reference manager and export it as CSL JSON into `references/`. The research report itself never becomes a source; all anchors bind to the located publications. ^ops05

### Deep research prompt skeleton

> Research the topic **{topic from the controlled topic set}** for the project **{project}**.
> Search broadly, then prioritize: peer-reviewed and official sources first;
> exclude: {project exclusion list}. Evaluate candidates at full text.
> Counter-check adversarially: for each candidate finding, search for sources
> that contradict it. Deliver a list of publications with full bibliographic
> data and, per publication, the two or three passages that matter for the
> topic, quoted verbatim. Do not deliver synthesis; the vault synthesizes.

^ops06

## Ingest

Per source, produce the Markdown representation. The operation is the **Markdown conversion**, and it runs in two steps. The first step converts the original into structure-preserving Markdown, so that headings, lists, tables and paragraph boundaries survive as the original had them. The second step stamps a block ID onto every anchor-relevant paragraph. After the second step the file is never edited again, because every later layer anchors into these blocks and an edit would move them. ^ops07

Which converter performs the first step is decided per source, along this list. The chosen converter is recorded in the `converter` field of the Markdown representation as before, so that a later run can be reproduced or repeated with a different tool. ^ops08

- Short, simply structured texts are converted by the agent itself, because a tool adds nothing where the structure is already flat. ^ops09
- Standard office and PDF formats go through MarkItDown or pandoc. ^ops10
- Complex layouts and scanned documents go through Docling, which works markedly faster when a GPU is available. ^ops11
- Image sources that require OCR are a named extension point of this profile and are not yet worked out. ^ops12

1. **document**: run the Markdown conversion into `10_markdown/documents/`, note the converter in the frontmatter, set the H1 from the original, fill the metadata block. ^ops13
2. **data**: place the data file in `10_markdown/data/`, write the schema description of the same slug, fill the metadata block. ^ops14
3. **publication**: no Markdown representation, because the CSL JSON record in `references/` is the root of this source type. ^ops15

Then run `python tools/inventory.py . --write`, which rewrites the source inventory in \[\[knowledge/state\]\] from the real file state. ^ops16

## Distill

One distillate per source, produced as a three-stage chain: ^ops17

1. **Extraction**: an LLM extracts the core statements with the canonical prompt (one statement per anchor, no evaluation, no cross-source merging). ^ops18
2. **Formatting**: deterministic pass that enforces the section skeleton, statement IDs and anchor syntax from \[\[knowledge/schema\]\]. ^ops19
3. **Fidelity check**: compare each statement against its anchor; for publications run the quotation check now, while the source text is at hand, and record it as `checked.quote`. ^ops20

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

^ops21

The chain iterates. A statement that fails the fidelity check is reformulated or discarded, and the check runs again, until every remaining statement passes. ^ops22

Where the source is to be judged as well as reproduced, the appraisal is written after the chain has run, so that no evaluation can leak into the extraction the chain checks. It goes into the optional Appraisal section defined in \[\[knowledge/schema\]\] and stays outside the fidelity check, which has nothing to compare it against. ^ops23

The distillate enters at `status: grounded`. Run `python tools/inventory.py . --write` again, so that the source inventory in \[\[knowledge/state\]\] carries the new file state. ^ops24

## Build assertions

Assertions are where the vault synthesizes, one file per assertion, and the work proceeds by topic in these steps. ^ops25

1. **Read in**: enter through the topic map of the topic and read every distillate registered there, so that synthesis covers the sources the topic actually holds rather than the ones at hand. ^ops26
2. **Group**: gather the distillate statements that concern the same matter, across sources and across source types. A group is the unit an assertion is written from. ^ops27
3. **Formulate**: write one atomic assertion per group, carried jointly by the sources of that group. Atomic means one statement that cannot be split without losing its point. ^ops28
4. **Ground**: list in `grounding` every statement ID that supports the assertion, one per supporting source, and say in the Support section what each anchor contributes. ^ops29
5. **Contradictions**: where a group holds statements that cannot be reconciled, write two assertions instead of one, set both to `contested`, and link them to each other in `contested-with` on both sides. ^ops30
6. **Posit candidates**: a conclusion that no distillate statement carries is noted for the output as a posit candidate and never becomes an assertion. The appraisal sections of the distillates are read at this step as posit candidates, never as support, because they hold the vault's judgment of a source rather than its content. ^ops31
7. **Register**: enter every assertion in its topic map with a half-sentence of orientation, and record questions the sources leave open under the map's open questions. ^ops32

Machine review then runs over every pair of assertion and supporting statement, under the contract below. A verdict below *fully supports* means the assertion is reformulated to the width its sources actually carry, or the grounding is corrected by dropping the anchor that does not carry it and naming one that does. Review repeats on the changed pair. ^ops33

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

^ops34

## Write chapters

Write per chapter, in the working language and style sheet set in \[\[knowledge/specification\]\]. Every load-bearing sentence gets a footnote `Grounded in \[\[assertion\]\]`; every own conclusion gets a footnote `Posit: <rationale>. Open evidence question: <question>`. Mirror the referenced assertions and the posit count in the frontmatter. Update the chapter register in \[\[knowledge/state\]\]. ^ops35

A chapter that reports the state of research across the sources of a topic is written with the same means and needs no type of its own. Enter through the topic map, and let the three parts fall on the mechanics that already carry them. What the sources agree on becomes sentences grounded in the assertions of the topic. What they disagree on becomes sentences grounded in both sides of a contested pair, which is why taking one side alone raises `W-CONTESTED`. The gap that the vault's own work closes carries no source and becomes a posit footnote with its open evidence question; the topic map's open questions are the register such a gap is read off. A synthesis chapter that later feeds another chapter stays an ordinary row in the chapter register. ^ops36

## Query

To answer a question from the vault, enter through the topic maps, follow assertions to their distillate statements and, where exactness matters, down to the source passage. Quote assertions by wikilink so the answer stays anchored. Questions the vault cannot answer are recorded as open questions in the topic's map. ^ops37

## Check

Three instances check the vault. The architecture fixes their contracts; the mechanism fulfilling each contract is an instantiation decision recorded in \[\[knowledge/specification\]\]. ^ops38

### Contract: validation

- Judges: formal conformance of every file against \[\[knowledge/schema\]\]. ^ops39
- Authority: gates everything; no other check runs on a file that fails validation. Sets no status by itself except enforcing the discipline. ^ops40
- Conditions: deterministic, same input, same verdict. Runs on every change. ^ops41
- Record: `checked.validation: <date>` on every file that passes. ^ops42
- Reference mechanism: `python tools/validate.py .` (checks frontmatter per type, anchor resolution, statement IDs, quotation identity where a source text is available, computation declarations, MOC reachability, bidirectional contested links, chapter mirror and footnote keywords, status discipline). Data anchors are re-run and compared by default; `--no-computations` switches that off for a fast run. ^ops43
- Chapter scope: `python tools/validate.py . --chapter 40_output/<slug>` judges one chapter and, transitively, the assertions, distillates and Markdown representations it grounds in, so that a chapter can be reported ready while other parts of the vault are still in progress. The scope walk follows only anchors pointing one layer down, so a neighbouring branch of the vault stays out of the verdict. The vault-level warnings stay out too, because they are decidable only over the whole vault, and the run names them in its closing lines. In this mode any warning inside the scope fails the run alongside an error, because the question the run answers is whether this chapter is ready for acceptance. ^ops44
- The checks with their own codes are these. `E-ANCHOR` fires when an anchor does not resolve, and it resolves the frontmatter targets `representation`, `superseded-by` and `contested-with` as well as the anchors in the body. `E-LAYER` fires when an anchor skips a layer instead of binding to the layer directly beneath its own. `E-GROUNDING` fires when a document that owes grounding carries an empty grounding. `E-DUPLICATE` fires when a block ID or a statement ID occurs more than once in one file. `E-STATUS` fires when a status lacks a check its rung requires or when an entry of `checked` records no date. `E-LADDER` fires when a document stands higher on the status ladder than an anchor it rests on, the rule that a status is the minimum of the states of its anchors. `W-PLACEHOLDER` fires while an unreplaced template placeholder in double braces remains anywhere in the vault. `W-EMPTY` fires while the production chain from `10_markdown` to `40_output` holds no document, so that no content check had a subject. `W-STALE` fires when a document's `updated` date is younger than the youngest of its `checked` dates, because then its checks are older than the content they judge; a document without any check date does not fire, since that is the state the status ladder starts from. `W-DUPLICATE-GROUNDING` fires when two assertions carry the same grounding set or one grounding set contains the other, the shape an accidentally duplicated assertion has. `W-ALIAS` fires when the alias of a chapter footnote wikilink differs from the H1 title of the assertion it points to, because a shortened alias can silently drop the clause that restricts the assertion. ^ops45
- A run without errors is not by itself the success criterion. Every warning is printed, counted and to be acted on; a warning names either a check that found no subject or a defect the schema does not make an error, and both are the failure modes a silent green run hides. Over the whole vault a warning never changes the exit code, so that work in progress stays runnable. In chapter mode a warning fails the run, because there the run decides acceptance. ^ops46

### Contract: machine review

- Judges: whether a source location actually supports the statement built on it, per pair, with the fixed verdict vocabulary: **fully supports** | **partially supports** | **overreaches** | **contradicts** | **not in the text**. Only *fully supports* passes. ^ops47
- Authority: together with validation lifts a document to `validated`, never higher. ^ops48
- Conditions: anti-anchoring is mandatory. The reviewer sees only the source location and the statement; the producing agent's reasoning stays hidden. A reviewer from a different model family than the producer decorrelates error modes and is recommended. ^ops49
- Record: `checked.machine-review: <date>`; verdicts below *fully supports* trigger rework and are noted in the journal when they reveal a systematic pattern. ^ops50
- Reference prompt skeleton: ^ops51

  > You are an adversarial reviewer. Below are a source passage and a statement
  > that claims to be supported by it. Your task is to refute the statement.
  > Judge only whether this passage supports this statement. Answer with exactly
  > one verdict: fully supports | partially supports | overreaches | contradicts
  > | not in the text. Then give one sentence of justification.
  >
  > PASSAGE: {source location, with its heading path}
  > STATEMENT: {statement}

- Pair cutting: a pair consists of the anchored location (for documents the block plus its heading path, for publications the quotation, for data the computation and its result) and the bare statement. Nothing else enters the pair. ^ops52

### Contract: verification

- Judges: whether a grounding relation holds as evidence, by human expert judgment. The authority is the verification role named in \[\[knowledge/specification\]\]. ^ops53
- Authority: alone lifts to `verified`. Machine checks prepare, never replace it. ^ops54
- Conditions: proceeds passage by passage on the prepared pairs; may sample where the machine review pass rate justifies it, with the sampling rule noted in the journal. ^ops55
- Record: `checked.verification: <date>` set by or on behalf of the verifying role. ^ops56

### Status discipline

`grounded` → (validation and machine review passed) → `validated` → (expert passed) → `verified`. `contested` is set by assertion building or review when sources conflict, and resolved only by verification. A document's status is the minimum of its anchors' states. ^ops57
