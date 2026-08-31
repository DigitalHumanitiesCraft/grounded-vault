---
type: chapter
status: grounded
checked:
  validation: 2026-08-21
assertions:
  - "[[30_assertions/generated-citations-often-fail-to-support-their-sentences]]"
  - "[[30_assertions/source-binding-lowers-unsupported-citation-without-eliminating-it]]"
  - "[[30_assertions/resolvable-citation-without-support-is-a-distinct-error-class]]"
  - "[[30_assertions/attribution-is-separate-from-correctness]]"
  - "[[30_assertions/historical-method-separates-origin-check-from-credibility]]"
  - "[[30_assertions/layer-model-assigns-each-layer-its-anchor-form]]"
  - "[[30_assertions/anchors-are-minted-at-their-own-layer-and-bind-one-layer-down]]"
  - "[[30_assertions/source-type-follows-storability-and-fixes-the-anchor-form]]"
  - "[[30_assertions/markdown-representation-is-immutable-after-ingest]]"
  - "[[30_assertions/output-binds-load-bearing-sentences-by-footnote-and-marks-posits]]"
  - "[[30_assertions/obsidian-stores-notes-as-plain-text-with-rebuildable-derived-state]]"
  - "[[30_assertions/block-references-address-blocks-as-literal-text-markers]]"
  - "[[30_assertions/block-references-are-specific-to-obsidian]]"
  - "[[30_assertions/plain-text-meets-archival-format-criteria]]"
  - "[[30_assertions/card-index-organizes-knowledge-as-addressable-linked-notes]]"
  - "[[30_assertions/critical-apparatus-binds-reading-to-witnesses]]"
  - "[[30_assertions/prov-models-entities-activities-agents]]"
  - "[[30_assertions/prov-validity-is-internal-consistency]]"
  - "[[30_assertions/prov-derivation-conditions-unspecified]]"
  - "[[30_assertions/status-ladder-is-machine-enforced-and-takes-the-minimum-of-the-anchors]]"
  - "[[30_assertions/llm-summaries-broaden-the-scope-of-findings]]"
  - "[[30_assertions/llm-evaluators-favor-their-own-generations]]"
  - "[[30_assertions/cross-family-evaluator-panels-reduce-intra-model-bias]]"
  - "[[30_assertions/first-review-pass-concentrates-at-the-distillate-layer]]"
  - "[[30_assertions/modality-drift-is-the-most-frequent-recorded-defect]]"
  - "[[30_assertions/no-recorded-verdict-was-contradicts-or-not-in-the-text]]"
  - "[[30_assertions/agentic-context-engineering-as-design-task]]"
  - "[[30_assertions/agentic-promptotyping-knowledge-base-artifact]]"
posits: 6
created: 2026-08-21
updated: 2026-08-21
---

# Grounded Vault and the Support Gap

## Abstract

Generated prose can cite accessible documents while leaving many sentences unsupported by the cited passages.[^1] Grounded Vault addresses this support gap through a five-layer repository architecture in which output sentences resolve through assertions and source-specific anchors to recorded material.[^6] Deterministic validation checks the form and resolution of the chain, adversarial machine review judges each support relation, and human verification alone establishes evidence.[^20] A first review pass over the research instance reported 501 support pairs across 46 documents and located most checking work at the distillate layer.[^24] The architecture makes the state of support inspectable while leaving factual truth and substantive text quality to further judgment.[^4]

## The support gap

An audit of generative search systems found that 74.5 percent of citations supported the sentence to which they were attached and that 51.5 percent of generated sentences were fully supported by their citations.[^1] Studies of generated scholarly references found fabrication rates of 55 percent for one earlier chat model and 18 percent for its successor, while retrieval-based legal research systems retained hallucination rates between 17 and 33 percent in the reported evaluation.[^2] A citation can also resolve to a real document and fail because the response misinterprets that document or selects an inapplicable passage, which makes detection depend on opening and comparing the source.[^3]

Attribution research treats support by a supplied source as a separate judgment from the factual correctness of the generated statement.[^4] Classical historical method uses a related sequence in which the origin and transmission of a document are examined before its credibility is assessed.[^5] Grounded Vault turns this separation into an artefact structure that prepares support relations for inspection.[^29]

## The layer chain

The architecture arranges work across sources, Markdown representations, distillates, assertions, and output.[^6] Each layer carries its own anchor form, while the source layer remains the ground against which later forms can be checked.[^6] Anchors are minted only by their own layer and each layer points directly to the layer beneath it.[^7]

The storage conditions of a source determine its source type and therefore its anchor form.[^8] Storable documents use block references into an immutable Markdown representation, citable publications use checked verbatim quotations, and data findings use deterministic computations.[^8] A revised document enters as a new dated representation so existing block anchors continue to resolve.[^9]

The output contract places a footnote to an assertion on every load-bearing sentence and marks unsupported conclusions as posits with an explicit evidence question.[^10] Assertions are the synthesis layer where statements from different source types converge before they can enter the manuscript.[^6] The status mirror in the chapter frontmatter allows validation to compare the declared assertion set and posit count with the footnotes that occur in the text.[^10]

## The file substrate

The reference implementation uses Markdown files in an Obsidian vault, which remains an ordinary folder on the local file system.[^11] Obsidian keeps derived metadata in a rebuildable cache, so the authored notes remain accessible to other editors and file tools.[^11] A block reference is a literal identifier written into the note and addressed through the link syntax.[^12]

This anchor form introduces a portability boundary because block references belong to Obsidian Flavored Markdown and do not function as standard Markdown links outside the application.[^13] Preservation guidance accepts plain text as an open format while ranking structured text formats higher for published textual works because plain text can lose structure, context, and embedded metadata.[^14] The repository therefore preserves inspectable authored files while its block-level navigation depends on a documented application convention.[^30]

## Intellectual precedents

The fixed address and dense reference structure of the scholarly card index provides a precedent for knowledge organised as addressable linked notes.[^15] The critical apparatus of the Text Encoding Initiative binds readings to identified witnesses through pointers that resolve against a witness register.[^16] Grounded Vault adapts both practices to a production chain in which machine generated statements remain attached to named source locations.[^29]

The World Wide Web Consortium provenance model describes entities, activities, and responsible agents together with relations that record what happened.[^17] Its validity constraints establish the internal consistency of a provenance record and provide no direct verdict on the truth of the recorded content.[^18] The model also leaves the conditions under which a derivation holds to an external determination, even though usage, generation, and influence participate in the relation.[^19]

## Grounding and evidence

Grounding records that a statement points to a source location. Attribution research gives that support relation its own evaluation axis and keeps factual correctness outside the attribution verdict.[^4] Grounded Vault reserves `verified` for human judgment and permits validation plus machine review to raise a document only to `validated`.[^20]

The status of every document is bounded by the lowest status among the anchors on which it rests.[^20] Dated entries in the `checked` map record which checking operations actually ran.[^20] Contested and superseded anchors sit outside the ascending status ladder and keep dependent documents at the entry status.[^20]

## Agentic production and review

Promptotyping organises project work around a maintained and versioned knowledge base whose documents can enter a task-specific working context.[^28] Context engineering treats the selection and maintenance of that context as an engineering task, with experimental evidence that the position and volume of relevant information affect model performance.[^27] Grounded Vault adds a production schema for knowledge that must remain traceable through later synthesis.[^31]

Machine-generated summaries of research texts broaden the scope of original findings more often than the source abstracts, including under prompts that ask for accuracy.[^21] Pairwise review therefore compares a bare statement with its named source location and withholds the producing agent's reasoning.[^20] Language model evaluators have shown preference for their own generations, and this preference correlates with their capacity to recognise those generations.[^22] Evaluator panels drawn from disjoint model families reduced intra-model bias in the reported experiments.[^23]

## Findings from the first review pass

The first recorded machine review pass covered 501 pairs across 46 documents, with 405 pairs at the distillate layer, 87 at the assertion layer, and 9 at the chapter layer.[^24] This distribution places about four fifths of the pairwise checking work at the first statement layer above the source representations.[^24]

The review record contains 101 verdicts below full support.[^25] Modality drift accounts for 32 recorded defects, followed by 19 scope mismatches, 18 reaches into a neighbouring block, and 17 unanchored details.[^25] The computation yields category counts and no failure rate because the number of reviewed pairs does not come from that dataset.[^25] None of the recorded verdicts used the two harshest labels, `contradicts` and `not in the text`, and the record cannot establish whether unrecorded verdicts used them.[^26]

The concentration of findings at the distillate layer indicates where this instance spent its review effort.[^24] Generalisation beyond the instance requires comparable runs on other source sets and with independently recorded review logs.[^32]

## Limits of the method

A resolvable anchor guarantees traceability to a recorded location.[^7] The support relation still requires review, and attribution alone supplies no verdict about factual correctness.[^4] Internal consistency of provenance also leaves trust decisions to a later judgment.[^18]

The architecture has not been compared with an equivalent unanchored writing process under controlled conditions.[^33] Its current evidence supports claims about traceability, conformance, and the distribution of recorded review findings.[^24] A claim that the method improves substantive output quality requires a separate comparison.[^33]

Full anchor depth also depends on retaining the source material when the Markdown representation and its block identifiers are created.[^9] Retrospective reconstruction can document a later source state but cannot prove that it matches the material used in the earlier transformation.[^34] This dependency is why the source situation and storage rights are decided at intake.[^8]

[^1]: Grounded in [[30_assertions/generated-citations-often-fail-to-support-their-sentences]].
[^2]: Grounded in [[30_assertions/source-binding-lowers-unsupported-citation-without-eliminating-it]].
[^3]: Grounded in [[30_assertions/resolvable-citation-without-support-is-a-distinct-error-class]].
[^4]: Grounded in [[30_assertions/attribution-is-separate-from-correctness]].
[^5]: Grounded in [[30_assertions/historical-method-separates-origin-check-from-credibility]].
[^6]: Grounded in [[30_assertions/layer-model-assigns-each-layer-its-anchor-form]].
[^7]: Grounded in [[30_assertions/anchors-are-minted-at-their-own-layer-and-bind-one-layer-down]].
[^8]: Grounded in [[30_assertions/source-type-follows-storability-and-fixes-the-anchor-form]].
[^9]: Grounded in [[30_assertions/markdown-representation-is-immutable-after-ingest]].
[^10]: Grounded in [[30_assertions/output-binds-load-bearing-sentences-by-footnote-and-marks-posits]].
[^11]: Grounded in [[30_assertions/obsidian-stores-notes-as-plain-text-with-rebuildable-derived-state]].
[^12]: Grounded in [[30_assertions/block-references-address-blocks-as-literal-text-markers]].
[^13]: Grounded in [[30_assertions/block-references-are-specific-to-obsidian]].
[^14]: Grounded in [[30_assertions/plain-text-meets-archival-format-criteria]].
[^15]: Grounded in [[30_assertions/card-index-organizes-knowledge-as-addressable-linked-notes]].
[^16]: Grounded in [[30_assertions/critical-apparatus-binds-reading-to-witnesses]].
[^17]: Grounded in [[30_assertions/prov-models-entities-activities-agents]].
[^18]: Grounded in [[30_assertions/prov-validity-is-internal-consistency]].
[^19]: Grounded in [[30_assertions/prov-derivation-conditions-unspecified]].
[^20]: Grounded in [[30_assertions/status-ladder-is-machine-enforced-and-takes-the-minimum-of-the-anchors]].
[^21]: Grounded in [[30_assertions/llm-summaries-broaden-the-scope-of-findings]].
[^22]: Grounded in [[30_assertions/llm-evaluators-favor-their-own-generations]].
[^23]: Grounded in [[30_assertions/cross-family-evaluator-panels-reduce-intra-model-bias]].
[^24]: Grounded in [[30_assertions/first-review-pass-concentrates-at-the-distillate-layer]].
[^25]: Grounded in [[30_assertions/modality-drift-is-the-most-frequent-recorded-defect]].
[^26]: Grounded in [[30_assertions/no-recorded-verdict-was-contradicts-or-not-in-the-text]].
[^27]: Grounded in [[30_assertions/agentic-context-engineering-as-design-task]].
[^28]: Grounded in [[30_assertions/agentic-promptotyping-knowledge-base-artifact]].
[^29]: Posit: The combination of these established practices with the layer architecture is the manuscript's methodological synthesis. Open evidence question: Which earlier systems combine the same practices under an equivalent evidence contract?
[^30]: Posit: The repository combines file-level portability with application-specific block navigation. Open evidence question: Which portable anchor convention preserves the same paragraph-level addressability across Markdown tools?
[^31]: Posit: Grounded Vault extends a maintained project knowledge base with a production schema for evidence-obligated output. Open evidence question: Which other context engineering methods enforce an equivalent sentence-to-source chain?
[^32]: Posit: The recorded distribution belongs to one instance and cannot establish a general defect distribution. Open evidence question: How does the distribution change across domains, source types, and reviewer families?
[^33]: Posit: No controlled comparison in this research foundation establishes a substantive quality gain over equivalent unanchored writing. Open evidence question: What blinded comparison can measure that effect while holding source access and model capability constant?
[^34]: Posit: A later source copy cannot prove identity with an unarchived earlier source state. Open evidence question: What external archival record could establish that identity after the fact?
