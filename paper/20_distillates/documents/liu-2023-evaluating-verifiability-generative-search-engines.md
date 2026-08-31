---
type: distillate
source-type: document
representation: "[[10_markdown/documents/liu-2023-evaluating-verifiability-generative-search-engines]]"
topics: ["[[Verification]]", "[[Provenance]]"]
status: validated
checked:
  validation: 2026-08-10
  machine-review: 2026-08-10
created: 2026-08-10
updated: 2026-08-10
---

# Distillate: Evaluating Verifiability in Generative Search Engines

The source defines citation recall and citation precision as the two measures of verifiability and reports, from a human audit of four commercial generative search engines, how far deployed systems fall short of them.

## Core statements

- The source defines verifiability as the property that every generated statement about the external world is fully supported by its in-line citations and every citation supports the statement it is attached to. [[10_markdown/documents/liu-2023-evaluating-verifiability-generative-search-engines#^b03]] ^s1

- The source reports that on average a mere 51.5% of generated sentences are fully supported by citations and only 74.5% of citations support the sentence they are attached to. [[10_markdown/documents/liu-2023-evaluating-verifiability-generative-search-engines#^b01]] ^s2

- The source audits four commercial generative search engines, Bing Chat, NeevaAI, perplexity.ai and YouChat, by human evaluation. [[10_markdown/documents/liu-2023-evaluating-verifiability-generative-search-engines#^b04]] ^s3

- The source defines citation recall as the proportion of generated statements about the external world that are fully supported by their associated citations. [[10_markdown/documents/liu-2023-evaluating-verifiability-generative-search-engines#^b08]] ^s4

- The source defines citation precision as the proportion of generated citations that support their associated statements. [[10_markdown/documents/liu-2023-evaluating-verifiability-generative-search-engines#^b09]] ^s5

- The source states that a trustworthy generative search engine should achieve high citation recall and precision, indicating that its citations are comprehensive and correct. [[10_markdown/documents/liu-2023-evaluating-verifiability-generative-search-engines#^b10]] ^s6

- The source segments a response into sentences and treats each sentence as the statement unit whose citations are judged. [[10_markdown/documents/liu-2023-evaluating-verifiability-generative-search-engines#^b15]] ^s7

- The source notes that a sentence may carry several independently verifiable claims and that the scope of a single in-line citation is often ambiguous, and leaves finer-grained evaluation to future work. [[10_markdown/documents/liu-2023-evaluating-verifiability-generative-search-engines#^b16]] ^s8

- The source takes the position that every generated statement about the external world is verification-worthy, including statements that seem obvious or trivially true. [[10_markdown/documents/liu-2023-evaluating-verifiability-generative-search-engines#^b19]] ^s9

- The source collects the binary judgment of full support with the AIS framework, in which a statement counts as fully supported if a generic hearer would affirm "According to cited webpages, the statement" within the context of the query and response. [[10_markdown/documents/liu-2023-evaluating-verifiability-generative-search-engines#^b21]] ^s10

- The source defines full support of a statement by a citation as all of the information in the statement being supported by that citation. [[10_markdown/documents/liu-2023-evaluating-verifiability-generative-search-engines#^b23]] ^s11

- The source argues that citation precision is needed alongside recall because a response citing every webpage for each statement would have high recall and low precision. [[10_markdown/documents/liu-2023-evaluating-verifiability-generative-search-engines#^b22]] ^s12

- The source reports an average rating of 4.48 for fluency and 4.50 for perceived utility across all systems and responses. [[10_markdown/documents/liu-2023-evaluating-verifiability-generative-search-engines#^b46]] ^s13

- The source reports that citation recall varies from 68.7 for perplexity.ai down to 11.1 for YouChat, and citation precision from 89.5 for Bing Chat down to 63.6 for YouChat. [[10_markdown/documents/liu-2023-evaluating-verifiability-generative-search-engines#^b52]] ^s14

- The source reports that modifying the evaluation query distribution appears to affect citation recall more than citation precision, with a gap of nearly 11% in recall between NaturalQuestions queries with a long answer and non-NaturalQuestions queries (58.5 versus 47.8). [[10_markdown/documents/liu-2023-evaluating-verifiability-generative-search-engines#^b53]] ^s15

- The source hypothesizes that citation recall is driven by the relevance of the retrieved webpages, and reports an average recall of 44.3 on open-ended essay questions, which generally have no extractive answer on the Internet. [[10_markdown/documents/liu-2023-evaluating-verifiability-generative-search-engines#^b54]] ^s16

- The source reports that citation precision is inversely correlated with perceived utility across the audited systems, at r = -0.96. [[10_markdown/documents/liu-2023-evaluating-verifiability-generative-search-engines#^b57]] ^s17

- The source attributes the inverse relation to a trade-off between faithfulness and abstractiveness, in that extractively copied text is almost always fully supported by its citation while the copied snippet may not answer the query. [[10_markdown/documents/liu-2023-evaluating-verifiability-generative-search-engines#^b58]] ^s18

- The source reports that systems whose generated statements are more similar to their cited webpages also have higher average citation precision, at r = 0.80 between each of BLEU and BERTScore and average citation precision. [[10_markdown/documents/liu-2023-evaluating-verifiability-generative-search-engines#^b61]] ^s19

- The source concludes that the responses which seem more helpful are often those with more unsupported statements or inaccurate citations. [[10_markdown/documents/liu-2023-evaluating-verifiability-generative-search-engines#^b62]] ^s20

## Terms

- **Verifiability**: the property of a response that each generated statement about the external world is fully supported by its in-line citations and each citation supports its associated statement [[10_markdown/documents/liu-2023-evaluating-verifiability-generative-search-engines#^b03]]
- **Verification-worthy statement**: a generated statement about the external world, which the source treats as owing a citation regardless of how obvious it seems [[10_markdown/documents/liu-2023-evaluating-verifiability-generative-search-engines#^b19]]
- **Citation F1**: the harmonic mean of citation precision and citation recall [[10_markdown/documents/liu-2023-evaluating-verifiability-generative-search-engines#^b28]]

## Open questions

- The source judges a whole sentence against its citations and leaves open how to score a sentence whose several claims are supported unevenly.
- The source measures each query-response pair with a single annotation and does not settle how much of the reported spread is annotator variance.
- The source shows that precision rises with copying but does not say what an evaluation that rewards support without rewarding extraction would look like.

## Appraisal

This is the empirical counterpart to the definitional work on attribution: it takes the same AIS judgment and applies it to systems in production, which turns a conceptual distinction into a measurement of how often the citation relation actually holds. For this vault the most usable finding is the inverse correlation between citation precision and perceived utility, because it names a cost that a strictly grounded text pays, and it does so from data rather than from principle. The audit's limits are worth carrying forward, notably the single annotation per pair and the sentence as the unit of judgment, both of which put a floor under how fine the reported numbers can be read. The systems audited are commercial products of a particular moment, so the absolute figures date quickly while the mechanism they demonstrate does not.

## Related

- [[20_distillates/publications/rashkin-2023-measuring-attribution]]
- [[20_distillates/documents/gao-2023-llms-generate-text-with-citations]]
