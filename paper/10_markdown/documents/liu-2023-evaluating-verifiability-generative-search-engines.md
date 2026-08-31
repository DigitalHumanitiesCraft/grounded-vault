---
type: representation
source-type: document
source: "[[00_sources/2023.findings-emnlp.467.pdf]]"
converter: "pdftotext (poppler), default column mode"
channel: collection
scope: "abstract, introduction, the full metric definitions of section 2, the evaluation setup of section 3, the results and analyses of sections 4.1 to 4.4 and the conclusion; the related work of section 5 and all appendices are not represented"
metadata:
  title: "Evaluating Verifiability in Generative Search Engines"
  creator: "computer science research, Stanford University"
  date: "2023-12"
  format: "pdf"
  identifier: "https://doi.org/10.18653/v1/2023.findings-emnlp.467"
  license: "CC-BY-4.0"
  confidential: false
created: 2026-08-10
updated: 2026-08-10
---

# Evaluating Verifiability in Generative Search Engines

> Represented scope: abstract, introduction, the full metric definitions of section 2, the evaluation setup of section 3, the results and analyses of sections 4.1 to 4.4 and the conclusion; the related work of section 5 and all appendices are not represented

## Abstract

Generative search engines directly generate responses to user queries, along with in-line citations. A prerequisite trait of a trustworthy generative search engine is verifiability, i.e., systems should cite comprehensively (high citation recall; all statements are fully supported by citations) and accurately (high citation precision; every cite supports its associated statement). We conduct human evaluation to audit four popular generative search engines—Bing Chat, NeevaAI, perplexity.ai, and YouChat— across a diverse set of queries from a variety of sources (e.g., historical Google user queries, dynamically-collected open-ended questions on Reddit, etc.). We find that responses from existing generative search engines are fluent and appear informative, but frequently contain unsupported statements and inaccurate citations: on average, a mere 51.5% of generated sentences are fully supported by citations and only 74.5% of citations support their associated sentence. We believe that these results are concerningly low for systems that may serve as a primary tool for information-seeking users, especially given their facade of trustworthiness. We hope that our results further motivate the development of trustworthy generative search engines and help researchers and users better understand the shortcomings of existing commercial systems. ^b01


## 1 Introduction

Generative search engines fulfill user information needs by directly generating responses to input queries, along with in-line citations (Figure 1).1 Existing generative search engines are rapidly gaining users—in March 2023, Microsoft reported that "roughly one third of daily preview users are using [Bing] Chat daily", and that Bing Chat served 45 million chats in the first month of its public preview (Mehdi, 2023). Generative search engines have the potential to transform how people find information online, but generated responses from existing large language model-backed generative search engines may not always be accurate (Maynez et al., 2020). Given their potential and rapid mainstream adoption, it is critical to evaluate these systems to better understand their potential limitations (akin to prior work in algorithmic auditing; Metaxas and Pruksachatkun, 2017; Buolamwini and Gebru, 2018; Kiritchenko and Mohammad, 2018; Robertson et al., 2018; Metaxa et al., 2019; Green and Chen, 2019; Birhane et al., 2022, inter alia). ^b02

A prerequisite trait of a trustworthy generative search engine is verifiability,2 that is, each generated statement about the external world should be fully supported by a set of in-line citations, and each provided citation should support its associated statement. Verifiability enables readers to easily check that any generated statement is supported by its cited source. ^b03

We conduct a human evaluation to audit four popular commercial generative search engines (Bing Chat, NeevaAI, perplexity.ai, and YouChat) across a diverse set of information-seeking queries (e.g., various types of historical Google user queries from NaturalQuestions (Kwiatkowski et al., 2019), dynamically-collected open-ended questions from Reddit; see Appendix A for examples). ^b04

For each query-response pair, we use human evaluation to measure a variety of dimensions: ^b05

1. fluency (whether the generated text is fluent and cohesive; 2.2); ^b06

2. perceived utility (whether the generated answer is helpful and informative; 2.2); ^b07

3. citation recall (the proportion of generated statements about the external world that are fully supported by their citations; 2.3); and ^b08

4. citation precision (the proportion of generated citations that support their associated statements; 2.4). ^b09

A trustworthy generative search engine should achieve high citation recall and precision, indicating that its generated citations are comprehensive (every generated statement is fully supported by citation) and correct (every citation supports its associated statement). ^b10

We find that existing generative search engine responses often have high fluency and perceived utility (4.1), but frequently contain unsupported statements or inaccurate citations (low citation recall and precision; 4.2). On average, merely 51.5% of generated sentences are fully supported with citations (citation recall), and only 74.5% of citations support their associated sentence (citation precision). Furthermore, citation precision is inversely correlated with perceived utility (r = -0.96); the responses that seem more helpful are often those with inaccurate citations (4.3). This facade of trustworthiness increases the potential for existing generative search engines to mislead users. For example, in Figure 1, a user with little background knowledge about the James Webb Space Telescope (motivating a query about its recent discoveries) will likely struggle to identify unsupported statements in the generated response. We hypothesize that citation precision is inversely correlated with perceived utility because generative search engines often copy or closely paraphrase from their cited webpages (4.4). This improves citation precision because copied text is often supported by the cited webpage, but decreases perceived utility when copied statements are irrelevant to the query or the rest of the generated response. ^b11

We make the following contributions: first, we define the citation recall and citation precision evaluation metrics, which aim to encourage the development of systems that cite comprehensively and correctly. Second, we conduct a human evaluation of four popular generative search engines, finding that responses are broadly fluent and appear useful, but frequently contain unsupported statements and inaccurate citations, increasing their potential to mislead users. Third, we observe that perceived utility is inversely correlated with citation precision in existing generative search engines, and hypothesize that this inverse correlation occurs when some systems copy or closely paraphrase from cited webpages. To facilitate further work on developing trustworthy generative search engines, we have released our human evaluation annotations.3 ^b12


## 2 Human Evaluation of Fluency, Perceived Utility, and Verifiability

In this section, we formalize the inputs and outputs of the generative search engines we study, describe the evaluation of fluency and perceived utility, and define and describe the evaluation of citation recall and precision. Citation recall and precision are designed to reward systems that cite comprehensively (i.e., high recall; all statements are fully supported by citations) and accurately (i.e., high precision; every cite supports its associated statement). We also define citation F1, a metric that combines citation precision and citation recall. ^b13


### 2.1 Task Formulation

Given a user query q as input, a generative search engine produces a text response r, which is a string with embedded in-line citations. For the example in Figure 1, the query q is "What are the latest discoveries from the James Webb Space Telescope?" and the response r is the string paragraph "The James Webb Space Telescope ... used to study the next interstellar interloper [3].", with embedded citations "[1]", "[2]", and "[3]". ^b14

To evaluate citation precision and recall, we first segment the r into a set of n statements S = {s1, . . . , sn}. In this work, the segmentation S is set of sentences in the response r. For each statement si S, we construct a (possibly empty) set Ci = {ci,1, . . . , ci,k} of k citations associated with the statement si, where ci,j is the jth citation associated with the ith response statement. For each citation ci,j, we have a URL ui,j and its contents pi,j. In this work, Ci is set of citations that occur in si (e.g., for si = "Blueberries[1], cherries[2], and grapes[3] grow on trees.[4]", Ci = {[1], [2], [3], [4]}). ^b15

In practice, a sentence may contain multiple independently-verifiable claims (e.g., conjuncts such as "Cups can be made of glass[1] or plastic[2]."), and a single in-line citation's scope is often ambiguous (e.g., a cite marker after two statements could be interpreted as either supporting both statements, or merely the final one); we leave finer-grained evaluation to future work. ^b16


### 2.2 Measuring Fluency and Perceived Utility

To measure response fluency, annotators were shown the user query, the generated response, and the claim "The response is fluent and cohesive". We ask annotators to rate their level of agreement with the claim on a five-point Likert scale from Strongly Disagree to Strongly Agree. We use a similar process to measure perceived utility, asking annotators to rate their level of agreement with the claim "The response is a helpful and informative answer to the query". ^b17


### 2.3 Measuring Citation Recall

Citation recall is the proportion of verificationworthy statements that are fully supported by their associated citations (see Figure 2 for several examples). Thus, computing citation recall requires (i) identifying the verification-worthy statements in a response and (ii) evaluating whether each verification-worthy statement is fully supported by its associated citations. ^b18

Identifying verification-worthy statements. Given the statements S in a response r, we first ask annotators to remove statements in the response that are not verification-worthy. We take the position that every generated statement about the external world is verification-worthy, even those that might seem obvious, trivially true, or "common sense". Generated statements may be incorrect, and statements that seem obvious to some readers may be less than obvious to others (e.g., "The Pope is Catholic"). We believe that systems should aim to provide a source for all generated statements about the external world, enabling readers to easily verify any statement in a generated response. ^b19

In practice, almost all system-generated statements are verification-worthy—notable exceptions include statements about the speaker (the system) itself (e.g., "As a language model, I do not have the ability to ban books.") and questions posed to the user (e.g.,"Would you like to learn more?", generated by systems like Bing Chat and YouChat that are deployed in conversational settings). ^b20

Evaluating whether a verification-worthy statement is fully supported by its associated citations. Given the verification-worthy statements in a response r, annotators evaluate whether each statement is fully supported by its associated citations (see the sentences of generated response in Figure 1 for examples). To collect these binary judgments, we use the attributable to identified sources (AIS) evaluation framework of Rashkin et al. (2022). In particular, a statement si is fully supported by its associated citations Ci if a generic hearer would affirm the statement "According to cited webpages Ci, si", within the context of the query q and response r, and unsupported otherwise. ^b21


### 2.4 Measuring Citation Precision

Citation precision is the proportion of generated citations that support their associated statements (Figure 2). In contrast to citation recall, citation precision rewards systems for citing accurately—a response that cites every webpage on the Internet for each generated statement would have high citation recall, but low citation precision (since many articles are irrelevant and do not support their associated statement). To measure citation precision for a response r, we first ask annotators to judge whether each citation ci,k contributes full, partial, or no support for its associated statement si (see cited webpages in Figure 1 for examples): ^b22

Full support: all of the information in the statement is supported by the citation. ^b23

Partial support: some of the information in the statement is supported by the citation, but other parts are not supported (e.g., missing or contradictory). ^b24

No support: the citation does not support any part of the statement (e.g., the cited webpage is completely irrelevant or contradictory). ^b25

For statements that have multiple associated citations, we additionally ask annotators whether the union of its associated cited webpages collectively provides full support for the statement (a binary judgment). Similar to citation recall, we use the AIS evaluation framework of Rashkin et al. (2022) to collect these binary judgments. ^b26

To calculate citation precision, let Tfs be the number of citations that fully support its associated statement, and let Tps be the number of citations that partially supports its associated statement, where the associated statement is fully supported by the union of its associated citations and no associated citation fully supports the statement by itself.4 Let N be the total number of citations in the response. Then, the citation precision is (Tfs + Tps)/N . ^b27


### 2.5 Citation F1

Citation F1 is a metric that combines citation precision and citation recall by taking their harmonic mean: ^b28

To achieve a high citation F1, systems must have high citation precision and high citation recall. ^b29


## 3 Evaluation Setup

In this section, we describe the evaluated generative search engines (3.1), the diverse query distributions we use for evaluation (3.2), and the details of our human evaluation protocol (3.3). ^b30


### 3.1 Evaluated Generative Search Engines

We evaluate four existing commercial generative search engines: Bing Chat, NeevaAI, perplexity.ai, and YouChat. 5 These systems pattern after prior work (e.g., Nakano et al., 2021; Menick et al., 2022; Glaese et al., 2022; Thoppilan et al., 2022, inter alia) and generate responses by conditioning large language models on the input query and retrieved content (e.g., search results from a conventional search engine). For each input, we save the system's first complete response (i.e., single-turn). Responses were scraped between late February and late March 2023. ^b31

Note that evaluated generative search engines have differing abstention rates (Table 1), which can make direct comparison difficult—one might expect that systems with higher abstention rates might also have higher evaluation performance, since they can simply abstain from generating responses to difficult queries (we do not find this to be the case in practice). NeevaAI abstains from responding on nearly 23% of evaluated queries, since its response is displayed within a conventional search engine results page. In contrast, Bing Chat, perplexity.ai, and YouChat respond to almost every user query. ^b32


### 3.2 Evaluated Query Distributions

To gain a broader understanding of the strengths and weaknesses of existing commercial generative search engines, we evaluate on a diverse set of queries from a variety of sources (e.g., Google user queries, open-ended Reddit questions, how-to queries) requiring knowledge from several different answer types (e.g., short textual spans, long-form paragraph, lists, or tables). See Appendix A for example queries from each distribution. Each system is evaluated on 1450 queries—150 randomlysampled queries from each of AllSouls, davincidebate, ELI5 (KILT / Live), and WikiHowKeywords, and 100 randomly-sampled queries for each of the seven NaturalQuestions subdistributions. ^b33

AllSouls. We evaluate systems on open-ended essay questions taken from the entrance exam (general paper component) for All Souls College, Oxford University. These questions cover topics including the arts, science, politics, literature, current events, and issues in education and sport. ^b34

davinci-debate. We evaluate systems on debate topics generated from text-davinci-003. To generate debate queries, we follow the procedure of Bakker et al. (2022); see Appendix B.1 for details. ^b35

ELI5. We take queries from the "Explain Like I'm Five" (ELI5) subreddit, where users provide long-form layperson-accessible answers to submitted questions. Submitted questions are required to admit objective explanations, and answering them often requires long-form textual responses. ^b36

We consider two subdistributions of ELI5 queries: ELI5 (KILT) and ELI5 (Live). ELI5 (KILT) uses historical queries from the KILT ELI5 dataset (Fan et al., 2019; Petroni et al., 2021), drawn from posts created before July 2018. A retrieval-based system could hypothetically perform well on ELI5 (KILT) by simply identifying the query's source Reddit ELI5 post and copying its content. As a result, we also evaluate generative search engines on the ELI5 (Live) subdistribution, which increases ecological validity by evaluating systems on real user queries at their time of creation and reducing the incidence of search results with the query's exact keywords. 6 We continuously listen to the stream of new Reddit ELI5 posts and immediately query generative search engines for responses whenever a new post is created. This ensures that the source ELI5 post will not have been indexed (and thus, cannot be retrieved) by conventional search engines. minimizing the possibility that the generative search engine has access to the source ELI5 post. ^b37

WikiHowKeywords. We evaluate systems on queries derived from WikiHow articles. We found that directly querying generative search engines with WikiHow article titles yields responses that largely paraphrase or copy text directly from WikiHow. As a result, we use text-davinci-003 to paraphrase article titles (e.g., "How to Cut An Avocado") into keyword queries (e.g., "cut avocado"). ^b38

NaturalQuestions. We evaluate generative search engines on NaturalQuestions (Kwiatkowski et al., 2019) queries, stratified by their answer type. NaturalQuestions contains historical queries issued to the Google search engine coupled with long and short answers extracted from Wikipedia. We evaluate on queries from 7 NaturalQuestions subdistributions: queries with paragraph-type long answers (i) with and (ii) without short answers, queries with list-type long answers (iii) with and (iv) without short answer, queries with table-type long answers (v) with and (vi) without short answers, and finally (vii) queries with no long answer (and thus no short answer either). ^b39

Summary. In total, we evaluate existing generative search engines on 12 total query distributions. Eight query distributions are taken from prior work (ELI5 (KILT) and the seven NaturalQuestions query distributions), while four query distributions were constructed for this work: AllSouls, davinci-debate, ELI5 (Live), and WikiHowKeywords. These diverse settings provide broad coverage of several potential use cases and information needs, helping us gain a comprehensive understanding of systems' strengths and weaknesses. ^b40


### 3.3 Human Evaluation Protocol

Annotation process. Evaluating a single queryresponse pair requires human annotators to complete a three-step The first step measures the response's fluency and perceived utility (2.2), and the second and third step provide the judgments necessary to measure citation recall (2.3) and precision (2.4). See Appendix C for screenshots of the annotation interface and Appendix D for the annotation guidelines. ^b41

Annotator recruitment and training. Annotation was performed on Amazon Mechanical Turk. Annotators were pre-screened with a qualification study, which required them to read an annotation guidelines document and evaluate five representative query-response pairs. We individually reviewed submitted annotations for qualification study and provided annotators with personalized feedback to help correct any misconceptions or confusion about the task. Annotators who performed well on the qualification study and demonstrated thorough understanding of the task and annotation guidelines were permitted to participate in the main round of human evaluation. We remained in constant contact with annotators throughout the human evaluation process to answer questions about corner-cases and clarify intended behavior. In total, 34 annotators participated in human evaluation. ^b42

Annotator compensation. Annotators were compensated $1.00 per query-response pair for responses with citations, and $0.38 per queryresponse pair for responses without citations ($15.00 per hour, by conservative time estimates). On average, annotators took approximately four minutes to complete all three steps for a single query-response pair for responses that contained at least one citation. ^b43

Annotation agreement. Each query-response pair is annotated once in the human evaluation process. To measure inter-annotator agreement, we collected three annotations for 250 randomlysampled query-response pairs, finding high agreement rates (greater than 82.0% pairwise agreement and 91.0 F1 for all judgments; see Appendix E). ^b44


## 4 Results and Analysis

This section presents the results of our human evaluation study and discusses our main observations and analyses. We see that fluency and perceived utility are generally high across different generative search engines (4.1), while citation recall and precision are quite low (4.2), though performance certainly varies by system and query distribution—the low citation recall and precision, when combined with the facade of trustworthiness from fluency and high perceived utility, increase the potential for existing generative search engines to mislead users. Our results also show that citation precision is inversely correlated with perceived utility in existing generative search engines (4.3). We hypothesize that this is a byproduct of systems' propensity to copy or closely paraphrase text from cited webpages, which may increase citation precision and decrease perceived utility (4.4). ^b45


### 4.1 Fluency and Perceived Utility

Generated responses are fluent and appear helpful. Averaging across all systems and responses yields an average rating of 4.48 for fluency and 4.50 for perceived utility, indicating that annotators generally found generated responses fluent and helpful for answering the user's input query. ^b46

Comparing fluency and perceived utility between generative search engines. Comparing fluency and perceived utility ratings between the generative search engines (aggregated over all responses), we see that Bing Chat receives the lowest fluency / perceived utility ratings (4.40 / 4.34), followed by NeevaAI (4.43 / 4.48), perplexity.ai (4.51 / 4.56), and YouChat (4.59 / 4.62). ^b47

Comparing fluency across query distributions. Comparing average fluency ratings across different query distributions, we see similar ratings between NaturalQuestions queries that have a long answer (i.e., an extractive answer of some length exists on Wikipedia) and non-NaturalQuestions distributions (4.50 vs. 4.47, respectively). Comparing average fluency ratings between NaturalQuestions subdistributions, we see that generated responses to queries that have a short extractive answer are generally more fluent (4.55) than responses to queries with only a long answer (4.46) or those without a long answer (4.46), perhaps because responses to questions with short answers are generally shorter and often only require factoid knowledge. ^b48

A notable outlier distribution is NaturalQuestions queries with table-type long answers and no short answers, where system responses are dramatically less fluent (average of 4.36 across systems vs. average of 4.48 across all query distributions). These challenging queries often require aggregating information across table cells or retrieved sources, since the lack of a short answer implies that no single Wikipedia table cell directly answers the question (e.g., the query "how many grammys does beyonce have without destiny's child"). When the retrieved webpages do not contain a clear extractive answer to the query, but contain facts that seem relevant (e.g., information about Destiny's Child's first Grammy, or Beyonce's total number of career Grammy awards), the generated response is often a stilted agglomeration of statements from various sources, reducing overall fluency. ^b49

Comparing perceived utility across query distributions. In contrast to fluency, perceived utility can differ substantially between different query distributions. Perceived utility is much higher for NaturalQuestions queries containing a long answer (4.59), as opposed to non-NaturalQuestions queries (4.43). Comparing between different NaturalQuestions subdistributions, we see that perceived utility is highest for queries that have a short answer (4.62), followed by queries that have only a long answer (4.55), and finally by queries that have no long (or short) answer (4.52). Overall, perceived utility decreases as queries require longer-form and lessextractive answers (e.g., factoid NaturalQuestions queries with short answers versus ELI5 queries). ^b50


### 4.2 Citation Recall and Precision

Existing generative search engines often do not cite comprehensively or correctly. When averaging across all systems, a mere 51.5% of generated statements are fully supported with citations (recall), and only 74.5% of citations fully support their associated statements (precision). We believe these results are unacceptably low for systems that are quickly becoming a popular tool for answering user queries and already have millions of users, especially given that generated responses often appear informative and useful. ^b51

Comparing citation recall and precision between generative search engines. Citation recall and precision varies dramatically between different generative search engines. perplexity.ai achieves the highest average recall (68.7), compared to NeevaAI (67.6), Bing Chat (58.7), and YouChat (11.1). On the other hand, Bing Chat achieves the highest average precision (89.5), followed by perplexity.ai (72.7), NeevaAI (72.0), and YouChat (63.6). A gap of nearly 58% separates the system with the highest and lowest recall (perplexity.ai vs. YouChat), and the gap between the systems with the highest and lowest precision is almost 25% (Bing Chat vs. YouChat). ^b52

Comparing citation recall across query distributions. Modifying the evaluation query distribution appears to affect citation recall more than citation precision. For example, the gap in citation recall between NaturalQuestions queries with a long answer and non-NaturalQuestions queries is nearly 11% (58.5 vs. 47.8, respectively). Similarly, the difference in citation recall between NaturalQuestions queries with and without short answers is nearly 10% (63.4 for queries with a short answer, 53.6 for queries with only a long answer, and 53.4 for queries with no long or short answer). ^b53

We hypothesize that citation recall is driven by the relevance of retrieved webpages. In the absence of retrieved evidence that directly answers the input user query, systems generate statements that are unsubstantiated by citations, resulting in lower recall. For example, generative search engines struggle with citation recall when evaluated on the open-ended AllSouls essay questions (average recall of 44.3), because these queries generally have no extractive answer on the Internet. ^b54

Comparing citation precision across query distributions. Precision on NaturalQuestions queries with long answers is higher than nonNaturalQuestions distributions (76.1 vs. 72.3, respectively). Precision is highest on NaturalQuestions queries with paragraph answer types (precision of 81.5 when a short answer exists and 78.7 when only a long answer exists). On the other hand, citation precision is lowest when systems are evaluated on AllSouls open-ended essay questions (67.8) and davinci-debate queries (70.3). Comparing between NaturalQuestions subdistributions, average system precision is higher on queries with short answers (77.4) than those with only long answers (74.8) or no long answer (73.5). ^b55

Summary. To summarize our human evaluation results, Figure 3 plots average perceived utility against average citation F1. Existing systems make different trade-offs between citation recall, citation precision, and perceived utility. See Appendix H for full citation F1 results for every generative search engine on each of our query distributions. ^b56


### 4.3 Citation Precision is Inversely Related to Perceived Utility

We find that citation precision is inversely correlated with perceived utility in existing generative search engines (r = -0.96). For example, Bing Chat achieves the highest precision, but has the lowest perceived utility. In contrast, YouChat has the lowest citation precision, but its responses attain the highest perceived utility ratings. ^b57

This inverse relationship between citation precision and perceived utility is symptomatic of a trade-off between faithfulness and abstractiveness (Ladhak et al., 2022). In particular, we find that system-generated statements often closely paraphrase or directly copy from their associated citations (see 4.4 for further analysis). This results in high citation precision (since extractively copied text is almost always fully supported by the source citation), but lower perceived utility (since the extractive snippets may not actually answer the user's input query). In contrast, systems that frequently deviate from cited content (resulting in low citation precision) may have greater freedom to generate fluent responses that appear relevant and helpful to the user's input query. ^b58

This tradeoff is especially apparent on the AllSouls query distribution, which contains openended essay questions. AllSouls queries often cannot be answered via extraction from a single webpage on the Internet. For example, given the query "Is cooperation or competition the driving force guiding the evolution of society?", conventional search engine results focus on biological evolution, rather than societal evolution. Bing Chat simply copies irrelevant statements directly from the cited sources, resulting in high citation precision but low perceived utility (Figure 4). ^b59


### 4.4 Generative Search Engines Closely Paraphrase From Cited Webpages

To better understand how generative search engines use citations to support their responses, we analyze the similarity between generated statements and their supporting cited webpages. For citations that provide full or partial support for their associated statement, annotators were asked to provide evidence by copy-pasting the minimal set of sentences from the cited webpage that support their judgment (if any such sentences exist). We compute the BLEU (Papineni et al., 2002) and BERTScore (Zhang et al., 2020) between each generated statement and the annotator-provided evidence from the associated citation. For statements with multiple associated citations, we take the maximum similarity with any associated citation's evidence. ^b60

Table 2 presents similarity metrics between generated statements and extracted evidence from supporting webpages—when statements are fully or partially supported by their citations, they often copy or closely paraphrase from their cited articles. Furthermore, systems with higher similarity between their generated statements and cited webpages also have higher average citation precision (r = 0.80 between each of BLEU and BERTScore with average citation precision), indicating that their improved precision may largely be a byproduct of their increased tendency to copy or paraphrase from cited webpages. ^b61


## 6 Conclusion

In this work, we used human evaluation to audit the verifiability of four popular commercial generative search engines—Bing Chat, NeevaAI, perplexity.ai, and YouChat. We find that responses from existing generative search engines are generally fluent and often appear informative, but frequently contain unsupported statements and inaccurate citations (low citation recall and precision)—a mere 51.5% of generated statements are fully supported by citations (recall), and only 74.5% of citations support their associated statements (precision). We believe that existing systems' citation recall and precision are unacceptably low, given that they are quickly becoming a popular tool for answering user queries and already have millions of users. Moreover, we find that citation precision is inversely correlated with perceived utility in existing generative search engines—the responses that seem more helpful are often those with more unsupported statements or inaccurate citations. Analysis suggests that this inverse correlation occurs in existing systems because of their propensity to copy or closely paraphrase from cited webpages, which inflates citation precision at the cost of lower perceived utility. We hope our results and insights further motivate the development of trustworthy generative search engines and help researchers and users better understand their current shortcomings. ^b62
