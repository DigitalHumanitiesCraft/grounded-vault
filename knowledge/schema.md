---
title: Schema
project:
  name: "{{PROJECT_NAME}}"
  repository: "{{REPOSITORY}}"
method:
  name: Promptotyping
  url: https://dhcraft.org/Promptotyping/
profile:
  name: Grounded Vault
  url: https://github.com/DigitalHumanitiesCraft/grounded-vault
status: draft
language: en
created: "{{DATE}}"
updated: "{{DATE}}"
related: [index, specification, operations, state]
---

# Schema

The rules of the vault cover the layer model, the controlled vocabularies, the anchor mechanics per source type, the audit trail, and for every content document type the exact frontmatter and section skeleton. Every content file, whether produced by agent or human, derives from them. The procedures that produce and check these documents live in [[knowledge/operations]].

## Layer model

| Layer | Folder | Content | Anchor it carries |
|---|---|---|---|
| Sources | `00_sources/` | originals, local only | none, this is the ground |
| Markdown representation | `10_markdown/` | archived full texts, datasets with schema | block IDs, file plus schema |
| Distillates | `20_distillates/` | one distillate per source | grounding anchors into its source, statement IDs |
| Assertions | `30_assertions/` | atomic statements not bound to one source, topic maps | grounding anchors into distillate statements |
| Output | `40_output/` | one file per chapter | footnote anchors into assertions, posits marked |

The source inventory in `knowledge/state.md` lists every Markdown representation and every distillate, and it is generated from the file state by `python tools/inventory.py . --write` rather than maintained by hand, so that no second bookkeeping can drift away from the files. For a document representation it also carries the coverage defined in [[knowledge/index]] § Terminology, and validation raises `W-COVERAGE` where coverage falls below the share an instance sets.

The terms for the layers and their parts are defined once in [[knowledge/index]] § Terminology. The schema fixes the form of what they name.

Two rules constrain the chain. Anchors are minted only at the layer they belong to. A Markdown representation mints block IDs, a distillate mints statement IDs, and no higher layer creates anchors into material below its direct predecessor. Each layer also anchors only into the layer directly beneath it, so the output binds to assertions, assertions bind to distillate statements, and distillates bind to the blocks of the Markdown representation. Links in the Related sections serve navigation and fall outside this rule.

## Controlled vocabularies

- `type` takes one of the values `representation`, `distillate`, `assertion`, `moc`, `glossary` and `chapter`. The value `representation` is the machine-side short form for Markdown representation, and the prose of this vault uses the full term.
- `source-type` takes one of the values `document`, `publication` and `data`.
- `channel` takes one of the values `handover`, `collection`, `import` and `deep-research`.
- `status` takes one of the values `grounded`, `validated` and `verified`, plus `contested` (assertions only) and `superseded` (distillates only).
- Each value of `topics` must name an existing topic map, and the set of `MOC-*.md` files in `30_assertions/` is the controlled topic set.

## Audit trail

A status records the outcome of checks that actually ran. Every check writes its date into the `checked` map of the document it checked:

```yaml
status: validated
checked:
  validation: 2026-07-11
  machine-review: 2026-07-11
```

The discipline is machine-enforced. For a distillate or an assertion, `validated` requires `checked.validation` and `checked.machine-review`. A chapter reaches `validated` with `checked.validation` alone, because machine review pairs the assertions it cites and not its sentences, and the minimum rule below keeps it at `grounded` until each of those assertions stands at `validated`. `verified` additionally requires `checked.verification` for every type. Every entry of the map carries an ISO date, because a record without one cannot be held against the content it judges. `grounded` is the entry status of every freshly produced document and requires no entry. A document's status is the minimum of the states of its anchors, judged against the anchors an assertion names in `grounding` and a chapter in its `assertions` mirror, so one unreviewed anchor keeps the whole document at `grounded`. `contested` and `superseded` lie beside the ladder and earn no rank, so a document resting on one of them stays at `grounded` as well. No instance ever sets a status above its own authority, and the contracts that fix each authority are defined in [[knowledge/operations]].

## Source metadata

Every Markdown representation carries a compact, Dublin-Core-compatible metadata block. Licensing and confidentiality are metadata of the individual source, and nothing else in the architecture depends on them.

```yaml
metadata:
  title: ""            # dc:title
  creator: ""          # dc:creator; role and institution, no third-party personal names
  date: ""             # dc:date of the source, ISO 8601
  format: ""           # dc:format of the original (pdf, pptx, csv, …)
  identifier: ""       # dc:identifier (DOI, URL, archival signature) where one exists
  license: ""          # dc:rights; SPDX identifier or short clause
  confidential: false  # true keeps original and full text local
```

## Source types

The source type of a source follows from whether its content may be stored in the vault and from the anchor that storage decision permits.

A `document` is a source whose full text may be stored in the vault. It is converted into a Markdown representation and anchored by block reference into that representation. A `publication` is a source that is only cited. What lies in the vault is the bibliographic record, and the anchor is the verbatim quotation together with the identifier. A `data` source is a file whose anchor is a deterministic computation over that file. An aggregate or a statistical finding exists at no single passage, so the computation takes the place of one.

The criterion is storability, and the publication status of a source decides nothing by itself, so an open-access article that may be stored is treated as a `document`. Where a full text may be stored, `document` is preferred over `publication`, because its anchors resolve inside the vault.

## Bibliographic records

`references/` holds the bibliographic records of the citable-only sources as CSL JSON, exported from the reference manager. Each file is a JSON array of records, and each record carries an `id` alongside its bibliographic fields.

```json
[
  {
    "id": "author2024keyword",
    "type": "article-journal",
    "title": "",
    "author": [{ "family": "", "given": "" }],
    "issued": { "date-parts": [[2024]] },
    "container-title": "",
    "URL": ""
  }
]
```

The `reference` field of a publication distillate names one such `id`, and validation raises `E-ANCHOR` when no record in `references/` carries it. The folder is needed only while the source type `publication` is active.

## Document types

Each type carries its frontmatter as a code block, followed by the section skeleton where one is fixed. Fields not marked optional are required. Wikilink values are quoted, block IDs unquoted, as Obsidian requires for YAML.

### 1. Markdown representation (`source-type: document`)

Exactly one per source, stored in `10_markdown/documents/`. A revised source enters as a new file with a date-suffixed slug, and existing anchors keep resolving against the old file.

```yaml
---
type: representation
source-type: document
source: "[[00_sources/<filename>]]"
converter: ""            # e.g. Docling, MarkItDown
channel: handover        # handover | collection | import | deep-research
metadata: { … }          # see Source metadata
created: 2026-01-01
updated: 2026-01-01
---
```

The body is the converted full text under an H1 taken from the original. Every anchor-relevant paragraph ends with a block ID:

```markdown
The board approves centrally operated services. ^a1b2
```

Block IDs are short, stable, unique per file, and minted only here.

### 2. Markdown representation (`source-type: data`)

A dataset plus its schema description. The data file (CSV, XML, …) lives in `10_markdown/data/` next to a Markdown file of the same slug that carries the frontmatter and describes the schema.

```yaml
---
type: representation
source-type: data
source: "[[00_sources/<filename>]]"    # omit when the data file is the original
data: "[[10_markdown/data/<file.csv>]]"
channel: handover
metadata: { … }
created: 2026-01-01
updated: 2026-01-01
---
```

The body describes columns, units, encodings and known limitations. The anchor of this type is a computation, defined in the distillate.

### 3. Distillate

One file per source in `20_distillates/<source-type>s/`, same slug as its Markdown representation. The core statements reproduce their source without merging it with other sources. Synthesis belongs to assertions, and judging the source belongs to the Appraisal section defined below.

```yaml
---
type: distillate
source-type: document        # document | publication | data
representation: "[[10_markdown/documents/<slug>]]"   # document and data types
reference: ""                # publication type: CSL JSON id from references/
topics: ["[[<Topic>]]"]
status: grounded             # grounded | validated | verified | superseded
checked: {}
checked-against: ""          # publication type: the text version checked.quote ran on
channel: import              # publication type, optional: import | deep-research
superseded-by: ""            # optional, wikilink to the successor distillate
created: 2026-01-01
updated: 2026-01-01
---
```

```markdown
# Distillate: <source short title>

<Lead: one sentence naming the source and its contribution to the vault.>

## Core statements

- <statement> [[10_markdown/documents/<slug>#^a1b2]] ^s1
- <statement> [[10_markdown/documents/<slug>#^c3d4]] ^s2

## Terms

- **<term>**: <meaning as set by the source> [[10_markdown/documents/<slug>#^e5f6]]

## Open questions

- <unclarity of the source>

## Appraisal

<optional; what this source is worth, in prose>

## Related

- [[20_distillates/…]] / [[30_assertions/…]]
```

Every core statement carries exactly one grounding anchor into its source and ends with a statement ID (`^s1`, `^s2`, …), the anchor assertions bind to. The anchor form varies by source type:

- For a `document`, the anchor is a block reference into the Markdown representation, as above.
- For a `publication`, the anchor is a verbatim quotation with citation instead of a block reference. The quotation must appear character for character in the source. The intake-time check is recorded as `checked.quote`, and `checked-against` names the text version that check ran on, such as a preprint version, a publisher PDF or a page revision with its date. A publication has no representation in the vault, so nothing else records which text the quotations follow, and a record that later points to another version ages the quotations without moving any date. Validation raises `W-VERSION` while the field is missing.

  ```markdown
  - <statement in own words> ^s1
    > "<verbatim quotation>" (<identifier>, p. <n>)
  ```

  The quotation block opens with the verbatim text in quotation marks and closes with the identifier and locator in parentheses. It may run over several `>` lines, and validation reads it as one block against that form.

- For `data`, the anchor is a reproducible computation instead of a block reference, named on an indented line. The script lives in `tools/analysis/` and is deterministic.

  ```markdown
  - <statement, e.g. an aggregate or finding> ^s1
    - computation: `python tools/analysis/<script>.py` → `<stated result>`
  ```

  The script reads the data file of the Markdown representation, takes no arguments, and prints the stated result and nothing else to standard output. Validation re-runs it from the vault root and compares that output, with surrounding whitespace trimmed, character for character with the stated result, so any other formatting difference is a defect.

The Appraisal section is optional and holds the judgment of the source, covering the standing of its venue and its review, the strengths and limits of its method, its relevance to the output of this vault, and the position the vault takes towards it, as far as each applies to the source at hand. Saying what a source is worth is a different speech act from saying what it says, and the section separates the two so that a reader can tell evidence from opinion at a glance. The appraisal is the vault's own judgment and therefore a posit, so it carries no grounding obligation and no anchor of its own. It also mints no IDs, because every ID in a distillate is citable from the assertion layer. Validation raises `E-STATEMENT` on an ID minted anywhere but in the core statements, which is what keeps an appraisal from ever becoming grounding. Where an appraisal shapes the output, it enters as a posit footnote there.

The Open questions section holds questions and no findings. A finding that could carry an assertion belongs in the core statements with an anchor and an ID of its own, and it is lifted there rather than cited from where it sits. The section mints no IDs for the same reason the appraisal mints none, and that is what makes it the one place in the chain where unanchored material may rest.

### 4. Assertion

One file per assertion in `30_assertions/`. This is the layer where source types converge. An assertion resting on a single source is allowed, and the displaced-subject cases below say when it has to name that source.

```yaml
---
type: assertion
topics: ["[[<Topic>]]"]
status: grounded             # grounded | validated | verified | contested
checked: {}
grounding:
  - "[[20_distillates/documents/<slug>#^s1]]"
  - "[[20_distillates/publications/<slug>#^s2]]"
contested-with: []           # wikilinks; required on both sides when status is contested
created: 2026-01-01
updated: 2026-01-01
---
```

```markdown
# <The assertion as one sentence>

## Statement

<The assertion spelled out, one short paragraph.>

## Support

- [[20_distillates/documents/<slug>#^s1]], <what this anchor contributes>
- [[20_distillates/publications/<slug>#^s2]], <what this anchor contributes>

## Related

- [[30_assertions/…]]
```

A conclusion without source support never becomes an assertion. It enters the output as a posit in the sense of [[knowledge/index]] § Terminology, and where a source turns up later, a new assertion is written and the posit falls away. Assertions that cannot be reconciled are both set to `contested` and linked to each other in `contested-with`.

A passage can support a statement whose subject is not the subject the assertion is about, and the support relation still holds. Validation cannot see this, and machine review separates it only because its contract in [[knowledge/operations]] § Check names the two cases below.

#### Self-report

Where a source speaks about itself, about its own priority, reach or achievement, its passage covers the claim and never the matter the claim is about. The distillate holds such a statement as what the source asserts. An assertion built from it either carries the speaker along, in the form that the source claims something, or it rests on a second and independent source.

#### State report

Where a source shows the matter in one state at one time, its passage covers that state and never the matter across time. A restored object witnesses the restoration, a dated inventory witnesses the day it was taken, a plan witnesses what was intended when it was written. The distillate holds such a statement together with the state and its date. An assertion built from it either names the state and its date, or it rests on a source that establishes the property for the span the assertion claims.

### 5. Topic map (MOC)

One file per topic of the controlled topic set, named `MOC-<Topic>.md` in `30_assertions/`. The set of these files is the topic vocabulary.

```yaml
---
type: moc
topic: "<Topic>"
created: 2026-01-01
updated: 2026-01-01
---
```

```markdown
# MOC: <Topic>

<Lead: one sentence on what this topic covers.>

- [[30_assertions/<slug>]], <half-sentence of orientation>

## Open questions

- <question the vault cannot currently answer from its sources>
```

The body lists every assertion of the topic as a wikilink with a half-sentence of orientation. Every assertion must be reachable from at least one topic map, and the validator raises `E-ORPHAN` on one that is not.

### 6. Glossary entry

One term per file in `glossary/`, serving as definition, wikilink hub and tag keyword.

```yaml
---
type: glossary
term: "<term>"
created: 2026-01-01
updated: 2026-01-01
---
```

```markdown
# <Term>

<Definition in one or two sentences.> [[10_markdown/documents/<slug>#^a1b2]]
```

The body gives the definition in one or two sentences with a grounding anchor where the definition comes from a source. The glossary holds one document per central technical term of the content and is used as the need arises.

### 7. Chapter

One file per chapter in `40_output/`, continuous prose in the project's working language and style sheet. The type name `chapter` denotes the acceptance-capable unit of the output, one file that is checked and accepted on its own. In an article genre it corresponds to a section.

```yaml
---
type: chapter
status: grounded             # grounded | validated | verified
checked: {}
assertions: ["[[30_assertions/<slug>]]"]   # structured mirror of exactly the Grounded-in assertions; posit-linked ones stay out
posits: 0                                  # count of posit footnotes
created: 2026-01-01
updated: 2026-01-01
---
```

Under the anchor contract of the output, every load-bearing sentence carries a footnote marker. Every footnote begins with one of two keywords, and nothing else counts.

```markdown
Water use fell by a third after metering was introduced.[^1] The board should
therefore extend metering to all sites.[^2]

[^1]: Grounded in [[30_assertions/metering-reduces-use]].
[^2]: Posit: follows from [^1] only if consumption patterns are comparable
      across sites. Open evidence question: site-level baseline data.
```

Validation cross-checks the footnotes against the `assertions` mirror and the `posits` count. Footnotes are the reference notation, and an instantiation may substitute another notation as long as marker, keyword and mirror survive.

Where a chapter reports a matter the sources disagree on, it grounds in both sides of the contested pair. A chapter that names one assertion of such a pair and none of its counterparts presents the dispute as settled, and validation raises `W-CONTESTED`.

## Meta documents

The six project knowledge documents in `knowledge/` carry the Promptotyping header, as at the top of this file, instead of a content `type`, and they are exempt from the content schema, as [[knowledge/index]] § Terminology sets out.

## Naming

File names are speaking slugs, ASCII-lowercase with hyphens, derived from genre and subject (`report-water-metering-2026-03`). Markdown representation and distillate of the same source share the same slug. Date suffixes distinguish version rows.
