---
type: distillate
source-type: publication
reference: "rashkin2023attribution"
topics: ["[[Verification]]", "[[Provenance]]"]
status: validated
checked:
  quote: 2026-08-10
  validation: 2026-08-10
  machine-review: 2026-08-10
created: 2026-08-10
updated: 2026-08-10
---

# Distillate: Measuring Attribution in Natural Language Generation Models

The source defines Attributable to Identified Sources (AIS), a framework that judges whether a generated statement is corroborated by an identified source, and it separates that judgment explicitly from any judgment about the truth of the statement.

## Core statements

- The source presents AIS as an evaluation framework under which generated output about the external world is to be verified against an independent, provided source. ^s1
  > "we present an evaluation framework, Attributable to Identified Sources (AIS), stipulating that NLG output pertaining to the external world is to be verified against an independent, provided source" (rashkin2023attribution, p. 778)

- The source defines attribution as the accurate use of source documents to support generated text. ^s2
  > "In this article, we develop a framework for the evaluation of attribution, by which we mean the accurate use of source documents to support generated text." (rashkin2023attribution, p. 778)

- The source states that characteristics of the underlying source, such as source quality, and the fluency of the generated text can be measured using complementary metrics that are out of scope in this work, and that AIS can be used as a precondition for or in tandem with such metrics. ^s3
  > "AIS can be used as a pre-condition or in tandem with other metrics or evaluation frameworks to assess overall quality. For example, characteristics of the underlying source (such as "source quality"), the fluency of the generated text, and so forth, can be measured using complementary metrics that are out of scope in this work." (rashkin2023attribution, p. 779)

- The source defines a pair of a statement s and a time t as attributable to a set of parts P of some underlying corpus if a generic hearer will, with a chosen level of confidence, affirm "According to P, s", where s is interpreted relative to t. ^s4
  > "A pair (s, t) is attributable to a set of parts P of some underlying corpus K iff: A generic hearer will, with a chosen level of confidence, affirm the following statement: "According to P, s", where s is interpreted relative to time t." (rashkin2023attribution, p. 782)

- The source states the same affirmation test for the pair (E(c, s), t), which is attributable to a set of parts P if a generic hearer will, with a chosen level of confidence, affirm "According to P, E(c, s)", where E(c, s) is interpreted relative to t. ^s5
  > "The pair (E(c, s), t) is attributable to a set of parts P of some underlying corpus K iff: A generic hearer will, with a chosen level of confidence, affirm the following statement: "According to P, E(c, s)", where E(c, s) is interpreted relative to time t." (rashkin2023attribution, p. 787)

- The source states that AIS can hold only for system sentences whose explicature is a standalone proposition. ^s6
  > "Note that AIS can only hold for system sentences that have an explicature that is a standalone proposition (condition 3)." (rashkin2023attribution, p. 787)

- The source states that its full definition of AIS adds interpretability checks to the definition for standalone propositions and applies attribution to explicatures of system sentences. ^s7
  > "The definition is very similar to the earlier definition of AIS for standalone propositions, but with checks for interpretability, and with attribution applied to explicatures of system sentences." (rashkin2023attribution, p. 787)

- The source declines to make absolute judgments about the factuality of utterances. ^s8
  > "we avoid absolute judgments regarding "factuality" of utterances" (rashkin2023attribution, p. 781)

- The source assumes as a corollary that the source is a reference and that an actual system may select sources for their trustworthiness. ^s9
  > "As a corollary, we assume the source is a reference, and that an actual system may select sources for their trustworthiness." (rashkin2023attribution, p. 781)

- The source states that attribution of a system-generated response in relation to the source document can be established by considering what information the system response provides and whether that information is an accurate representation of information in the source document. ^s10
  > "Attribution of a system-generated response in relation to the source document can be established by considering the following: A. What is the information provided by the system response? B. Is this information an accurate representation of information in the source document?" (rashkin2023attribution, p. 788)

- The source maps the first annotation step onto determining the explicature and the second onto the "according to" test. ^s11
  > "Step A corresponds to ascertaining the explicature of the system response; Step B corresponds to the "according to" test." (rashkin2023attribution, p. 788)

- The source states that AIS does not set policy about where model output should fall and that its users still need to decide where to draw the line. ^s12
  > "AIS does not set policy about where model output should fall: Its users still need to decide where to draw the line." (rashkin2023attribution, p. 808)

- The source reports that annotators inevitably draw on personal world knowledge as statements and evidence grow more complex, and calls the resulting ground truth ambiguous. ^s13
  > "as statements and evidence become more complex, annotators inevitably draw inferences using personal world knowledge. This is unavoidable and is inherently noisy (Pavlick and Kwiatkowski 2019); ground truth is ambiguous, just as journalists, researchers, or judges often legitimately disagree." (rashkin2023attribution, p. 808)

- The source limits AIS to propositions judgeable by the "according to" test and excludes questions without presuppositions and imperatives. ^s14
  > "AIS is limited to propositions that can be judged with the "according to" framework. AIS is not applicable to questions (without presuppositions) or imperatives (commands and requests)." (rashkin2023attribution, p. 809)

- The source reports that the overall reported quality is in the high nineties for all three of its tasks, with slight variations. ^s15
  > "The overall reported quality is in the high nineties for all three tasks with slight variations." (rashkin2023attribution, p. 797)

## Terms

- **Attributable to Identified Sources (AIS)**: the property of a system statement that a generic hearer would affirm "According to P, s" for the identified source parts P, judged on the explicature of the statement and its time of interpretation (rashkin2023attribution, pp. 782, 787).
- **Attribution**: the accurate use of source documents to support generated text (rashkin2023attribution, p. 778).
- **Explicature**: the paraphrase of a sentence that is interpretable in the linguistically empty context and preserves the truth-conditional meaning the sentence has in its context (rashkin2023attribution, p. 785).
- **Standalone proposition**: a declarative sentence that is interpretable once a time of interpretation has been specified (rashkin2023attribution, p. 782).

## Open questions

- The source leaves open how attribution is to be judged for utterances whose explicature is a question rather than a proposition, and names this as future work.
- The source assumes the grounding source is explicitly defined and does not settle how AIS behaves where grounding is indirect or requires background knowledge.
- The source separates attribution from factuality but does not specify what a source-quality metric that would carry the factuality judgment looks like.

## Appraisal

The venue is a peer-reviewed journal of record for the field, and the article is the reference definition that later attribution and citation work cites rather than redefines. Its value for this vault lies in the conceptual separation it draws, since a structural relation between a statement and an identified source can be established without any claim that the statement is true, which is exactly the distinction between grounding and evidence that this vault's architecture rests on. The limits are equally usable: the framework is defined for propositions and leaves questions, imperatives and indirect grounding outside, and its own authors report that human judgment of the relation is noisy where inference and world knowledge enter. The vault takes the definition as the standard it aligns its terminology to, and reads the reported annotator noise as an argument for keeping the verification instance human rather than as a defect of the framework.

## Related

- [[20_distillates/documents/gao-2023-llms-generate-text-with-citations]]
- [[20_distillates/documents/liu-2023-evaluating-verifiability-generative-search-engines]]
