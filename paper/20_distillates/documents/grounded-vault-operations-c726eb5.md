---
type: distillate
source-type: document
representation: "[[10_markdown/documents/grounded-vault-operations-c726eb5]]"
topics: ["[[Architecture]]", "[[Agentic Workflow]]", "[[Verification]]"]
status: validated
checked:
  validation: 2026-08-10
  machine-review: 2026-08-10
created: 2026-08-10
updated: 2026-08-10
---

# Distillate: Grounded Vault, Operations

The procedure document of the Grounded Vault profile at commit `c726eb5`, from which this vault takes the chains acquire, ingest, distill, build assertions, write chapters and query, and the contracts of its three checking instances.

## Core statements

- The operations document defines the procedures of the vault, one section per chain, where every chain produces or checks artifacts defined in the schema document and updates the registers of the state document, while decisions made along the way go to the journal. [[10_markdown/documents/grounded-vault-operations-c726eb5#^ops01]] ^s1

- How a source enters the vault is orthogonal to its type, the channel is recorded in the `channel` field of the Markdown representation, and it changes nothing about checking. [[10_markdown/documents/grounded-vault-operations-c726eb5#^ops02]] ^s2

- In the channels handover and collection the original is placed in the sources folder. [[10_markdown/documents/grounded-vault-operations-c726eb5#^ops03]] ^s3

- In the channel import, records are exported from the reference library as CSL JSON into the references folder, one file per batch of records. [[10_markdown/documents/grounded-vault-operations-c726eb5#^ops04]] ^s4

- In the channel deep-research the research prompt is run, every located publication is captured in the reference manager and exported as CSL JSON into the references folder, the research report itself never becomes a source, and all anchors bind to the located publications. [[10_markdown/documents/grounded-vault-operations-c726eb5#^ops05]] ^s5

- The deep research prompt directs the search to prioritize peer-reviewed and official sources, to apply the project exclusion list, to evaluate candidates at full text, to counter-check adversarially by searching for sources that contradict each candidate finding, and to deliver bibliographic data with verbatim passages but no synthesis, because the vault synthesizes. [[10_markdown/documents/grounded-vault-operations-c726eb5#^ops06]] ^s6

- The ingest operation is the Markdown conversion in two steps, a structure-preserving conversion of the original in which headings, lists, tables and paragraph boundaries survive as the original had them, and the stamping of a block ID onto every anchor-relevant paragraph, after which the file is never edited again because every later layer anchors into these blocks and an edit would move them. [[10_markdown/documents/grounded-vault-operations-c726eb5#^ops07]] ^s7

- The converter for the conversion step is decided per source along a decision list and recorded in the `converter` field of the Markdown representation, so that a later run can be reproduced or repeated with a different tool. [[10_markdown/documents/grounded-vault-operations-c726eb5#^ops08]] ^s8

- Short, simply structured texts are converted by the agent itself, because a tool adds nothing where the structure is already flat. [[10_markdown/documents/grounded-vault-operations-c726eb5#^ops09]] ^s9

- Standard office and PDF formats are converted through MarkItDown or pandoc. [[10_markdown/documents/grounded-vault-operations-c726eb5#^ops10]] ^s10

- Complex layouts and scanned documents are converted through Docling. [[10_markdown/documents/grounded-vault-operations-c726eb5#^ops11]] ^s11

- Image sources that require OCR are a named extension point of the profile and are not yet worked out. [[10_markdown/documents/grounded-vault-operations-c726eb5#^ops12]] ^s12

- For a document source the Markdown conversion runs into the documents folder of the Markdown layer, the converter is noted in the frontmatter, the H1 is set from the original and the metadata block is filled. [[10_markdown/documents/grounded-vault-operations-c726eb5#^ops13]] ^s13

- For a data source the data file is placed in the data folder of the Markdown layer, a schema description of the same slug is written, and the metadata block is filled. [[10_markdown/documents/grounded-vault-operations-c726eb5#^ops14]] ^s14

- A publication source receives no Markdown representation, because the CSL JSON record in the references folder is the root of this source type. [[10_markdown/documents/grounded-vault-operations-c726eb5#^ops15]] ^s15

- After ingest the inventory tool rewrites the source inventory of the state document from the real file state. [[10_markdown/documents/grounded-vault-operations-c726eb5#^ops16]] ^s16

- The vault produces one distillate per source as a three-stage chain. [[10_markdown/documents/grounded-vault-operations-c726eb5#^ops17]] ^s17

- The extraction stage has an LLM extract the core statements with the canonical prompt, one statement per anchor, without evaluation and without cross-source merging. [[10_markdown/documents/grounded-vault-operations-c726eb5#^ops18]] ^s18

- The formatting stage is a deterministic pass that enforces the section skeleton, the statement IDs and the anchor syntax defined in the schema. [[10_markdown/documents/grounded-vault-operations-c726eb5#^ops19]] ^s19

- The fidelity check compares each statement against its anchor, and for publications the quotation check runs at this point, while the source text is at hand, and is recorded as `checked.quote`. [[10_markdown/documents/grounded-vault-operations-c726eb5#^ops20]] ^s20

- The canonical extraction prompt restricts the extractor to the given text of one source, requires one statement per anchor, requires each statement to stand on its own and stay within the literal sense of the source, forbids evaluation, interpretation, inference and cross-source merging because the vault synthesizes at a later layer, drops any statement whose source location cannot be named, and requires the source location in the form the source type demands. [[10_markdown/documents/grounded-vault-operations-c726eb5#^ops21]] ^s21

- The distillation chain iterates, so a statement that fails the fidelity check is reformulated or discarded and the check runs again, until every remaining statement passes. [[10_markdown/documents/grounded-vault-operations-c726eb5#^ops22]] ^s22

- Where a source is to be judged as well as reproduced, the appraisal is written after the chain has run, so that no evaluation can leak into the extraction the chain checks, and it stays outside the fidelity check, which has nothing to compare it against. [[10_markdown/documents/grounded-vault-operations-c726eb5#^ops23]] ^s23

- A distillate enters at status grounded. [[10_markdown/documents/grounded-vault-operations-c726eb5#^ops24]] ^s24

- Assertions are the layer where the vault synthesizes, one file per assertion, and the work proceeds by topic. [[10_markdown/documents/grounded-vault-operations-c726eb5#^ops25]] ^s25

- Assertion building enters through the topic map and reads every distillate registered there, so that synthesis covers the sources the topic actually holds rather than the ones at hand. [[10_markdown/documents/grounded-vault-operations-c726eb5#^ops26]] ^s26

- The grouping step gathers the distillate statements that concern the same matter across sources and across source types, and a group is the unit an assertion is written from. [[10_markdown/documents/grounded-vault-operations-c726eb5#^ops27]] ^s27

- One atomic assertion is written per group, carried jointly by the sources of that group, where atomic means one statement that cannot be split without losing its point. [[10_markdown/documents/grounded-vault-operations-c726eb5#^ops28]] ^s28

- The grounding step lists in the `grounding` field every statement ID that supports the assertion, one per supporting source, and states in the Support section what each anchor contributes. [[10_markdown/documents/grounded-vault-operations-c726eb5#^ops29]] ^s29

- Where a group holds statements that cannot be reconciled, two assertions are written instead of one, both are set to contested, and they are linked to each other in `contested-with` on both sides. [[10_markdown/documents/grounded-vault-operations-c726eb5#^ops30]] ^s30

- A conclusion that no distillate statement carries is noted for the output as a posit candidate and never becomes an assertion, and the appraisal sections of the distillates are read at this step as posit candidates and never as support, because they hold the vault's judgment of a source rather than its content. [[10_markdown/documents/grounded-vault-operations-c726eb5#^ops31]] ^s31

- Every assertion is registered in its topic map with a half-sentence of orientation, and questions the sources leave open are recorded under the map's open questions. [[10_markdown/documents/grounded-vault-operations-c726eb5#^ops32]] ^s32

- Machine review runs over every pair of assertion and supporting statement, and a verdict below fully supports means the assertion is reformulated to the width its sources actually carry or the grounding is corrected by dropping the anchor that does not carry it and naming one that does, after which review repeats on the changed pair. [[10_markdown/documents/grounded-vault-operations-c726eb5#^ops33]] ^s33

- The assertion review prompt casts the reviewer as adversarial with the task of refuting the assertion, restricts the judgment to whether this statement supports this assertion while the truth of the assertion is out of scope, requires exactly one verdict from the fixed vocabulary with one sentence of justification, and requires naming the part of the assertion the statement does not carry where the verdict is not fully supports. [[10_markdown/documents/grounded-vault-operations-c726eb5#^ops34]] ^s34

- Every load-bearing sentence of a chapter gets a footnote of the form grounded in an assertion and every own conclusion gets a posit footnote with its rationale and open evidence question, while the referenced assertions and the posit count are mirrored in the frontmatter. [[10_markdown/documents/grounded-vault-operations-c726eb5#^ops35]] ^s35

- A chapter that reports the state of research across the sources of a topic needs no document type of its own, because agreement becomes sentences grounded in the assertions of the topic, disagreement becomes sentences grounded in both sides of a contested pair, and the gap that the vault's own work closes carries no source and becomes a posit footnote with its open evidence question, read off the topic map's open questions. [[10_markdown/documents/grounded-vault-operations-c726eb5#^ops36]] ^s36

- A question is answered from the vault by entering through the topic maps and following assertions to their distillate statements and, where exactness matters, down to the source passage, quoting assertions by wikilink so the answer stays anchored, and questions the vault cannot answer are recorded as open questions in the topic's map. [[10_markdown/documents/grounded-vault-operations-c726eb5#^ops37]] ^s37

- Three instances check the vault, the architecture fixes their contracts, and the mechanism fulfilling each contract is an instantiation decision recorded in the specification. [[10_markdown/documents/grounded-vault-operations-c726eb5#^ops38]] ^s38

- Validation judges the formal conformance of every file against the schema. [[10_markdown/documents/grounded-vault-operations-c726eb5#^ops39]] ^s39

- Validation gates everything, so no other check runs on a file that fails it, and it sets no status by itself except by enforcing the discipline. [[10_markdown/documents/grounded-vault-operations-c726eb5#^ops40]] ^s40

- Validation is deterministic, gives the same verdict on the same input, and runs on every change. [[10_markdown/documents/grounded-vault-operations-c726eb5#^ops41]] ^s41

- Validation records its date on every file that passes. [[10_markdown/documents/grounded-vault-operations-c726eb5#^ops42]] ^s42

- The reference mechanism of validation checks frontmatter per type, anchor resolution, statement IDs, quotation identity where a source text is available, computation declarations, topic map reachability, bidirectional contested links, chapter mirror and footnote keywords and status discipline, and it re-runs and compares data anchors by default, which a switch turns off for a fast run. [[10_markdown/documents/grounded-vault-operations-c726eb5#^ops43]] ^s43

- In chapter scope validation judges one chapter and, transitively, the assertions, distillates and Markdown representations it grounds in, so that a chapter can be reported ready while other parts of the vault are still in progress; the scope walk follows only anchors pointing one layer down, the vault-level warnings stay out because they are decidable only over the whole vault, and any warning inside the scope fails the run alongside an error because the run decides acceptance. [[10_markdown/documents/grounded-vault-operations-c726eb5#^ops44]] ^s44

- The validation checks carry their own codes, among them anchor resolution, layer skipping, empty grounding, duplicate block or statement IDs, a status lacking a required check or a check without a date, and a document standing higher on the status ladder than an anchor it rests on, alongside warnings for unreplaced template placeholders, an empty production chain, checks older than the content they judge, two assertions with the same or contained grounding set, and a chapter footnote alias that differs from the H1 title of the assertion it points to. [[10_markdown/documents/grounded-vault-operations-c726eb5#^ops45]] ^s45

- A run without errors is not by itself the success criterion, because every warning names either a check that found no subject or a defect the schema does not make an error, and both are the failure modes a silent green run hides; over the whole vault a warning never changes the exit code so that work in progress stays runnable, while in chapter mode a warning fails the run. [[10_markdown/documents/grounded-vault-operations-c726eb5#^ops46]] ^s46

- Machine review judges per pair whether a source location actually supports the statement built on it, using the fixed verdict vocabulary fully supports, partially supports, overreaches, contradicts and not in the text, of which only fully supports passes. [[10_markdown/documents/grounded-vault-operations-c726eb5#^ops47]] ^s47

- Machine review together with validation lifts a document to validated and never higher. [[10_markdown/documents/grounded-vault-operations-c726eb5#^ops48]] ^s48

- Anti-anchoring is mandatory for machine review, so the reviewer sees only the source location and the statement while the producing agent's reasoning stays hidden, and a reviewer from a different model family than the producer is recommended because it decorrelates error modes. [[10_markdown/documents/grounded-vault-operations-c726eb5#^ops49]] ^s49

- Machine review records its date, and verdicts below fully supports trigger rework and are noted in the journal when they reveal a systematic pattern. [[10_markdown/documents/grounded-vault-operations-c726eb5#^ops50]] ^s50

- The machine review prompt casts the reviewer as adversarial with the task of refuting the statement, restricts the judgment to whether this passage supports this statement, requires exactly one verdict from the fixed vocabulary followed by one sentence of justification, and supplies the reviewer with the source location including its heading path and the statement alone. [[10_markdown/documents/grounded-vault-operations-c726eb5#^ops51]] ^s51

- A machine review pair consists of the anchored location, which for documents is the block plus its heading path, for publications the quotation and for data the computation and its result, together with the bare statement, and nothing else enters the pair. [[10_markdown/documents/grounded-vault-operations-c726eb5#^ops52]] ^s52

- Verification judges by human expert judgment whether a grounding relation holds as evidence, and its authority is the verification role named in the specification. [[10_markdown/documents/grounded-vault-operations-c726eb5#^ops53]] ^s53

- Verification alone lifts a document to verified, and the machine checks prepare it but never replace it. [[10_markdown/documents/grounded-vault-operations-c726eb5#^ops54]] ^s54

- Verification proceeds passage by passage on the prepared pairs and may sample where the machine review pass rate justifies it, with the sampling rule noted in the journal. [[10_markdown/documents/grounded-vault-operations-c726eb5#^ops55]] ^s55

- Verification records its date, set by or on behalf of the verifying role. [[10_markdown/documents/grounded-vault-operations-c726eb5#^ops56]] ^s56

- The status ladder runs from grounded through validated, reached when validation and machine review have passed, to verified, reached when the expert has passed, while contested is set by assertion building or review when sources conflict and is resolved only by verification, and a document's status is the minimum of its anchors' states. [[10_markdown/documents/grounded-vault-operations-c726eb5#^ops57]] ^s57

## Terms

- **Markdown conversion**: the two-step ingest operation, a structure-preserving conversion of the original followed by the stamping of a block ID onto every anchor-relevant paragraph. [[10_markdown/documents/grounded-vault-operations-c726eb5#^ops07]]
- **Fidelity check**: the third stage of the distillation chain, the comparison of each extracted statement against its anchor. [[10_markdown/documents/grounded-vault-operations-c726eb5#^ops20]]
- **Atomic assertion**: one statement that cannot be split without losing its point, carried jointly by the sources of its group. [[10_markdown/documents/grounded-vault-operations-c726eb5#^ops28]]
- **Posit candidate**: a conclusion that no distillate statement carries, noted for the output and never turned into an assertion. [[10_markdown/documents/grounded-vault-operations-c726eb5#^ops31]]
- **Anti-anchoring**: the mandatory condition of machine review under which the reviewer sees only the source location and the statement, while the producing agent's reasoning stays hidden. [[10_markdown/documents/grounded-vault-operations-c726eb5#^ops49]]
- **Pair cutting**: the rule fixing what enters a review pair, the anchored location in the form its source type takes and the bare statement, and nothing else. [[10_markdown/documents/grounded-vault-operations-c726eb5#^ops52]]

## Open questions

- The document requires the fidelity check to compare each statement against its anchor without naming the criterion by which the comparison passes or fails.
- It calls the formatting stage deterministic without saying whether a program or an agent performs it.
- It recommends a reviewer from a different model family without giving a rule for what counts as a different family or what follows when none is available.
- It permits sampling in verification where the machine review pass rate justifies it, without stating a threshold or a sampling procedure.

## Appraisal

The procedural counterpart of the schema document, by the same author and with the same standing, authoritative for what the profile prescribes and silent on whether the prescription holds up. Its strength for this vault lies in the prompt skeletons and the three check contracts, which state the division of authority between deterministic, probabilistic and human checking in terms concrete enough to be measured against an implementation. Its weak point is that several steps are named without an operational criterion, so the chain leaves more to the executing agent than the schema does, which is a finding about the source rather than a defect the source concedes.

## Related

- [[20_distillates/documents/grounded-vault-schema-c726eb5]]
- [[20_distillates/documents/promptotyping-specification-2026-07-31]]
