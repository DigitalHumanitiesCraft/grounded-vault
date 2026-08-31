---
type: representation
source-type: document
source: "[[00_sources/2023.emnlp-main.398.pdf]]"
converter: "pdftotext (poppler), default column mode"
channel: collection
scope: "abstract, introduction, task setup, the full evaluation framework (sections 3.1 to 3.4), the main results of section 5.1, the human evaluation of section 6 and the conclusion; the modelling components of section 4, the experimental setup and ablations of section 5.2 to 5.4, the related work and all appendices are not represented"
metadata:
  title: "Enabling Large Language Models to Generate Text with Citations"
  creator: "computer science research, Princeton University"
  date: "2023-12"
  format: "pdf"
  identifier: "https://doi.org/10.18653/v1/2023.emnlp-main.398"
  license: "CC-BY-4.0"
  confidential: false
created: 2026-08-10
updated: 2026-08-10
---

# Enabling Large Language Models to Generate Text with Citations

> Represented scope: abstract, introduction, task setup, the full evaluation framework (sections 3.1 to 3.4), the main results of section 5.1, the human evaluation of section 6 and the conclusion; the modelling components of section 4, the experimental setup and ablations of section 5.2 to 5.4, the related work and all appendices are not represented

## Abstract

Large language models (LLMs) have emerged as a widely-used tool for information seeking, but their generated outputs are prone to hallucination. In this work, our aim is to allow LLMs to generate text with citations, improving their factual correctness and verifiability. Existing work mainly relies on commercial search engines and human evaluation, making it challenging to reproduce and compare different modeling approaches. We propose ALCE, the first benchmark for Automatic LLMs' Citation Evaluation. ALCE collects a diverse set of questions and retrieval corpora and requires building end-to-end systems to retrieve supporting evidence and generate answers with citations. We develop automatic metrics along three dimensions—fluency, correctness, and citation quality—and demonstrate their strong correlation with human judgements. Our experiments with state-of-the-art LLMs and novel prompting strategies show that current systems have considerable room for improvement—For example, on the ELI5 dataset, even the best models lack complete citation support 50% of the time. Our analyses further highlight promising future directions, including developing better retrievers, advancing long-context LLMs, and improving the ability to synthesize information from multiple sources.1 ^b01


## 1 Introduction

Large language models (LLMs; Brown et al., 2020; OpenAI, 2023) have gained increasing popularity as a tool for information seeking. While they generate engaging and coherent responses, their outputs are prone to hallucination and often contain factually incorrect information (Ji et al., 2023). This makes it harder for users to trust and verify LLMgenerated outputs without any supporting evidence. ^b02

In this work, we study a new generation paradigm for LLMs, in which we require LLMs to provide citations to one or a few text passages for any statement they generate (Figure 1). Incorporating citations brings several benefits: (1) users can easily verify LLMs' claims with the provided citations; (2) LLMs can generate text that faithfully follows cited passages, which has the promise to improve correctness and alleviate hallucination. ^b03

Multiple commercial systems have adopted this paradigm: Bing Chat2 and perplexity.ai3 respond to user questions in natural language with references to Web pages. Nakano et al. (2021); Menick et al. (2022) share a similar motivation, but they mainly experiment with commercial search engines and closed-source models, making their results difficult to evaluate. Retrieval-augmented LMs (Borgeaud et al., 2022; Izacard et al., 2022) incorporate retrieved passages during both training and inference, but do not guarantee faithfulness to retrieved passages or explicitly provide citations. Additionally, previous studies mostly rely on human evaluation (Nakano et al., 2021; Menick et al., 2022; Liu et al., 2023), which is expensive and difficult to reproduce. We argue that the absence of automated evaluation hinders the advances of such systems. ^b04

We present ALCE, the first reproducible benchmark for automatically evaluating LLMs' generations with citations. ALCE assumes a naturallanguage question and a retrieval corpus, and requires building end-to-end systems to retrieve relevant passages from the corpus, generate a response to the question, and cite corresponding supporting passages. We compile three datasets that cover different types of questions and corpora— ASQA (Stelmakh et al., 2022), QAMPARI (Rubin et al., 2022), and ELI5 (Fan et al., 2019)—as shown in Table 1. Different from previous benchmarks (Lee et al., 2019; Bohnet et al., 2022), ALCE evaluates long-text generation, focusing on automatically evaluating citation quality, and allows citing multiple passages for individual statements. ^b05

We design automatic evaluation methods in three dimensions: fluency, correctness, and citation quality. Specifically, we use MAUVE (Pillutla et al., 2021) to measure fluency, propose tailored correctness metrics for each dataset, and adopt a natural language inference (NLI) model (Honovich et al., 2022) to measure citation quality. We showcase how the three dimensions together contribute to a robust evaluation, preventing systems from exploiting shortcuts. Additionally, we conduct human evaluation and demonstrate a strong correlation with our automatic metrics. ^b06

We experiment on multiple systems with stateof-the-art LLMs and retrievers and also propose novel prompting strategies to synthesize retrieved text into text generation. Although all systems are capable of providing fluent and coherent responses, there remains substantial room for improvement in terms of correctness and citation quality: For example, on the ELI5 dataset, around 50% generations of our ChatGPT and GPT-4 baselines are not fully supported by the cited passages. Additionally, we find that (1) a closed-book model (generating answers without accessing any retrieved documents) with post-hoc citing achieves good correctness but much worse citation quality; (2) although interactive retrieval approaches (Yao et al., 2023; Schick et al., 2023) offer more flexibility in when/what to retrieve, they do not improve the performance on this challenging benchmark; (3) summarizing the retrieved passages in a shorter text improves correctness but not citation quality; (4) reranking multiple generations boosts citation quality measured by human evaluation; (5) incorporating more retrieved passages in context does not help ChatGPT but improves GPT-4 performance. ^b07

Our extensive analyses highlight three major challenges of building LLMs to generate text with citations: (1) the retrieval quality is crucial to the final performance and has substantial room for improvement; (2) LLMs' limited context window restricts the number of passages they can incorporate; (3) current LLMs struggle to synthesize multiple documents in context without being distracted by irrelevant ones, although better instruction tuning brings significant improvement. These challenges pose promising research directions for developing better systems integrating retrieval and LLMs. ^b08


## 2 Task Setup and Datasets

Our task is formalized as follows: Given a query q and a corpus of text passages D, the system is required to return an output S, which consists of n statements s1, ..., sn, and each statement si cites a list of passages Ci = {ci,1, ci,2, . . .}4, where ci,j D. In this work, we segment LLMs' output into statements by sentence boundaries.5 While LLMs may include sentences that do not require a citation, such as "I'm happy to help", we observe that almost all sentences that LLMs output provide valuable information and require citations, similar to findings in Liu et al. (2023). In this work, citations are enclosed by box brackets such as [1][2]. ^b09

We divide the corpus D into 100-word passages following previous works on open-domain question answering (Karpukhin et al., 2020; Petroni et al., 2021; Piktus et al., 2021), in contrast to commercial systems like Bing Chat, which cite entire Web pages. We take 100-word passages because it is easier for humans to verify, and allows for more retrieved passages to fit in LLMs' limited context. ^b10

We choose QA datasets so that (1) they contain factual questions, in which references are important; (2) questions require long-text answers that cover multiple aspects; (3) answering the questions requires synthesizing multiple sources. We select three datasets (Table 1) and introduce them below. See B for additional statistics. ^b11

ASQA (Stelmakh et al., 2022) is a long-form factoid dataset. As shown in Figure 1, each question is an ambiguous question from AmbigQA (Min et al., 2020) that requires multiple short answers to cover different aspects, and the dataset provides a longform answer that covers all short answers. Since most questions can be answered by Wikipedia, we use the 2018-12-20 Wikipedia snapshot as D. ^b12

QAMPARI (Rubin et al., 2022) is a factoid QA dataset constructed from Wikipedia, where the answer is a list of entities that are drawn from different passages. Same as ASQA, we use the 2018-1220 Wikipedia as the corpus. ^b13

ELI5 (Fan et al., 2019) is a long-form QA dataset built on the Reddit forum "Explain Like I'm Five".6 Most ELI5 questions are how/why/what questions that require long answers and multiple passages as evidence. Due to the diverse topics discussed in the questions, we use Sphere (Piktus et al., 2021)—a filtered version of Common Crawl7—as the corpus. The ELI5 dataset is widely used in related work due to its challenging nature (Nakano et al., 2021; Menick et al., 2022; Liu et al., 2023). ^b14

We randomly select 1,000 examples from the development set of each dataset for ALCE. Our benchmark primarily assesses the citation capabilities of existing LLMs and does not provide training data, as there are no available examples that provide supervision for citations in these datasets. ^b15


## 3 Automatic Evaluation

Our benchmark measures the following three dimensions of system responses: ^b16

Fluency: whether the model's generated text is fluent and coherent. ^b17

Correctness: whether the answer is accurate and covers all aspects of interest. ^b18

Citation quality: whether the answer is well supported by the cited passages and no irrelevant passages are cited. ^b19

In the following, we present automatic metrics for each dimension and discuss why the combination of the three metrics provides a robust evaluation. ^b20


### 3.1 Fluency

We use MAUVE (Pillutla et al., 2021) to evaluate the fluency of the output (C). We deploy MAUVE for ASQA and ELI5 and omit it for QAMPARI, as QAMPARI only requires a list of short answers as the response and LLMs consistently adhere to the format in our experiments. As MAUVE is sensitive to output length and text style, and most LLMs are capable of producing fluent text, we mainly employ it as a sanity check as long as the MAUVE scores are high enough. ^b21


### 3.2 Correctness

Our objective is to measure the informativeness and utility of the generation to the question. Liu et al. (2023) propose to directly evaluate perceived utility by humans, a process difficult to automate. Therefore, we use correctness—whether the response is accurate compared to a ground truth answer—as a proxy. Evaluating the correctness of long-form generation is a challenging task (Krishna et al., 2021), and we describe our strategy for each dataset below. Figure 2 illustrates the metrics and we include additional implementation details in C. ^b22

For ASQA, we follow Stelmakh et al. (2022) and calculate the recall of correct short answers by checking whether the short answers (provided by the dataset) are exact substrings of the generation (exact match recall; EM recall). ^b23

For QAMPARI, we follow Rubin et al. (2022) and calculate the precision and recall of the model prediction, by checking the exact match to the gold answer list. We add one additional adjustment: considering that users often want to know only a few example answers of the question, our evaluation considers recall to be 100% if the prediction includes at least 5 correct answers (recall-5). ^b24

Unlike ASQA and QAMPARI, the ELI5 dataset does not provide short entity answers. Fan et al. (2019) use ROUGE for evaluation, which does not reflect the correctness well (Krishna et al., 2021; A). Inspired by works in summarization evaluation (Zhang and Bansal, 2021; Kamoi et al., 2023; Wang et al., 2020), we use InstructGPT (text-davinci-003; Ouyang et al., 2022) to generate three "sub-claims". Then we use TRUE8 (Honovich et al., 2022), a T5-11B (Raffel et al., 2020) model fine-tuned on a collection of natural language inference (NLI) datasets, to check whether the model output entails the sub-claims (claim recall). TRUE targets factual correctness and has been used by previous works in similar context (Bohnet et al., 2022; Gao et al., 2023). We demonstrate that claim recall provides a more accurate measure of correctness than existing metrics (more details in A). ^b25


### 3.3 Citation Quality

We evaluate citation qualities using two metrics: (1) citation recall, which determines if the output is entirely supported by cited passages, and (2) citation precision, which identifies any irrelevant citations. Although we prioritize citation recall as it entails a well-supported and truthful answer, enhancing precision is crucial for better user satisfaction, reducing the need for human review of extraneous passages. Figure 3 provides an illustrated example. ^b26

We use the NLI model TRUE (Honovich et al., 2022) again to automatically examine whether the cited passages entail the model generation. We conduct human evaluation (6) to demonstrate strong human correlation of our metric. ^b27

Citation recall. We calculate the citation recall of each statement (0 or 1) and average over all statements in the model response. For each statement si, its citation recall is 1 if and only if there is at least one citation (Ci = ) and (concat(Ci), si) = 1, where (premise, hypothesis) is the NLI model that outputs 1 if the premise entails the hypothesis, and 0 otherwise; concat(Ci) concatenates all passages in Ci together (details in C). The NLI evaluation is in accordance with the attributable to identified sources (AIS) framework (Rashkin et al., 2023): (concat(Ci), si) = 1 implies that si is true based solely on concat(Ci). ^b28

Citation precision. Our citation precision evaluation detects citations that are irrelevant, but it does not require citing a minimal set. We follow this design because human writing often cites redundant sources to enhance credibility; human readers may also appreciate multiple citations, especially when it pertains to critical claims such as medical advice. ^b29

We calculate the citation precision for each citation (0 or 1) and average over all citations in the response. We first define if a citation is "irrelevant". Intuitively, a citation ci,j is "irrelevant" if (a) ci,j itself cannot support si and (b) removing ci,j does not affect the rest of the citations to support si. Formally, ci,j is "irrelevant" if and only if (a) (ci,j, si) = 0, AND (b) (concat(Ci \ {ci,j}), si) = 1. ^b30

ci,j has a precision of 1 if si has recall=1 and ci,j is not irrelevant. For example (Figure 3), when s3 cites three references [2][4][5] and recall=1, [2] is "irrelevant" if ([2], s3) = 0 and ([4][5], s3) = 1. For condition (b) to work, we set recall=1 as a prerequisite for precision= 1. Note that this algorithm overlooks the scenario when one citation partially supports the statement. We discuss the details in E. ^b31


### 3.4 ALCE is Robust to Shortcut Cases

We showcase how the ALCE evaluation is robust to two possible shortcuts in D: (1) using the top-1 retrieved passage as the response and citing itself, and (2) using the first two sentences of the top-1 passage. Both cases have almost-perfect citation scores, but (1) has low fluency due to its unnaturally long length compared to human answers, and (2) has low correctness due to low coverage. ^b32


## 5 Experiments — 5.1 Main Results

We present the main results on three datasets in Table 4, 5, and 6 respectively (full results in G.6). We first note that all models achieve good fluency scores (except some models on ELI5 mainly due to their longer generations). We summarize the main takeaways from the experiments below. ^b33

VANILLA achieves strong performance. Despite its simplicity, VANILLA (putting retrieved passages in context) achieves close-to-the-best performance among all prompting strategies. ^b34

Using summaries or snippets improves correctness. We see a universal trend that SUMM or SNIPPET improves correctness, though on ASQA and ELI5, such an improvement comes at a cost of citation quality due to the lossy compression. Combining INTERACT with SUMM/SNIPPET does not bring improvement, and we hypothesize that checking the full passages offers limited benefit and current LLMs are not proficient in an interactive usage. ^b35

Retrieving text on the fly does not improve performance. All datasets show that VANILLA outperforms INLINESEARCH on citation quality (and ^b36


## 6 Human Evaluation

To verify that our automatic evaluation correlates with human judgement, we conduct human evaluation on selected models and request workers to judge model generations on three dimensions similar to Liu et al. (2023)—(1) utility: a 1-to-5 score indicating whether the generation helps answer the question; (2) citation recall: the annotator is given a sentence and all passages that the sentence cited, and is asked to judge whether the passages fully support the sentence; (3) citation precision: given a sentence and one of its citations, the annotator is asked to judge whether the citation "fully supports", "partially supports", or "does not support" the sentence. Each citation gets a precision score 1 if the output sentence has a citation recall of 1 and this citation at least "partially supports" it. See Appendix F for more details. ^b37

Model outputs score high utility. The utility scores do not differ significantly between models, ranging 3.7-3.9 for ASQA and 3.5-3.6 for ELI5. Upon inspection, all tested models are mostly able to output fluent answers that are related to the question, despite differences in factual correctness. ^b38

Our automatic evaluation of citation quality strongly correlates with human judgements. As shown in Table 8 (ASQA) and Table 9 (ELI5), the relative rankings induced by human and our automatic metrics are consistent. The absolute citation scores from human and ALCE are very close except for RERANK (which uses the automated citation recall for reranking). This suggests that an improvement on ALCE citation metrics translates to improvement on human preferences. Furthermore, the Cohen's kappa coefficient between human and ALCE suggests substantial agreement for citation recall (0.698) and moderate agreement for citation precision (0.525). We also show in G.5 that our automatic evaluation achieves high accuracy when treating human annotations as gold labels (85.1% for citation recall and 77.6% for citation precision). ^b39


## 8 Conclusion

We propose ALCE, the first automatic benchmark for evaluating LLM generations with citations. We deploy automatic metrics to measure fluency, correctness, and citation quality, and verify their efficacy via human evaluation. We explore a variety of strategies for incorporating citations in LLMs and demonstrate that current systems have considerable room for improvement on ALCE. ^b40

Our experiments highlight a number of promising research directions, including (1) enhancing retrieval and refining retrieval integrations in LLMs, (2) developing long-context LLMs, and (3) advancing LLMs' ability to synthesize multiple sources. What's even more intriguing is that these research proposals extend beyond the ALCE setup (for example, long-context LLMs have numerous exciting applications), and ALCE can serve as a valuable testbed for their development. ^b41
