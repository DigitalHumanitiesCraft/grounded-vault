---
type: distillate
source-type: document
representation: "[[10_markdown/documents/grounded-vault-index-79cd1d3]]"
topics: ["[[Architecture]]", "[[Verification]]"]
status: grounded
checked: {}
created: 2026-09-26
updated: 2026-09-26
---

# Distillate: Grounded Vault, Terminology

The terminology section of the Grounded Vault profile at commit `79cd1d3` of 2026-09-26, the first state in which the profile defines each term in one place and defines the distillate as a knowledge document rather than as a set of statements.

## Core statements

- The terminology section states that each term of the vault is defined there and nowhere else, while the schema fixes the form of what the terms name and the operations document fixes the procedures that produce and check it. [[10_markdown/documents/grounded-vault-index-79cd1d3#^idx01]] ^s1
- The terminology defines a knowledge document, in the sense of Promptotyping, as a bounded and maintained document that distills fuller material into what a task needs and is readable for humans and agents, holding checked and adopted interpretation that separates it from a regenerable derived artifact, and it names the distillate and the project knowledge document as its two kinds. [[10_markdown/documents/grounded-vault-index-79cd1d3#^idx02]] ^s2
- The terminology defines a project knowledge document as one of the six documents in `knowledge/` that describe the vault itself, and it states that such a document rests on no source, carries no anchor and stands outside the content schema. [[10_markdown/documents/grounded-vault-index-79cd1d3#^idx03]] ^s3
- The terminology defines the distillate as the source-bound knowledge document, one per source, which condenses what the source says into anchored core statements and holds the source's terms, open questions and optional appraisal beside them, and which falls under the content schema and its checks because it is bound to a source. [[10_markdown/documents/grounded-vault-index-79cd1d3#^idx07]] ^s4
- The terminology defines the appraisal as the optional section of a distillate holding the vault's judgment of the source, and it states that the appraisal is a posit, mints no IDs and can therefore never serve as grounding. [[10_markdown/documents/grounded-vault-index-79cd1d3#^idx08]] ^s5
- The terminology defines an assertion as a single source-supported statement synthesized from the distillates of a topic and grounded in at least one distillate statement, and it explains source-supported as resting on sources and never on the author alone, without being bound to one source, so that one source is enough. [[10_markdown/documents/grounded-vault-index-79cd1d3#^idx09]] ^s6
- The terminology defines the topic map as the file `MOC-<Topic>.md` in `30_assertions/`, one per topic, registering the distillates and assertions of that topic, and it identifies the set of topic maps with the controlled topic set. [[10_markdown/documents/grounded-vault-index-79cd1d3#^idx10]] ^s7
- The terminology defines a chapter as an output text in which every load-bearing sentence carries a footnote to an assertion and every own conclusion is marked as a posit, and as the unit of the output that is checked and accepted on its own. [[10_markdown/documents/grounded-vault-index-79cd1d3#^idx12]] ^s8
- The terminology defines a posit as a conclusion in the output without source support, marked with its rationale and open evidence question, and it states that a posit differs from an assertion in kind and not in ripeness and never matures into one. [[10_markdown/documents/grounded-vault-index-79cd1d3#^idx13]] ^s9
- The terminology defines an anchor as a machine-resolvable reference from a statement to the location it rests on one layer down, and it assigns block IDs to the Markdown representation, grounding anchors and statement IDs to the distillate, grounding anchors into distillate statements to the assertion and footnote anchors into assertions to the chapter. [[10_markdown/documents/grounded-vault-index-79cd1d3#^idx14]] ^s10
- The terminology defines a block ID as the ID minted once at ingest on a passage of a document representation, which distillate anchors bind to. [[10_markdown/documents/grounded-vault-index-79cd1d3#^idx15]] ^s11
- The terminology defines a core statement as a statement in the Core statements section of a distillate that reproduces its source within the source's literal sense and carries exactly one grounding anchor whose form follows the source type, and it states that only core statements can support an assertion. [[10_markdown/documents/grounded-vault-index-79cd1d3#^idx16]] ^s12
- The terminology defines the statement ID as the ID that ends a core statement, minted only in a distillate, which assertions bind to. [[10_markdown/documents/grounded-vault-index-79cd1d3#^idx17]] ^s13
- The terminology defines validation as deterministic conformance checking of every file against the schema, judging resolvability and form and lifting a document to `validated` together with machine review. [[10_markdown/documents/grounded-vault-index-79cd1d3#^idx20]] ^s14
- The terminology defines machine review as adversarial checking by a language model under anti-anchoring that judges per pair of source location and statement whether the location supports the statement with one verdict from a fixed vocabulary, and that lifts a document to `validated` together with validation and never higher. [[10_markdown/documents/grounded-vault-index-79cd1d3#^idx21]] ^s15
- The terminology defines verification as human expert review by the verification role, which alone establishes evidence and sets `verified`, and it notes that this assignment of the three check terms inverts the IEEE convention. [[10_markdown/documents/grounded-vault-index-79cd1d3#^idx22]] ^s16
- The terminology defines evidence as a grounding relation that has passed verification and calls it relational and deliberately rare. [[10_markdown/documents/grounded-vault-index-79cd1d3#^idx23]] ^s17
- The terminology defines the status ladder as `grounded`, `validated` and `verified`, with `contested` and `superseded` beside it, and states that a document's status is the minimum of the states of its anchors. [[10_markdown/documents/grounded-vault-index-79cd1d3#^idx24]] ^s18

## Terms

- **Knowledge document**: a bounded, maintained document distilling fuller material into what a task needs, with the distillate and the project knowledge document as its two kinds. [[10_markdown/documents/grounded-vault-index-79cd1d3#^idx02]]
- **Project knowledge document**: one of the six documents in `knowledge/`, resting on no source and outside the content schema. [[10_markdown/documents/grounded-vault-index-79cd1d3#^idx03]]
- **Distillate**: the source-bound knowledge document, one per source. [[10_markdown/documents/grounded-vault-index-79cd1d3#^idx07]]

## Open questions

- The terminology takes the knowledge document from Promptotyping but does not say whether the three Promptotyping kinds of declarative, process and agent instruction documents apply to the distillate.

## Related

- [[20_distillates/documents/grounded-vault-schema-c726eb5]]
