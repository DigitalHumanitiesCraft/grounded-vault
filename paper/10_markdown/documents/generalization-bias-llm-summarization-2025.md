---
type: representation
source-type: document
source: "[[00_sources/peters-chinyee-2025.html]]"
converter: "MarkItDown for the first survey, then a section-selecting BeautifulSoup and markdownify pass over the publisher HTML"
channel: collection
scope: "Abstract, introduction, the full results section including tables 1 to 5, and the methods section of the published article. Discussion, recommendations, strengths and limitations, conclusion, references and supplementary material are not part of this representation. Figures are not carried over; the figures they display are stated in the prose and tables."
metadata:
  title: "Generalization bias in large language model summarization of scientific research"
  creator: "research team, Utrecht University and Western University"
  date: "2025-04-30"
  format: "html"
  identifier: "https://doi.org/10.1098/rsos.241776"
  license: "CC-BY-4.0"
  confidential: false
created: 2026-08-10
updated: 2026-08-10
---

# Generalization bias in large language model summarization of scientific research

## Abstract

Artificial intelligence chatbots driven by large language models (LLMs) have the potential to increase public science literacy and support scientific research, as they can quickly summarize complex scientific information in accessible terms. However, when summarizing scientific texts, LLMs may omit details that limit the scope of research conclusions, leading to generalizations of results broader than warranted by the original study. We tested 10 prominent LLMs, including ChatGPT-4o, ChatGPT-4.5, DeepSeek, LLaMA 3.3 70B, and Claude 3.7 Sonnet, comparing 4900 LLM-generated summaries to their original scientific texts. Even when explicitly prompted for accuracy, most LLMs produced broader generalizations of scientific results than those in the original texts, with DeepSeek, ChatGPT-4o, and LLaMA 3.3 70B overgeneralizing in 26–73% of cases. In a direct comparison of LLM-generated and human-authored science summaries, LLM summaries were nearly five times more likely to contain broad generalizations (odds ratio = 4.85, 95% CI [3.06, 7.70], *p* < 0.001). Notably, newer models tended to perform worse in generalization accuracy than earlier ones. Our results indicate a strong bias in many widely used LLMs towards overgeneralizing scientific conclusions, posing a significant risk of large-scale misinterpretations of research findings. We highlight potential mitigation strategies, including lowering LLM temperature settings and benchmarking LLMs for generalization accuracy. ^pc01

**Keywords:** large language models, algorithmic bias, science communication, overgeneralization ^pc02

## 1. Introduction

Accurately communicating findings of scientific studies is vital for educating the public, informing policy, guiding behaviour, and advancing research [1,2]. To learn about, review, and communicate scientific findings, both experts (e.g. researchers) and laypeople (e.g. reporters and students) now increasingly use artificial intelligence (AI) chatbots (e.g. ChatGPT) powered by large language models (LLMs) [3–5]. AI chatbots can process vast amounts of scientific information and summarize content in easily understandable language, thus helping to spread scientific knowledge, promote evidence uptake, and facilitate research [3,6,7]. ^pc03

However, many experts have voiced concerns, noting that AI chatbots used as science communication tools may generate plausible sounding but false or misleading information [3,8–10]. One important related yet underexplored issue is that chatbots may overlook uncertainties, limitations, and nuances in original research by omitting qualifiers and oversimplifying text [11,12], leading to *overgeneralizations*, i.e. generalizations that are broader than those in the original text and that may therefore be unwarranted by the original findings. This can result in widespread misinterpretations of findings, illusions of understanding, research lacunas, and risky practices [13]. For instance, LLM chatbots are increasingly used in medical education and clinical practice for research summarization and answering medical queries [10,14,15]. If chatbots produce summaries that overlook qualifiers or restrictors to the generalizability of clinical trial results, trainees and practitioners who rely on these chatbots may prescribe unsafe or inappropriate treatments. ^pc04

Several recent studies found that scientists and science reporters also frequently overgeneralized or exaggerated scientific findings in their writings [16–18]. This problem could be exacerbated or mitigated if LLMs, instead of human communicators, convey scientific results. However, the specific question of whether LLMs accurately capture the generalizations of scientific research remains unexamined, leaving a critical knowledge gap regarding the societal risks of using LLMs for science summarization that has led several commentators to call for a systematic investigation [11]. ^pc05

To address this gap, we tested 10 prominent LLMs on their ability to summarize abstracts and articles from top journals in science (e.g. *Science*, *Nature*) and medicine (e.g. *The New England Journal of Medicine*, *Lancet*) (see Methods). The models, tested through an application programming interface (API) or website user interface (UI), were GPT-3.5 Turbo (API and UI), GPT-4 Turbo (API and UI), LLaMA 2 70B (API), Claude 2 (API), ChatGPT-4o (UI), ChatGPT-4.5 (UI), LLaMA 3.3 70B Versatile (API), Claude 3.5 Sonnet (UI), Claude 3.7 Sonnet (UI), and DeepSeek (UI). By ‘GPT-3.5 Turbo (UI)’ and ‘GPT-4 Turbo (UI)’, we mean ChatGPT-3.5 and ChatGPT-4, respectively, as these systems were powered by GPT-3.5 Turbo and GPT-4 Turbo at the time of the first data collection. ^pc06

The first four models were selected because they were among the most widely used LLMs at the time of study inception (January 2024), and prior research found that LLaMA 2 and GPT models outperformed humans in medical text summarization [19], while Claude models demonstrated greater faithfulness in book summaries than GPT [20]. To assess diachronic trends in LLM generalization behaviour, the four older models were compared to the six newer ones (tested in March 2025), which currently rank among the most widely used and preferred by scientists [21]. ^pc07

Our primary focus was on GPT models, as they remain dominant LLMs [22], with ChatGPT usage among US teenagers for schoolwork doubling from 13% in 2023 to 26% in 2025 [23]. Additionally, GPT models have been found to produce a lower percentage of misrepresentations (15%) in news summarization compared to competitors such as Perplexity (17%), Copilot (27%), and Gemini (34%), further justifying our emphasis on them [24]. DeepSeek was included due to its rapid rise in popularity, having recently overtaken ChatGPT as the most downloaded free chatbot app [25]. ^pc08

For the scientific texts to be summarized, abstracts (100 from multidisciplinary science journals and 100 from medical journals) were our primary focus as they provide an efficient format for testing summarization by LLMs [9]. Additionally, we tested several models on their summarization of 100 full-length articles, focusing on articles reporting clinical studies because overly broad generalizations of clinical findings can be particularly problematic, often directly affecting policy-making or patient care [18,26]. To systematically assess differences between LLM-generated and human-written summaries, we also collected the corresponding expert-written summaries from *NEJM Journal Watch* (henceforth ‘*NEJM JW*’) [27]. ^pc09

In our analysis, we compared the generalizations within the result claims of LLM summaries with the generalizations in the original texts. Furthermore, LLM article summaries were compared with *NEJM JW* summaries of the same articles. Original texts and summaries were coded based on whether their result claims contained one or more of the following three types of generalizations: ^pc10

1. *Generic generalizations (generics*). These are present tense generalizations that do not have a quantifier (e.g. ‘many’, ‘75%’) in the subject noun phrase and describe study results as if they apply to whole categories of people, things, or abstract concepts (e.g. ‘parental warmth is protective’) instead of specific or quantified sets of individuals (e.g. study participants) [28]. Generics are known to obscure differences between individuals of a reference class since they are semantically underdetermined (e.g. the generic ‘children like sweets’ may refer to some, most, or all children) [18,26]. Hence, when an LLM summarizes a quantified generalization by using a generic, it transitions from a narrower to a potentially unwarranted broader generalization. ^pc11

2. *Present tense generalizations*. Result claims in past tense have a more limited generalization scope than present tense result claims because they refer to a particular sample and do not extend findings to the here and now [18]. When past tense result claims from an original text are turned into present tense in the summary, a broader generalization is conveyed than the author(s) of the original text may have intended [29]. ^pc12

3. *Action guiding generalizations*. While result claims commonly manifest in descriptive statements (e.g. ‘OCD patients benefit from CBT’), they often underlie recommendations (e.g. for policy-makers, practitioners, etc.) about a particular policy or action (e.g. ‘CBT should be recommended for OCD patients’) [30]. When descriptive result claims are summarized such that action guiding recommendations are communicated, this involves a broader generalization than that found in the summarized text because researchers may have deliberately avoided such recommendations due to insufficient evidence to support them. ^pc13

We tested whether the outputs of the 10 LLMs mentioned above retained the quantified, past tense, or descriptive generalizations of the scientific texts that they summarized, or transitioned to unquantified (generic), present tense, or action guiding generalizations. We defined the latter kind of conclusions collectively as *generalized* and the former as *restricted conclusions*. ^pc14

Using logistic regressions to model the scope of a text’s conclusion (generalized versus restricted) as the binary outcome variable, we examined whether LLM summaries of original texts differed from the original texts in the likelihood of containing generalized conclusions. Moreover, we compared the number of original texts containing generalized conclusions with the number of corresponding LLM summaries containing them. When the latter number was higher than the former, this difference indicated the overall cases in which LLMs deviated in their summaries from original texts by producing broader conclusions than the original texts contained. We defined such a case as an *overall algorithmic overgeneralization*. When a specific original scientific text did not contain a generalized conclusion, but the corresponding LLM summary contained one, this was defined as a *specific algorithmic overgeneralization*. ^pc15

Not all generic, present tense, or action guiding generalizations—whether made by scientists or LLMs—are problematic. When evidentially warranted, these generalizations (by humans) are an essential part of inductive scientific knowledge acquisition [31] and sometimes necessary for effective science communication, as, for instance, members of the public are interested in what the results mean *for them now* (versus only the sample tested). Similarly, while generic statements carry semantic risks due to their underdetermined meaning [18], they can also be effective in simplifying complex information, making scientific content more accessible. ^pc16

However, when generalizations lack sufficient empirical support, for instance, when researchers fail to control for confounders or use unrepresentative samples, they become problematic. In this study, we did not assess whether the generalizations in human-authored texts were warranted. Rather, we used them as a baseline for comparison. The faithful representation of the original text served as the normative standard, and we defined ‘overgeneralizations’ as cases where LLMs broadened conclusions beyond those presented in the original scientific text. To the extent that an LLM user asks specifically only for a summary of a given text, any deviation in generalization from the original remains an epistemically problematic LLM output. ^pc17

Prior research found that the content of LLM prompts can significantly affect output accuracy [32,33]. Whether this also applies to the accuracy of LLM generalizations in science text summarization has not yet been studied. We therefore also tested three different prompts. The first one simply asked LLMs to summarize a given text without further instruction. The second was selected based on evidence from a previous study, which found that a prompt with the phrase ‘take a deep breath and work on this problem step by step’ produced LLM outputs with the highest accuracy compared to prompts with more neutral language [32]. While caution is warranted about anthropomorphizing LLMs [34], we included a summary prompt with this phrase to test whether it would also facilitate generalization accuracy. The third prompt explicitly asked LLMs to avoid inaccuracies in the summaries. ^pc18

Since LLM responses can be influenced by temperature, a parameter that controls the randomness of generated text (higher temperatures produce more varied and less constrained outputs), we accessed some models via an API, as this allows explicit temperature control. To maximize replicability and consistency, we retrieved 400 LLM-generated abstract summaries using a temperature setting of 0, the most deterministic setting [35]. However, ChatGPT, the UI for GPT models, is widely assumed to default to a temperature of 0.7, though OpenAI has not disclosed exact details [36,37]. Similarly, the DeepSeek AI Assistant UI does not disclose its default temperature setting (though its API documentation lists 1.0 as the default) [38]. To capture LLM responses as experienced by lay users who do not know how to code (and thus may rely only on the UI), we collected most LLM abstract and article summaries at a temperature of 0.7 or via UIs. ^pc19

Finally, to assess whether LLM responses remain stable upon retesting, several models were tested multiple times with the same inputs. The details of all conditions (i.e. prompts, temperatures, and retests) and LLM summary retrievals are presented in figure 1, showing that a total of 4900 LLM summaries—4300 abstract summaries and 600 article summaries—were tested. This total was pre-specified to keep data labelling tractable. For the testing, our three main research questions were: ^pc20

1. Do algorithmic overgeneralizations occur? ^pc21
2. If so, can LLM prompts that focus on systematic (‘step-by-step’) or accurate processing mitigate them? ^pc22
3. Do LLMs differ from human science communicators (specifically, *NEJM JW* authors) in their tendency to overgeneralize? ^pc23

## 2. Results

### 2.1. Do algorithmic overgeneralizations occur?

We first compared scientific abstracts and LLM summaries in terms of their likelihood of containing generalized conclusions, combining all original abstracts and their 4300 LLM-generated summaries. A regression analysis was conducted with scope of conclusion (generalized versus restricted) as the dependent variable and text source (original abstract versus LLM (all models combined)) as the main predictor, while controlling for temperature, prompt, and test condition (i.e. first test, second test, etc.). The model was significant overall (*F*7,4492 = 32.34, *p* < 0.001), showing that LLM summaries (all combined) were twice as likely to contain generalized conclusions compared to the original abstracts, indicating an algorithmic overgeneralization tendency (table 1, figure 2). ^pc24

#### Table 1.

Fixed effects of generalized linear mixed models (GLMMs) predicting the likelihood of generalized (versus restricted) conclusions in LLM-generated summaries of abstracts and articles. Models comparing abstracts versus LLM-generated summaries control for temperature, test condition, and prompt type. *B* coefficients represent unstandardized estimates of each predictor’s effect on the likelihood of generalized conclusions, holding other factors constant. ^pc25

| GLMM regression table | | | | |
| --- | --- | --- | --- | --- |
| **Type of comparison** | **B** | **SE** | ***t*** | ***p*** |
| **Overall source comparison** |  |  |  |  |
| *All scientific abstracts as reference* |  |  |  |  |
| All LLM summaries combined versus original abstracts | 0.693 | 0.1926 | 3.597 | <0.001 |
| **Subtype source comparisons** |  |  |  |  |
| GPT-3.5 Turbo (API and UI) versus original abstracts | 0.516 | 0.2719 | 1.896 | 0.058 |
| GTP-4 Turbo (API and UI) versus original abstracts | 0.949 | 0.2520 | 3.765 | <0.001 |
| ChatGPT-4o (UI) versus original abstracts | 2.200 | 0.4415 | 4.983 | <0.001 |
| ChatGPT-4.5 (UI) versus original abstracts | 0.883 | 0.4438 | 1.989 | 0.047 |
| LLaMA 2 70B (API) versus original abstracts | 0.964 | 0.2744 | 3.515 | <0.001 |
| LLaMA 3.3 70B (API) versus original abstracts | 3.672 | 0.3936 | 9.330 | <0.001 |
| Claude 2 (API) versus original abstracts | −0.110 | 0.2707 | −0.406 | 0.685 |
| Claude 3.5 Sonnet (UI) versus original abstracts | 0.248 | 0.4562 | 0.543 | 0.587 |
| Claude 3.7 Sonnet (UI) versus original abstracts | 0.824 | 0.4447 | 1.853 | 0.064 |
| DeepSeek (UI) versus original abstracts | 1.168 | 0.4407 | 2.651 | 0.008 |
| **Temperature comparisons** |  |  |  |  |
| *Temp 0.7 as reference* |  |  |  |  |
| Temp 0.0 versus temp 0.7 | −1.432 | 0.3726 | −3.843 | <0.001 |
| UI temp versus temp 0.7 | −0.262 | 0.3219 | −0.813 | 0.416 |
| **Retesting** |  |  |  |  |
| *Test 1 as reference* |  |  |  |  |
| Test 2 versus test 1 | −0.199 | 0.3642 | −0.546 | 0.585 |
| Test 3 versus test 1 | 0.426 | 0.3497 | 1.217 | 0.224 |
| **Prompt comparisons** |  |  |  |  |
| *Simple prompt as reference* |  |  |  |  |
| Systematic versus simple prompt | −0.148 | 0.2720 | −0.544 | 0.587 |
| Accuracy versus simple prompt | 0.640 | 0.2753 | 2.323 | 0.020 |
| **Human versus LLM article summaries** |  |  |  |  |
| *100 scientific (medical) articles as reference* |  |  |  |  |
| *NEJM JW* summaries versus scientific articles | 0.297 | 0.2917 | 1.018 | 0.309 |
| LLMs versus scientific articles | 1.905 | 0.2374 | 8.025 | <0.001 |
| GPT-4 Turbo (API) (temp 0.7) versus scientific articles | 1.045 | 0.3081 | 3.392 | <0.001 |
| ChatGPT-4 (UI) test 1 versus scientific articles | 1.565 | 0.3306 | 4.735 | <0.001 |
| ChatGPT-4 (UI) test 2 versus scientific articles | 1.501 | 0.3271 | 4.587 | <0.001 |
| ChatGPT-4 (UI) test 3 versus scientific articles | 2.199 | 0.3768 | 5.834 | <0.001 |
| ChatGPT-4o (UI) versus. scientific articles | 3.176 | 0.5084 | 6.246 | <0.001 |
| DeepSeek (UI) versus scientific articles | 3.715 | 0.6259 | 5.934 | <0.001 |
| *NEJM JW summaries as reference* |  |  |  |  |
| LLMs versus *NEJM JW* summaries | 1.579 | 0.2353 | 6.713 | <0.001 |
| GPT-4 Turbo (API) (temp 0.7) versus *NEJM JW* summaries | 0.728 | 0.3054 | 2.385 | 0.017 |
| ChatGPT-4 (UI) test 1 versus *NEJM JW* summaries | 1.240 | 0.3278 | 3.781 | <0.001 |
| ChatGPT-4 (UI) test 2 versus *NEJM JW* summaries | 1.176 | 0.3244 | 3.625 | <0.001 |
| ChatGPT-4 (UI) test 3 versus *NEJM JW* summaries | 1.865 | 0.3742 | 4.984 | <0.001 |
| ChatGPT-4o (UI) versus *NEJM JW* summaries | 2.835 | 0.5062 | 5.600 | <0.001 |
| DeepSeek (UI) versus *NEJM JW* summaries | 3.371 | 0.6241 | 5.402 | <0.001 |

Open in a new tab

A subsequent analysis using subtype of text source (original abstract versus each individual LLM) as the main predictor and controlling for temperature, prompt, test condition, and interactions between LLMs and these three factors showed significant effects of subtype of text source (*F*9,4467 = 39.58, *p* < 0.001), temperature (*F*2,4467 = 4.21, *p* = 0.015), and prompt (*F*2,4467 = 17.10, *p* < 0.001). But there was no evidence that test condition significantly affected LLM generalizations (*F*2,4467 = 0.56, *p* = 0.57), suggesting that for the relevant models, the overall results were stable upon retesting. ^pc26

Focusing on specific models, the summaries by 6 of the 10 models, i.e. GPT-4 Turbo (API and UI), ChatGPT-4o (UI), ChatGPT-4.5 (UI), LLaMA 2 70B (API), LLaMA 3.3 70B (API), and DeepSeek (UI), were significantly more likely to contain generalized conclusions compared to the original texts (table 1, figure 2). From the older models, GPT-4 Turbo (API and UI) and LLaMA 2 70B (API) abstract summaries were about 2.6 times more likely to contain such conclusions compared to the abstracts (figure 2). This tendency increased to 9 (ChatGPT-4o (UI)) and 39 times (LLaMA 3.3 70B (API)) in more recent models. We return to this pronounced difference between older and newer models below. Notably, the summaries by GPT-3.5 Turbo (API and UI) and both the older and most recent versions of Claude (i.e. 2, 3.5 and 3.7) did not significantly differ in generalizations from the abstracts. ^pc27

Moreover, at LLM temperature 0, summaries containing generalized conclusions were 76% less likely to occur compared to those generated at temperature 0.7 (figure 2). No significant difference was observed between the (unknown) temperature setting of the LLM UIs and temperature 0.7. ^pc28

Corresponding to the differences in likelihood of producing outputs with generalized conclusions, the number of overall algorithmic overgeneralizations (i.e. the total number of LLM summaries with generalized conclusions higher than the original texts with them) also differed between models (table 2). Newer models such as ChatGPT-4o (UI) (45−60%), LLaMA 3.3 70B (API) (69−73%), and DeepSeek (UI) (26−67%) were associated with the highest proportion of these overgeneralizations, compared to older ones. Claude models had the lowest (−1 to 20%). ^pc29

#### Table 2.

Counts of texts containing generalized conclusions and overall algorithmic overgeneralizations (OAO). ^pc30

| Text source | Texts with generalized conclusions | OAO |
| --- | --- | --- |
| ***All 200 scientific abstracts*** | 108 (54%) |  |
| **GPT-3.5 Turbo (API) (temp 0.7)** |  |  |
| Simple prompt | 122 (61%) | 14 (7%) |
| Systematic prompt | 118 (59%) | 10 (5%) |
| Accuracy prompt | 139 (69.5%) | 31 (15.5%) |
| **GPT-4 Turbo (API) (temp 0.7)** |  |  |
| Simple prompt | 141 (70.5%) | 33 (16.5%) |
| Systematic prompt | 133 (66.5%) | 25 (12.5%) |
| Accuracy prompt | 151 (75.5%) | 43 (21.5%) |
| **LLaMA 2 70B (API) (temp 0.7)** |  |  |
| Simple prompt | 134 (67%) | 26 (13%) |
| **Claude 2 (API) (temp 0.7)** |  |  |
| Simple prompt | 105 (52.5%) | 0 |
| ***100 scientific (medical) abstracts*** | 20 (20%) |  |
| **GPT-3.5 Turbo (API) (temp 0.7)** |  |  |
| Simple prompt | 34 (34%) | 14 (14%) |
| Systematic prompt | 37 (37%) | 17 (17%) |
| Accuracy prompt | 46 (46%) | 26 (26%) |
| **GPT-4 Turbo (API) (temp 0.7)** |  |  |
| Simple prompt | 50 (50%) | 30 (30%) |
| Systematic prompt | 50 (50%) | 30 (30%) |
| Accuracy prompt | 56 (56%) | 36 (36%) |
| **ChatGPT-4o (UI)** |  |  |
| Simple prompt | 65 (65%) | 45 (45%) |
| Systematic prompt | 75 (75%) | 55 (55%) |
| Accuracy prompt | 80 (80%) | 60 (60%) |
| **ChatGPT-4.5 (UI)** |  |  |
| Simple prompt | 41 (41%) | 21 (21%) |
| **LLaMA 2 70B (API) (temp 0.7)** |  |  |
| Simple prompt | 51 (51%) | 31 (31%) |
| **LLaMA 3.3 70B (API) (temp 0.7)** |  |  |
| Simple prompt | 89 (89%) | 69 (69%) |
| Systematic prompt | 76 (76%) | 56 (56%) |
| Accuracy prompt | 93 (93%) | 73 (73%) |
| **Claude 2 (API) (temp 0.7)** |  |  |
| Simple prompt | 19 (19%) | −1 (−1%) |
| **Claude 3.5 Sonnet (UI)** |  |  |
| Simple prompt | 31 (31%) | 11 (11%) |
| Systematic prompt | 39 (39%) | 19 (19%) |
| Accuracy prompt | 24 (24%) | 4 (4%) |
| **Claude 3.7 Sonnet (UI)** |  |  |
| Simple prompt | 40 (40%) | 20 (20%) |
| **DeepSeek (UI)** |  |  |
| Simple prompt | 46 (46%) | 26 (26%) |
| Systematic prompt | 68 (68%) | 48 (48%) |
| Accuracy prompt | 87 (87%) | 67 (67%) |

Open in a new tab

Turning to specific algorithmic overgeneralizations (i.e. instances where a specific LLM summary introduced a generic, present tense, or action guiding generalization absent in the original text), table 3 presents concrete examples. Compared to older models (table 4), ChatGPT-4o (UI) and LLaMA 3.3 70B (API) had the highest proportion of specific algorithmic overgeneralizations (reaching 61 and 73%, respectively) (table 5). Claude had consistently the lowest. Notably, across LLMs and prompts, among the tested models, the most frequent transitions from a narrow generalization in the original text to a broader generalization in the LLM summary were transitions from quantified generalizations to generics (table 4). ^pc31

#### Table 3.

Randomly selected examples of transitions from narrower claims in abstracts to generalized conclusions in LLM summaries (simple prompt responses). Numbers in parentheses indicate OSF IDs (i.e. identifiers of the text in the datasheets available on our OSF platform). Phrases marking generalization transitions are highlighted in bold. ^pc32

| Examples of specific algorithmic overgeneralizations |
| --- |
| *Non-generic to generic generalizations* |
| Original (153): ‘While exposure to disinformation **had strong detrimental effects on participants’ climate change beliefs** (*δ* = −0.16), affect towards climate mitigation action (*δ* = −0.33), ability to detect disinformation (*δ* = −0.14) and pro-environmental behaviour (*δ* = −0.24), we found almost no evidence for protective effects of the inoculations (all *δ* < 0.20)’ |
| ChatGPT-4 (UI): ‘The main findings from the experiments indicate that exposure to climate disinformation **significantly undermines individuals’ beliefs in climate change**, their positive feelings towards climate mitigation, their ability to recognize disinformation and their engagement in pro-environmental behaviours’ |
| Original (13): ‘Among adults with obesity, **bariatric surgery** compared with no surgery **was associated** with a significantly lower incidence of obesity-associated cancer and cancer-related mortality’ |
| DeepSeek (UI) ‘The study concluded that **bariatric surgery is associated** with a significantly lower incidence of obesity-associated cancers and cancer-related mortality compared to nonsurgical care in adults with obesity’ |
| Original (26): ‘Among patients undergoing hip or knee arthroplasty for osteoarthritis, **aspirin compared with enoxaparin resulted in a significantly higher rate of symptomatic VTE within 90 days**, defined as below- or above-knee DVT or pulmonary embolism’ |
| LLaMA 3.3 70B (API): ‘Overall, the study suggests that **enoxaparin is more effective than aspirin in preventing symptomatic VTE after THA or TKA**’ |
| *Past to present tense generalizations* |
| Original (7): ‘Among women with a history of gestational diabetes mellitus, each additional optimal modifiable factor **was associated with an incrementally lower risk of type 2 diabetes**’ |
| ChatGPT-4o (UI): ‘For women with a history of gestational diabetes, every additional healthy lifestyle choice **significantly lowers the risk of type 2 diabetes**, regardless of weight status or genetic predisposition’ |
| Original (77): ‘The consumption of caffeinated coffee **did not result in significantly more** daily premature atrial contractions than the avoidance of caffeine’ |
| ChatGPT-3.5 (UI): ‘The results suggest that the consumption of caffeinated coffee **does not significantly increase** the occurrence of premature atrial contractions’ |
| Original (20): ‘Genital HSV-1 shedding **was frequent** after first-episode genital HSV-1, particularly among those with primary infection, and declined rapidly during the first year after infection’ |
| Claude 3.5 Sonnet (UI): ‘The key takeaway is that genital HSV-1 shedding **is common** initially after first-episode infection, particularly in those with primary infection, but declines significantly during the first year, despite maintained immune responses’ |
| *Descriptive to action guiding generalizations* |
| Original (41): ‘Our results are relevant to clinical practice, **supporting the use of the Mediterranean diet** in secondary prevention’ |
| Claude 3.5 Sonnet (UI): ‘The findings suggest that the **Mediterranean diet should be considered** as a preferred dietary approach for patients with established cardiovascular disease, particularly for men’ |
| Original (158): ‘These findings **have immediate implications for government communicators** and open the door for a renewed focus on how the design and presentation of information impacts behaviour’ |
| Claude 2 (API): ‘The findings suggest **government communicators should consider** using more formal communication designs and presentations, as this can positively impact resident behavior’ |
| Original (35): ‘We found that transcatheter arterialization of the deep veins **was safe and could be performed successfully** in patients with chronic limb-threatening ischaemia and no conventional surgical or endovascular revascularization treatment options’ |
| DeepSeek (UI): ‘The study concluded that TADV **is a safe and effective treatment option** for patients with CLTI who lack conventional revascularization options, offering significant benefits in amputation-free survival and limb salvage’ |

Open in a new tab

#### Table 4.

Overview of specific algorithmic (SA) overgeneralizations and undergeneralizations by generalization types (SA overgeneralization types indicated with \*, SA undergeneralization types indicated with \*\*), focusing on older LLMs. Undergeneralizations are the reverse of overgeneralizations, involving LLM transitions from broader generalizations in the original text to narrower generalizations in the summary. ^pc33

| Generalizations in LLM summaries of 200 scientific abstracts (older models) | | | | |
| --- | --- | --- | --- | --- |
| **Prompt and**  **generalization type** | **GPT-3.5 Turbo**  **(API, 0.7)** | **GPT-4 Turbo**  **(API, 0.7)** | **LLaMA 2 70B**  **(API, 0.7)** | **Claude 2**  **(API, 0.7)** |
| **Simple prompt** |  |  |  |  |
| SA overgeneralizations | 23 (11.5%) | 41 (20.5%) | 43 (21.5%) | 10 (5%) |
| SA undergeneralizations | 9 (4.5%) | 8 (4%) | 17 (8.5%) | 13 (6.5%) |
| *Breakdown by generalization type* |  |  |  |  |
| (1) non-generic to generic\* | 31 (15.5%) | 51 (25.5%) | 53 (26.5% | 13 (6.5%) |
| (1) generic to non-generic\*\* | 13 (6.5%) | 17 (8.5%) | 20 (10%) | 12 (6%) |
| (2) past to present tense\* | 23 (11.5%) | 41 (20.5%) | 43 (21.5%) | 10 (5%) |
| (2) present to past tense\*\* | 9 (4.5%) | 8 (4%) | 17 (8.5%) | 13 (6.5%) |
| (3) descriptive to action guiding\* | 3 (1.5%) | 5 (2.5%) | 5 (2.5%) | 6 (3%) |
| (3) action guiding to descriptive\*\* | 4 (2%) | 7 (3.5%) | 10 (5%) | 9 (4.5%) |
| **Systematic prompt** |  |  |  |  |
| SA overgeneralizations | 23 (11.5%) | 39 (19.5%) |  |  |
| SA undergeneralizations | 13 (6.5%) | 14 (7%) |  |  |
| *Breakdown by generalization type* |  |  |  |  |
| (1) non-generic to generic\* | 31 (15.5%) | 41 (20.5%) |  |  |
| (1) generic to non-generic\*\* | 15 (7.5%) | 11 (5.5%) |  |  |
| (2) past to present tense\* | 23 (11.5%) | 39 (19.5%) |  |  |
| (2) present to past tense\*\* | 13 (6.5%) | 14 (7%) |  |  |
| (3) descriptive to action guiding\* | 3 (1.5%) | 1 (0.5%) |  |  |
| (3) action guiding to descriptive\*\* | 5 (2.5%) | 10 (5%) |  |  |
| **Accuracy prompt** |  |  |  |  |
| SA overgeneralizations | 33 (16.5%) | 47 (23.5%) |  |  |
| SA undergeneralizations | 2 (1%) | 4 (2%) |  |  |
| *Breakdown by generalization type* |  |  |  |  |
| (1) non-generic to generic\* | 31 (15.5%) | 47 (23.5%) |  |  |
| (1) generic to non-generic\*\* | 6 (3%) | 8 (4%) |  |  |
| (2) past to present tense\* | 33 (16.5%) | 47 (23.5%) |  |  |
| (2) present to past tense\*\* | 2 (1%) | 4 (2%) |  |  |
| (3) descriptive to action guiding\* | 7 (3.5%) | 10 (5%) |  |  |
| (3) action guiding to descriptive\*\* | 5 (2.5%) | 8 (4%) |  |  |

Open in a new tab

#### Table 5.

Overview of specific algorithmic (SA) overgeneralizations and undergeneralizations, focusing on recent LLMs. ^pc34

| Generalizations in LLM summaries of 100 scientific abstracts (recent models) | | | | | | |
| --- | --- | --- | --- | --- | --- | --- |
| **Prompt and**  **generalization type** | **ChatGPT-4o**  **(UI)** | **ChatGPT-4.5**  **(UI)** | **LLaMA 3.3**  **70B (API, 0.7)** | **Claude 3.5**  **Sonnet (UI)** | **Claude 3.7**  **Sonnet (UI)** | **DeepSeek**  **(UI)** |
| **Simple prompt** |  |  |  |  |  |  |
| SA overgeneralizations | 48 (48%) | 26 (26%) | 71 (71%) | 14 (14%) | 22 (22%) | 29 (29%) |
| SA undergeneralizations | 3 (3%) | 5 (5%) | 2 (2%) | 3 (3%) | 2 (2%) | 3 (3%) |
| **Systematic prompt** |  |  |  |  |  |  |
| SA overgeneralizations | 58 (58%) |  | 57 (57%) | 26 (26%) |  | 51 (51%) |
| SA undergeneralizations | 3 (3%) |  | 1 (1%) | 7 (7%) |  | 3 (3%) |
| **Accuracy prompt** |  |  |  |  |  |  |
| SA overgeneralizations | 61 (61%) |  | 73 (73%) | 8 (8%) |  | 67 (67%) |
| SA undergeneralizations | 1 (1%) |  | 0 (0%) | 4 (4%) |  | 0 (0%) |

Open in a new tab

### 2.2. Can LLM prompts that focus on systematic or accurate processing mitigate algorithmic overgeneralizations?

Compared to the simple prompt, the systematic prompt did not significantly change the likelihood of LLM outputs containing generalized conclusions. However, the accuracy prompt did change the chances, albeit in an unexpected direction: LLM summaries retrieved with the accuracy prompt were about twice as likely to contain generalized conclusions compared to the simple prompt (OR = 1.90, 95% CI [1.11, 3.26], *p* = 0.02) (figure 2). Correspondingly, for all models (older and newer versions), except Claude, the proportion of both overall and specific algorithmic overgeneralizations was also highest when the accuracy prompt was used (tables 4 and 5). ^pc35

### 2.3. Do LLMs differ from human science communicators in producing overgeneralizations?

Previous studies found that human science communicators also often overgeneralize or exaggerate research results [16–18]. To examine whether LLMs differ from humans in this respect, we additionally tested GPT-4 Turbo (API and UI), ChatGPT-4o (UI), and DeepSeek (UI) on the summarization of 100 full-length scientific (medical) articles that had corresponding human-authored summaries published in *NEJM JW*, enabling direct human–LLM summary comparisons. ^pc36

Compared to the original articles, *NEJM JW* summaries did not significantly differ in their likelihood of containing generalized conclusions (table 1). However, overall, LLM (GPT-4 Turbo (API and UI), ChatGPT-4o (UI), and DeepSeek (UI)) article summaries had more than 6 times higher chances of containing generalized conclusions than the articles themselves (OR = 6.72, 95% CI [4.22, 10.71], *p* < 0.001). Moreover, when the human-authored *NEJM JW* summaries of the same articles were used as the reference, LLM summaries were almost 5 times as likely to contain generalized conclusions compared to *NEJM JW* summaries (OR = 4.85, 95% CI [3.06, 7.70], *p* < 0.001). This likelihood (figure 2), as well as the number of overall and specific algorithmic overgeneralizations (figure 3), substantially increased in newer models such as ChatGPT-4o and DeepSeek. ^pc37

## 7. Methods

This experimental study, which was preregistered on an OSF platform (https://osf.io/25ct6), combined between- and within-subject aspects, testing different and the same LLMs multiple times. The 10 tested LLMs were accessed through either an API or UI (figure 1). In UI data collections, LLM summaries were retrieved in separate chats, either using new accounts or with memory turned off (ChatGPT-4o) to mitigate personalization. ^pc38

*Material*. 200 abstracts of scientific articles were used: 100 from the top four general medical journals (*Lancet*, *NEJM*, *JAMA*, and the *BMJ*) and 100 from the top four multidisciplinary science journals (*Nature*, *Science*, *Nature Human Behavior*, and *Psychological Science in the Public Interest*) as ranked by the 2022/23 Clarivate Journal Citation Reports. The 25 most recent abstracts from each journal were collected by moving backward from December 2023, excluding non-research articles (e.g. opinion pieces and commentaries). For more generalizable results, 100 full-length articles were added to test GPT-4 Turbo (API and UI), ChatGPT-4o (UI), and DeepSeek (UI) article summarization. They were taken from the four medical journals (25 per journal, moving back from May 2023), focusing only on original prospective clinical studies, as they offer key evidence for the efficacy of medical interventions, making their summaries particularly relevant. For these 100 studies, corresponding *NEJM JW* summaries were also collected. ^pc39

LLM summaries were retrieved with four prompts and different model temperatures as shown in figure 1. For retrieving GPT-4 Turbo (API and UI), ChatGPT-4o (UI), and DeepSeek (UI) article summaries, we used a version of the simple prompt designed to ensure comparability with *NEJM JW* summaries, which also always have a title. ^pc40

*Procedure*. After retrieving LLM summaries, two experts in corpus analysis and science communication coded each text as containing either restricted or generalized conclusions using preregistered criteria (see OSF material). A third, independent researcher, blinded to the summary source, applied the same criteria to 100 texts. Inter-rater agreement ranged from *k* = 0.79, 95% CI [0.70, 0.87] to *k* = 0.95, 95% CI [0.91, 0.99]. Disagreements were resolved through discussion. All generalized conclusions identified by the researchers were recorded in spreadsheets available at https://osf.io/q936d/. ^pc41

*Statistical information*. To analyse the distribution of generalized conclusions, we modelled the probability of a text containing them (categorical dependent variable) using generalized linear mixed models (GLMMs) with a binomial distribution and logit link. To avoid multicollinearity problems and tailor analyses to the different text types (abstract and article summaries), six separate models were conducted with Bonferroni corrections (for models (1) and (2), *α* = 0.025; for models (3) to (6), *α* = 0.0125). ^pc42

Model (1) compared the probability of generalized conclusions in LLM summaries versus abstracts, using overall source (abstracts versus all LLM summaries) as the main predictor with temperature (0, 0.7, UI temperature), test condition (tests 1−3) and prompt (simple, systematic, and accuracy) as fixed effects and a unique identifier for each abstract as a random intercept to account for repeated measures. Model (2) used the same variables but divided the LLM source category into individual LLMs to test for differences. Interaction terms (source × temperature, source × test, and source × prompt) were included to determine if the effects of temperature, test, and prompt were different depending on the source type. Model (3) compared 100 articles and their generalized conclusions to the corresponding *NEJM JW*, GPT-4 Turbo (API and UI), ChatGPT-4o (UI), and DeepSeek (UI) summaries, combining all 600 LLM responses to assess overall effects. Main predictor was text source (article, *NEJM JW*, or LLM (all LLMs combined, i.e. GPT-4 Turbo, ChatGPT-4o, and DeepSeek)), with a random effect for each article. Model (4) used the same set-up but with subtype of text source as main predictor, separating the individual LLMs (and LLM tests). Models (5) and (6) repeated this approach, using *NEJM JW* summaries as the reference instead of the articles. ^pc43

Model assumptions, including independence of observations, linearity of the logit, absence of multicollinearity and random effect significance, were assessed and met. Independence was ensured by including original text identifiers as a random effect, with source, temperature, test condition, and prompt as fixed effects. Linearity of the logit was assumed for the binary outcome (generalized versus restricted) and confirmed through model fit statistics. Variance inflation factors were within acceptable limits, indicating no multicollinearity among the fixed effects. The random effect was significant, supporting its inclusion. Analyses and visualizations were done using IBM SPSS 29.0 and R Studio. ^pc44
