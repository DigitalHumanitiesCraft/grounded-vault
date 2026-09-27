---
type: representation
source-type: document
source: "[[00_sources/grounded-vault-knowledge-index-79cd1d3.md]]"
converter: "none; the original is Markdown, the agent selected the representation and stamped the block IDs"
channel: collection
metadata:
  title: "Grounded Vault, knowledge/index.md, the terminology of the profile this vault instantiates"
  creator: "Digital Humanities Craft; Christopher Pollin, Department of Digital Humanities, University of Graz (vault operator)"
  date: "2026-09-26"
  format: "markdown"
  identifier: "https://github.com/DigitalHumanitiesCraft/grounded-vault, knowledge/index.md at commit 79cd1d37b6a3d8750fbb1ddd4520f5186045d3dd of 2026-09-26"
  license: "CC-BY-4.0"
  confidential: false
created: 2026-09-26
updated: 2026-09-26
---

# Terminology

Scope: the Terminology section of `knowledge/index.md` of the Grounded Vault template repository, taken at commit `79cd1d3` of 2026-09-26, from its section heading to the end of the file. The Promptotyping header, the reading paths and the table of the six project knowledge documents are not represented here. Wikilink brackets of the original appear as `\[\[` and `\]\]`, because this vault would otherwise read them as its own anchors. This escape changes no word of the text.

Each term of the vault is defined here and nowhere else. \[\[knowledge/schema\]\] fixes the form of what these terms name, \[\[knowledge/operations\]\] the procedures that produce and check it. ^idx01

### Documents and layers

- **Knowledge document**: A bounded, maintained document that distills fuller material into what a task needs, readable for humans and agents alike, as [Promptotyping](https://dhcraft.org/Promptotyping/) defines it. It holds interpretation that has been checked and adopted, which separates it from a derived artifact that could simply be regenerated. The vault knows two kinds, the distillate and the project knowledge document, and the bare term is used only where both are meant. ^idx02
- **Project knowledge document**: One of the six documents in `knowledge/`, which describe the vault itself, its terms, parameters, schema, procedures, state and decisions. It rests on no source, carries no anchor and stands outside the content schema. ^idx03
- **Source**: The original file exactly as it arrived, kept untouched so that every later form of its content can be checked against it. ^idx04
- **Source type**: A class of sources defined by its Markdown representation, its distillation operation and its grounding anchor: `document`, `publication` or `data`. ^idx05
- **Markdown representation**: The uniform Markdown form of a source, produced once by converting the original and given block IDs so that later layers anchor into passages that never change afterwards. ^idx06
- **Distillate**: The source-bound knowledge document, one per source. It condenses what the source says into core statements, each anchored to the passage of the representation it was taken from, and holds the source's terms, open questions and optional appraisal beside them. Being bound to a source, it falls under the content schema and its checks. ^idx07
- **Appraisal**: The optional section of a distillate that holds the vault's judgment of the source, such as the standing of its venue, the limits of its method and its relevance. It is a posit, mints no IDs and can therefore never serve as grounding. ^idx08
- **Assertion**: A single source-supported statement synthesized from the distillates of a topic and grounded in at least one distillate statement. Source-supported means that it rests on sources and never on the author alone, not that it is bound to one source: a core statement reports what its one source says, while an assertion states the matter, so a further source can join its grounding without the assertion changing. One source is enough. ^idx09
- **Topic map**: The file `MOC-<Topic>.md` in `30_assertions/`, one per topic, which registers the distillates and assertions of that topic. The set of topic maps is the controlled topic set. ^idx10
- **Output**: The final product of the vault, one or more documents such as a report, proposal, thesis or paper, held as chapters. ^idx11
- **Chapter**: An output text in which every load-bearing sentence carries a footnote to an assertion and every own conclusion is marked as a posit. It is the unit of the output that is checked and accepted on its own. ^idx12
- **Posit**: A conclusion in the output without source support, explicitly marked with its rationale and open evidence question. It differs from an assertion in kind, not in ripeness, and never matures into one. ^idx13

### Anchors and statements

- **Anchor**: A machine-resolvable reference from a statement to the location it rests on, one layer down. Each layer carries its own form: block IDs in the Markdown representation, grounding anchors and statement IDs in the distillate, grounding anchors into distillate statements in the assertion, footnote anchors into assertions in the chapter. ^idx14
- **Block ID**: The ID (`^a1b2`) minted once at ingest on a passage of a document representation, the target distillate anchors bind to. ^idx15
- **Core statement**: A statement in the Core statements section of a distillate that reproduces its source within the source's literal sense. It carries exactly one grounding anchor, whose form follows the source type: a block reference for a document, a verbatim quotation for a publication, a declared computation for data. Only core statements can support an assertion. ^idx16
- **Statement ID**: The ID (`^s1`) that ends a core statement, minted only in a distillate, the target assertions bind to. ^idx17
- **Grounding**: The anchor relation between an assertion and its source locations. A structural property an agent can produce; it says nothing about whether the statement is true. ^idx18
- **Provenance chain**: The unbroken anchor path from an output sentence through assertions and distillates to source locations. A break anywhere is a defect that validation detects. ^idx19

### Checking

- **Validation**: Deterministic conformance checking of every file against the schema, by `tools/validate.py` in the reference implementation. It judges resolvability and form; together with machine review it lifts a document to `validated`. ^idx20
- **Machine review**: Adversarial checking by a language model under anti-anchoring, which judges per pair of source location and statement whether the location supports the statement, with one verdict from a fixed vocabulary. Together with validation it lifts a document to `validated`, never higher. ^idx21
- **Verification**: Human expert review by the verification role named in \[\[knowledge/specification\]\]. It alone establishes evidence and sets `verified`. Note that this assignment of the three terms inverts the IEEE convention; here establishing truth is a human act. ^idx22
- **Evidence**: A grounding relation that has passed verification. Relational and deliberately rare; a fresh vault contains grounding, evidence arises only through review. ^idx23
- **Status ladder**: `grounded` → `validated` → `verified`, with `contested` for assertions whose sources conflict and `superseded` for replaced distillates beside the ladder. A document's status is the minimum of the states of its anchors. ^idx24
- **Audit trail**: The principle that status fields record outcomes of checks that actually ran, each with its date on the checked document. ^idx25
