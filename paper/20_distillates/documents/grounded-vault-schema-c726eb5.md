---
type: distillate
source-type: document
representation: "[[10_markdown/documents/grounded-vault-schema-c726eb5]]"
topics: ["[[Architecture]]", "[[Provenance]]", "[[Verification]]"]
status: validated
checked:
  validation: 2026-08-10
  machine-review: 2026-08-10
created: 2026-08-10
updated: 2026-08-10
---

# Distillate: Grounded Vault, Schema

The schema document of the Grounded Vault profile at commit `c726eb5`, from which this vault takes the layer model, the anchor mechanics of the three source types, the audit trail and the frontmatter and section skeleton of every document type it produces.

## Core statements

- The schema document defines the layer model, the controlled vocabularies, the anchor mechanics per source type, the audit trail and, for every content document type, the exact frontmatter and section skeleton, and it defines only what a well-formed artifact is, while the procedures that produce and check these documents live in the operations document. [[10_markdown/documents/grounded-vault-schema-c726eb5#^sch01]] ^s1

- The architecture has five layers, sources as the ground carrying no anchor, the Markdown representation holding archived full texts and datasets with schema and carrying block IDs and file plus schema, distillates carrying grounding anchors into their source and statement IDs, assertions carrying grounding anchors into distillate statements, and the output carrying footnote anchors into assertions with posits marked. [[10_markdown/documents/grounded-vault-schema-c726eb5#^sch02]] ^s2

- The source inventory listing every Markdown representation and every distillate is generated from the file state by a tool rather than maintained by hand, because the files are the one record of what the vault holds and a second bookkeeping could drift away from them. [[10_markdown/documents/grounded-vault-schema-c726eb5#^sch03]] ^s3

- A source is the original file exactly as it arrived, kept untouched so that every later form of its content can be checked against it; a Markdown representation is the uniform Markdown form of a source, produced once and given block IDs so that later layers anchor into passages that never change afterwards; a distillate is the set of single statements extracted from one source, each anchored to the passage it was taken from; an assertion is a single source-supported statement synthesized from the distillates of a topic and grounded in at least one distillate statement; a chapter is an output text in which every load-bearing sentence carries a footnote to an assertion and every own conclusion is marked as a posit. [[10_markdown/documents/grounded-vault-schema-c726eb5#^sch04]] ^s4

- Two rules constrain the chain, that anchors are minted only at the layer they belong to, so that a Markdown representation mints block IDs and a distillate mints statement IDs and no higher layer creates anchors into material below its direct predecessor, and that each layer references only the layer directly beneath it. [[10_markdown/documents/grounded-vault-schema-c726eb5#^sch05]] ^s5

- The controlled vocabulary of the `type` field is representation, distillate, assertion, moc, glossary and chapter, where `representation` is the machine-side short form for Markdown representation and the prose uses the full term. [[10_markdown/documents/grounded-vault-schema-c726eb5#^sch06]] ^s6

- The controlled vocabulary of the `source-type` field is document, publication and data. [[10_markdown/documents/grounded-vault-schema-c726eb5#^sch07]] ^s7

- The controlled vocabulary of the `channel` field is handover, collection, import and deep-research. [[10_markdown/documents/grounded-vault-schema-c726eb5#^sch08]] ^s8

- The controlled vocabulary of the `status` field is grounded, validated and verified, plus contested for assertions only and superseded for distillates only. [[10_markdown/documents/grounded-vault-schema-c726eb5#^sch09]] ^s9

- Every value of the `topics` field must name an existing topic map, and the set of `MOC-*.md` files in the assertions folder is the controlled topic set. [[10_markdown/documents/grounded-vault-schema-c726eb5#^sch10]] ^s10

- A status records the outcome of checks that actually ran, and every check writes its date into the `checked` map of the document it checked. [[10_markdown/documents/grounded-vault-schema-c726eb5#^sch11]] ^s11

- The status discipline is machine-enforced, so that `validated` requires a recorded validation and machine review, `verified` additionally requires a recorded verification, every entry of the `checked` map carries an ISO date because a record without one cannot be held against the content it judges, `grounded` is the entry status of every freshly produced document and requires no entry, a document's status is the minimum of the states of its anchors, and documents resting on a contested or superseded anchor stay at `grounded` because those two states lie beside the ladder. [[10_markdown/documents/grounded-vault-schema-c726eb5#^sch12]] ^s12

- Every Markdown representation carries a compact, Dublin-Core-compatible metadata block, and licensing and confidentiality are metadata of the individual source on which nothing else in the architecture depends. [[10_markdown/documents/grounded-vault-schema-c726eb5#^sch13]] ^s13

- The metadata block holds title, creator, date, format, identifier, license and a confidentiality flag whose true value keeps original and full text local, and it names the creator by role and institution without third-party personal names. [[10_markdown/documents/grounded-vault-schema-c726eb5#^sch14]] ^s14

- The source type of a source follows from whether its content may be stored in the vault and from the anchor that storage decision permits. [[10_markdown/documents/grounded-vault-schema-c726eb5#^sch15]] ^s15

- A document is a source whose full text may be stored and which is anchored by block reference into its Markdown representation, a publication is a source that is only cited, whose vault-side record is bibliographic and whose anchor is the verbatim quotation together with the identifier, and a data source is a file whose anchor is a deterministic computation over that file, because an aggregate or a statistical finding exists at no single passage. [[10_markdown/documents/grounded-vault-schema-c726eb5#^sch16]] ^s16

- The criterion of the source type is storability rather than publication status, so an open-access article that may be stored is treated as a document, and where a full text may be stored the type `document` is preferred over `publication` because its anchors resolve inside the vault. [[10_markdown/documents/grounded-vault-schema-c726eb5#^sch17]] ^s17

- The bibliographic records of the citable-only sources are held as CSL JSON exported from the reference manager, one JSON array of records per file, each record carrying an `id` alongside its bibliographic fields. [[10_markdown/documents/grounded-vault-schema-c726eb5#^sch18]] ^s18

- The `reference` field of a publication distillate names one CSL JSON id, validation raises `E-ANCHOR` when no record carries it, and the reference folder is needed only while the source type publication is active. [[10_markdown/documents/grounded-vault-schema-c726eb5#^sch19]] ^s19

- Each document type is specified by its frontmatter and, where one is fixed, its section skeleton, with fields required unless marked optional, and with wikilink values quoted and block IDs unquoted as Obsidian requires for YAML. [[10_markdown/documents/grounded-vault-schema-c726eb5#^sch20]] ^s20

- For the source type document there is exactly one Markdown representation per source, and a revised source enters as a new file with a date-suffixed slug, so that existing anchors keep resolving against the old file. [[10_markdown/documents/grounded-vault-schema-c726eb5#^sch21]] ^s21

- The body of a Markdown representation of a document is the converted full text under an H1 taken from the original, and every anchor-relevant paragraph ends with a block ID. [[10_markdown/documents/grounded-vault-schema-c726eb5#^sch22]] ^s22

- Block IDs are short, stable, unique per file, and minted only in the Markdown representation. [[10_markdown/documents/grounded-vault-schema-c726eb5#^sch23]] ^s23

- A data representation consists of the data file and a Markdown file of the same slug beside it that carries the frontmatter and describes the schema. [[10_markdown/documents/grounded-vault-schema-c726eb5#^sch24]] ^s24

- The body of a data representation describes columns, units, encodings and known limitations, and the anchor of this source type is a computation defined in the distillate. [[10_markdown/documents/grounded-vault-schema-c726eb5#^sch25]] ^s25

- A distillate is one file per source sharing the slug of its Markdown representation, and its core statements reproduce their source without merging it with other sources, because synthesis belongs to the assertion layer and judging the source belongs to the Appraisal section. [[10_markdown/documents/grounded-vault-schema-c726eb5#^sch26]] ^s26

- Every core statement of a distillate carries exactly one grounding anchor into its source and ends with a statement ID, which is the anchor assertions bind to. [[10_markdown/documents/grounded-vault-schema-c726eb5#^sch27]] ^s27

- For the source type document the anchor of a core statement is a block reference into the Markdown representation. [[10_markdown/documents/grounded-vault-schema-c726eb5#^sch28]] ^s28

- For the source type publication the anchor is a verbatim quotation with citation instead of a block reference, the quotation must appear character for character in the source, and the intake-time check is recorded as `checked.quote`. [[10_markdown/documents/grounded-vault-schema-c726eb5#^sch29]] ^s29

- For the source type data the anchor is a reproducible computation named on an indented line, whose script lives in the analysis folder of the tools and is deterministic. [[10_markdown/documents/grounded-vault-schema-c726eb5#^sch30]] ^s30

- The computation script reads the data file of the Markdown representation, takes no arguments and prints the stated result and nothing else to standard output, and validation re-runs it from the vault root and compares that output character for character with the stated result, so that a formatting difference is a defect. [[10_markdown/documents/grounded-vault-schema-c726eb5#^sch31]] ^s31

- The Appraisal section is optional, holds the judgment of the source covering the standing of its venue and review, the strengths and limits of its method, its relevance and the position the vault takes towards it, is the vault's own judgment and therefore a posit carrying no grounding obligation and no anchor, and mints no IDs, which validation enforces by raising `E-STATEMENT` on an ID minted anywhere but in the core statements. [[10_markdown/documents/grounded-vault-schema-c726eb5#^sch32]] ^s32

- An assertion is one file per statement in the assertions folder and is the layer where the source types converge. [[10_markdown/documents/grounded-vault-schema-c726eb5#^sch33]] ^s33

- A conclusion without source support never becomes an assertion but enters the output as a posit, and assertions that cannot be reconciled are both set to contested and linked to each other in the `contested-with` field. [[10_markdown/documents/grounded-vault-schema-c726eb5#^sch34]] ^s34

- There is one topic map file per topic of the controlled topic set, and the set of these files is the topic vocabulary. [[10_markdown/documents/grounded-vault-schema-c726eb5#^sch35]] ^s35

- A topic map lists every assertion of its topic as a wikilink with a half-sentence of orientation, every assertion must be reachable from at least one topic map, and the validator raises `E-ORPHAN` on one that is not. [[10_markdown/documents/grounded-vault-schema-c726eb5#^sch36]] ^s36

- The glossary holds one term per file, serving as definition, wikilink hub and tag keyword. [[10_markdown/documents/grounded-vault-schema-c726eb5#^sch37]] ^s37

- A glossary entry gives its definition in one or two sentences with a grounding anchor where the definition comes from a source, and the glossary is used as the need arises. [[10_markdown/documents/grounded-vault-schema-c726eb5#^sch38]] ^s38

- A chapter is one file of continuous prose in the project's working language and style sheet, and the type name denotes the acceptance-capable unit of the output, one file that is checked and accepted on its own, which in an article genre corresponds to a section. [[10_markdown/documents/grounded-vault-schema-c726eb5#^sch39]] ^s39

- The anchor contract of the output requires a footnote marker on every load-bearing sentence and a footnote that begins with one of two keywords, and nothing else counts. [[10_markdown/documents/grounded-vault-schema-c726eb5#^sch40]] ^s40

- Validation cross-checks the footnotes of a chapter against the `assertions` mirror and the posit count, and footnotes are the reference notation of the profile, which an instantiation may substitute as long as marker, keyword and mirror survive. [[10_markdown/documents/grounded-vault-schema-c726eb5#^sch41]] ^s41

- A chapter reporting a matter the sources disagree on grounds in both sides of the contested pair, and validation raises `W-CONTESTED` when it names one assertion of such a pair and none of its counterparts, because that presents the dispute as settled. [[10_markdown/documents/grounded-vault-schema-c726eb5#^sch42]] ^s42

- The six knowledge documents carry the Promptotyping header instead of a content type, are meta-knowledge about the vault exempt from the content schema, and a knowledge document is split only when its sections develop divergent update rhythms or divergent readers. [[10_markdown/documents/grounded-vault-schema-c726eb5#^sch43]] ^s43

- File names are speaking slugs in ASCII lowercase with hyphens derived from genre and subject, Markdown representation and distillate of the same source share the same slug, and date suffixes distinguish version rows. [[10_markdown/documents/grounded-vault-schema-c726eb5#^sch44]] ^s44

## Terms

- **Source**: the original file exactly as it arrived, kept untouched so that every later form of its content can be checked against it. [[10_markdown/documents/grounded-vault-schema-c726eb5#^sch04]]
- **Markdown representation**: the uniform Markdown form of a source, produced once by conversion and given block IDs so that later layers anchor into passages that never change afterwards. [[10_markdown/documents/grounded-vault-schema-c726eb5#^sch04]]
- **Distillate**: the set of single statements extracted from one source, each anchored to the passage of the representation it was taken from. [[10_markdown/documents/grounded-vault-schema-c726eb5#^sch04]]
- **Assertion**: a single source-supported statement synthesized from the distillates of a topic and grounded in at least one distillate statement. [[10_markdown/documents/grounded-vault-schema-c726eb5#^sch04]]
- **Chapter**: an output text in which every load-bearing sentence carries a footnote to an assertion and every own conclusion is marked as a posit. [[10_markdown/documents/grounded-vault-schema-c726eb5#^sch04]]
- **Document (source type)**: a source whose full text may be stored in the vault and which is anchored by block reference into its Markdown representation. [[10_markdown/documents/grounded-vault-schema-c726eb5#^sch16]]
- **Publication (source type)**: a source that is only cited, whose vault-side record is bibliographic and whose anchor is the verbatim quotation together with the identifier. [[10_markdown/documents/grounded-vault-schema-c726eb5#^sch16]]
- **Data (source type)**: a file whose anchor is a deterministic computation over that file. [[10_markdown/documents/grounded-vault-schema-c726eb5#^sch16]]
- **Block ID**: the short, stable, per-file unique identifier that a Markdown representation stamps on an anchor-relevant paragraph and that no other layer mints. [[10_markdown/documents/grounded-vault-schema-c726eb5#^sch23]]
- **Appraisal**: the optional section in which a distillate states the vault's own judgment of a source, a posit that carries no anchor and mints no ID. [[10_markdown/documents/grounded-vault-schema-c726eb5#^sch32]]

## Open questions

- The schema fixes the anchor mechanics of three source types and names no procedure by which a further source type would be added.
- It requires block IDs to be short, stable and unique per file without stating a minting scheme or a granularity rule for which paragraph counts as anchor-relevant.
- It defines the status ladder as the minimum over a document's anchors without saying how a status is corrected downwards when an anchor later falls to contested.

## Appraisal

The source is the normative document of the architecture this vault runs on, written by the operator of this vault, so it is authoritative for what the profile prescribes and carries no independent standing for whether the prescription works. Its strength for the vault is that it is fully explicit, since almost every rule has a code the validator enforces, which makes the gap between stated architecture and implemented architecture checkable rather than assertable. Its limit is that it is a template document, so it holds no evidence about any instance, and any claim that the architecture is practicable belongs to the instances rather than to this source.

## Related

- [[20_distillates/documents/grounded-vault-operations-c726eb5]]
- [[20_distillates/documents/promptotyping-specification-2026-07-31]]
