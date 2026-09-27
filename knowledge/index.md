---
title: Index
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
related: [specification, schema, operations, state, journal]
---

# Index

Human readers start at [[HOME]], and agents start at `CLAUDE.md`, which routes onto these documents.

## Reading paths

- To understand the project, read [[knowledge/specification]] for purpose and parameters, then [[knowledge/state]] for where work stands.
- To produce or check content, read [[knowledge/schema]] for what a well-formed artifact is and [[knowledge/operations]] for the chain that produces it.
- To understand a past decision, read [[knowledge/journal]], which is append-only with the newest entry last.

## The six project knowledge documents

| Document | Holds | Changes |
|---|---|---|
| [[knowledge/index]] | navigation, terminology | rarely |
| [[knowledge/specification]] | purpose, parameters, settled decisions | on decisions |
| [[knowledge/schema]] | layer model, document types, anchor mechanics, audit trail | rarely, by decision |
| [[knowledge/operations]] | the chains (acquire, ingest, distill, assertions, chapters, query, check) | rarely, by decision |
| [[knowledge/state]] | source inventory, chapter register, everything volatile | constantly |
| [[knowledge/journal]] | decision history | append-only |

A document is split only when its sections develop divergent update rhythms or divergent readers.

## Terminology

Each term of the vault is defined here and nowhere else. [[knowledge/schema]] fixes the form of what these terms name, [[knowledge/operations]] the procedures that produce and check it.

### Documents and layers

#### Knowledge document

A bounded, maintained document that distills fuller material into what a task needs, readable for humans and agents alike, as [Promptotyping](https://dhcraft.org/Promptotyping/) defines it. The vault knows two kinds, the distillate and the project knowledge document, and the bare term is used only where both are meant.

#### Project knowledge document

One of the six documents in `knowledge/`, which describe the vault itself, its terms, parameters, schema, procedures, state and decisions. It rests on no source, carries no anchor and stands outside the content schema.

#### Source

The original file exactly as it arrived, kept untouched so that every later form of its content can be checked against it.

#### Source type

A class of sources defined by its Markdown representation, its distillation operation and its grounding anchor. The source types are `document`, `publication` and `data`.

#### Markdown representation

The uniform Markdown form of a source, produced once by converting the original and given block IDs so that later layers anchor into passages that never change afterwards.

#### Distillate

The source-bound knowledge document, one per source. It condenses what the source says into core statements, each anchored to the source location it was taken from, and holds the source's terms, open questions and optional appraisal beside them. Being bound to a source, it falls under the content schema and its checks.

#### Appraisal

The optional section of a distillate that holds the vault's judgment of the source, such as the standing of its venue, the limits of its method and its relevance. It is a posit, mints no IDs and can therefore never serve as grounding.

#### Assertion

A single source-supported statement synthesized from the distillates of a topic and grounded in at least one distillate statement. Source-supported means that it rests on sources and never on the author alone. It does not mean that the assertion is bound to one source. A core statement reports what its one source says, while an assertion states the matter, so a further source can join its grounding without the assertion changing. One source is enough.

#### Topic map

The file `MOC-<Topic>.md` in `30_assertions/`, one per topic, which registers the assertions of that topic, while each distillate names its topics in its own `topics` field. The set of topic maps is the controlled topic set.

#### Output

The final product of the vault, one or more documents such as a report, proposal, thesis or paper, held as chapters.

#### Chapter

An output text in which every load-bearing sentence carries a footnote to an assertion and every own conclusion is marked as a posit. It is the unit of the output that is checked and accepted on its own.

#### Posit

A conclusion in the output without source support, explicitly marked with its rationale and open evidence question. It differs from an assertion in kind, not in ripeness, and never matures into one.

### Anchors and statements

#### Anchor

A machine-resolvable reference from a statement to the location it rests on, one layer down. Each layer carries its own form, block IDs in the Markdown representation, grounding anchors and statement IDs in the distillate, grounding anchors into distillate statements in the assertion, and footnote anchors into assertions in the chapter.

#### Block ID

The ID (`^a1b2`) minted once at ingest on a passage of a document representation, the target distillate anchors bind to.

#### Core statement

A statement in the Core statements section of a distillate that reproduces its source within the source's literal sense. It carries exactly one grounding anchor, whose form follows the source type, a block reference for a document, a verbatim quotation for a publication and a declared computation for data. Only core statements can support an assertion.

#### Statement ID

The ID (`^s1`) that ends a core statement, minted only in a distillate, the target assertions bind to.

#### Grounding

The anchor relation between a statement and what it rests on one layer down, source locations for a core statement and distillate statements for an assertion. The anchors that carry it are grounding anchors. It is a structural property an agent can produce and says nothing about whether the statement is true.

#### Displaced subject

The case in which a passage supports a statement while its subject is not the matter the assertion is about. Its two named cases are the self-report, in which a source speaks about itself, and the state report, in which a source shows its matter in one state at one time.

#### Provenance chain

The unbroken anchor path from an output sentence through assertions and distillates to source locations. A break anywhere is a defect that validation detects.

### Checking

#### Acquisition channel

The way a source entered the vault, one of `handover`, `collection`, `import` and `deep-research`. It changes nothing about how the source is checked.

#### Fidelity check

The last stage of distillation, which compares every core statement against its anchor. For a publication it includes the quotation check, which confirms each quotation character for character against the source text.

#### Coverage

The share of the blocks of a document representation that some distillate statement anchors. It asks whether the passages were used, the direction the anchor chain itself does not check.

#### Validation

Deterministic conformance checking of every file against the schema, by `tools/validate.py` in the reference implementation. It judges resolvability and form. Together with machine review it lifts a distillate or an assertion to `validated`, and it lifts a chapter there alone, once every assertion the chapter cites stands at `validated`.

#### Machine review

Adversarial checking by a language model under anti-anchoring, the condition that the reviewer sees only the pair and never the producing agent's reasoning, which judges per pair of source location and statement whether the location supports the statement, with one verdict from a fixed vocabulary. Together with validation it lifts a distillate or an assertion to `validated`, never higher.

#### Verification

Human expert review by the verification role named in [[knowledge/specification]]. It alone establishes evidence and sets `verified`.

#### Evidence

A grounding relation that has passed verification. It is relational and deliberately rare. A fresh vault contains grounding, and evidence arises only through review.

#### Status ladder

The sequence `grounded` → `validated` → `verified`, with `contested` for assertions whose sources conflict and `superseded` for replaced distillates beside the ladder. A document's status is the minimum of the states of its anchors. `contested` is set by assertion building or review when sources conflict, and only verification resolves it.

#### Audit trail

The principle that status fields record outcomes of checks that actually ran, each with its date on the checked document.

