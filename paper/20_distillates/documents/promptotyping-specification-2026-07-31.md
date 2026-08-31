---
type: distillate
source-type: document
representation: "[[10_markdown/documents/promptotyping-specification-2026-07-31]]"
topics: ["[[Architecture]]", "[[Agentic Workflow]]", "[[Verification]]"]
status: validated
checked:
  validation: 2026-08-10
  machine-review: 2026-08-10
created: 2026-08-10
updated: 2026-08-10
---

# Distillate: Promptotyping, Specification of the Method, chapters 1 and 2

The method paper of Promptotyping in its review draft of 31 July 2026, from which the vault takes the definitions of the method, of its knowledge base, of its four forms of work, and of the four differentiated forms of checking.

## Core statements

- The paper defines Context Engineering as the systematic selection, organisation, maintenance and provision of the information an LLM-based system requires for its work, extends Prompt Engineering, understood as the iterative development of prompts, to the wider informational environment in which prompts are interpreted, and states that Context Engineering does not consist in placing all available material into a context window. [[10_markdown/documents/promptotyping-specification-2026-07-31#^p013]] ^s1

- The paper defines an AI agent as an LLM-based system that pursues a goal through a sequence of tool-supported actions and adapts to intermediate results, and Agentic Engineering as the systematic organisation of that extended work, covering task decomposition and coordination, tool use, the point at which human intervention is required, and how the work is inspected and continued. [[10_markdown/documents/promptotyping-specification-2026-07-31#^p014]] ^s2

- The paper defines an AI harness as the technical environment through which an agent receives context, accesses project resources, uses tools and obtains feedback, and states that agentic capability arises from the combined model, harness and environment system rather than from the model alone. [[10_markdown/documents/promptotyping-specification-2026-07-31#^p015]] ^s3

- The paper defines Promptotyping as an iterative, knowledge-driven method for developing project-specific digital research artefacts from structured research data and maintained project knowledge through Context Engineering and Agentic Engineering, whose organising structure is an evolving and versioned project knowledge base, and states that findings arising from implementation and examination are written back into that knowledge base. [[10_markdown/documents/promptotyping-specification-2026-07-31#^p019]] ^s4

- The paper states that the project knowledge base is a knowledge base in the sense of an explicitly represented body of knowledge that guides an agent's work, that it takes a semi-formal documentary form, and that it supports no formal inference. [[10_markdown/documents/promptotyping-specification-2026-07-31#^p020]] ^s5

- The paper describes the project knowledge base as interrelated documents that are bounded representations distilled from fuller research material, maintained for human inspection and revision, and available for inclusion in agents' task-specific working contexts, and it calls its three document types organisational heuristics rather than a prescribed file structure. [[10_markdown/documents/promptotyping-specification-2026-07-31#^p021]] ^s6

- The paper defines declarative knowledge documents as documents stating what the project currently takes to be the case and what the artefact is required to realise, naming a data, a requirements and a design document as examples. [[10_markdown/documents/promptotyping-specification-2026-07-31#^p022]] ^s7

- The paper defines process knowledge documents as documents preserving how the project's understanding developed and why decisions were taken, naming a journal and dedicated decision records as examples. [[10_markdown/documents/promptotyping-specification-2026-07-31#^p023]] ^s8

- The paper defines agent instruction documents as documents translating maintained project knowledge into operational guidance for agentic work, and states that keeping these comparatively volatile instructions separate from more stable accounts of data and scholarly purpose prevents temporary implementation directives from silently altering the project's maintained understanding. [[10_markdown/documents/promptotyping-specification-2026-07-31#^p024]] ^s9

- The paper introduces derived project artefacts as regenerable outputs produced from a referenced project state through an identified process, and holds them distinct from maintained project knowledge because they record derived observations rather than interpretations or decisions that project contributors have examined and adopted. [[10_markdown/documents/promptotyping-specification-2026-07-31#^p025]] ^s10

- The paper distinguishes the persistent project knowledge base, which preserves the project's maintained understanding and decisions, from an agent's task-specific working context, which holds the information and access required for a particular assignment, and states that retrieval and direct access to project resources supplement rather than replace the maintained account. [[10_markdown/documents/promptotyping-specification-2026-07-31#^p026]] ^s11

- The paper states that Context Engineering organises the task-specific information and project access available to an agent while Agentic Engineering structures how the agent acts within those conditions, that a carefully maintained knowledge base does not determine an adequate course of action and a well-organised agentic workflow cannot compensate for an inadequate account of the data or research purpose, and that Promptotyping treats selection as part of Context Engineering. [[10_markdown/documents/promptotyping-specification-2026-07-31#^p027]] ^s12

- The paper organises Promptotyping around the four recurrent phases of work Preparation, Exploration, Distillation and Implementation, calls them analytically distinct but not a fixed or exclusively linear sequence, and states that findings arising from Implementation may return the work to any earlier phase, most frequently to Distillation. [[10_markdown/documents/promptotyping-specification-2026-07-31#^p029]] ^s13

- The paper defines Distillation as the translation of the understanding produced through Preparation and Exploration into maintained knowledge documents from which implementation and verification can proceed, and calls it the principal documentary operation of Context Engineering within Promptotyping. [[10_markdown/documents/promptotyping-specification-2026-07-31#^p036]] ^s14

- The paper states that Distillation is not reducible to summarisation or context compression, that a model's nominal context capacity does not imply that all supplied information will be used reliably, and that Distillation creates an inspectable and selective representation preserving the distinctions, conditions and uncertainties required for adequate implementation and verification. [[10_markdown/documents/promptotyping-specification-2026-07-31#^p037]] ^s15

- The paper calls the sufficiency of Distillation practical rather than formal, testing it by whether a new contributor or agent instance can reconstruct the project's current logic and continue the assigned work without undocumented explanation, and states that successful implementation does not establish scholarly adequacy. [[10_markdown/documents/promptotyping-specification-2026-07-31#^p038]] ^s16

- The paper defines the promptotype as the accepted iteration state in which maintained project knowledge, the resulting digital research artefact, the referenced research-data state and the documented grounds of acceptance form a coherent and identifiable state for a stated purpose, assigns acceptance to the Critical Expert, and states that an agent may contribute proposals and assessments but cannot assume responsibility for their adequacy. [[10_markdown/documents/promptotyping-specification-2026-07-31#^p043]] ^s17

- The paper reports that the examination of the implemented workflows required several forms of checking with different evidential scope and authority, and states that in scholarly research adequacy depends not only on conformity to specified requirements but also on the interpretation of sources, the modelling decisions through which they are represented, and the purpose for which the resulting data are intended. [[10_markdown/documents/promptotyping-specification-2026-07-31#^p051]] ^s18

- The paper defines deterministic verification as testing conformity to formalised requirements through schemas, constraints, transformation tests, structural audits and reproducible measurements, and limits its conclusions to the properties encoded by the check, so that it does not establish that the requirements themselves are adequate. [[10_markdown/documents/promptotyping-specification-2026-07-31#^p052]] ^s19

- The paper defines agentic review as a bounded, tool-supported investigation in which one or more LLM-based agents examine outputs, data states, implementations or research artefacts against relevant sources, references, requirements and criteria. [[10_markdown/documents/promptotyping-specification-2026-07-31#^p053]] ^s20

- The paper defines Critical Expert verification and adjudication as accountable examination of particular outputs against their sources and the resolution of cases that deterministic or probabilistic procedures cannot determine, able to confirm, correct or reject previous findings, and recording who assumes responsibility for the resulting judgement. [[10_markdown/documents/promptotyping-specification-2026-07-31#^p054]] ^s21

- The paper defines scholarly validation as the assessment of whether the representations, requirements, evaluation criteria and artefacts governing the workflow are warranted by the research material and adequate for their intended scholarly purpose. [[10_markdown/documents/promptotyping-specification-2026-07-31#^p055]] ^s22

- The paper distinguishes agentic review from LLM-as-a-Judge, which it describes as typically evaluating a supplied output under a given reference or rubric and returning a score, ranking or judgement, and states that LLM-as-a-Judge can be one operation within agentic review. [[10_markdown/documents/promptotyping-specification-2026-07-31#^p056]] ^s23

- The paper makes the evidential value of agentic review depend on how the investigation is organised, and states that its findings remain probabilistic evidence rather than authorised verification, scholarly validation or acceptance. [[10_markdown/documents/promptotyping-specification-2026-07-31#^p057]] ^s24

- The paper reports that in one of its project cases, the ZBZ workflow, an earlier agent-screening process assigned approval labels although no responsible contributor had granted approval, that these labels were abolished and agent findings reclassified as provisional evidence pending operator adjudication, and it states that the capacity to inspect an output was thereby separated from the authority to record it as verified. [[10_markdown/documents/promptotyping-specification-2026-07-31#^p058]] ^s25

- The paper holds acceptance distinct from the forms of checking, defines it as the accountable decision through which an identifiable iteration state becomes a promptotype for a stated purpose, and states that acceptance may be bounded, so that an artefact can be accepted as an experimental processing pipeline or handover state without being accepted as a completed or publication-ready scholarly edition. [[10_markdown/documents/promptotyping-specification-2026-07-31#^p060]] ^s26

- The paper states that maintained project knowledge guides Implementation without determining a single adequate realisation, because natural-language descriptions retain ambiguity and different agent runs may realise the same requirement in materially different ways, and that formal conformity alone cannot establish scholarly adequacy, which is why the Critical Expert remains in the loop. [[10_markdown/documents/promptotyping-specification-2026-07-31#^p076]] ^s27

- The paper states that dividing agentic work among several agents does not transfer responsibility to them, that their assignments and permissions should remain explicit and auditable with access limited to the delegated task, and that increasing the number of agents may increase the work required to coordinate and audit their actions. [[10_markdown/documents/promptotyping-specification-2026-07-31#^p077]] ^s28

- The paper requires the accepted state to remain identifiable and reconstructable and the relation on which acceptance rests to remain recoverable through a repository release, an archived deposit or another durable reference, prescribes neither GitHub nor Semantic Versioning, and counts a renewed implementation using another model, harness or project state as a new iteration rather than a silent reproduction of the earlier promptotype. [[10_markdown/documents/promptotyping-specification-2026-07-31#^p079]] ^s29

## Terms

- **Promptotyping**: an iterative, knowledge-driven method for developing project-specific digital research artefacts from structured research data and maintained project knowledge through Context Engineering and Agentic Engineering. [[10_markdown/documents/promptotyping-specification-2026-07-31#^p019]]
- **Context Engineering**: the systematic selection, organisation, maintenance and provision of the information an LLM-based system requires for its work. [[10_markdown/documents/promptotyping-specification-2026-07-31#^p013]]
- **Agentic Engineering**: the systematic organisation of the extended, tool-supported work an agent performs. [[10_markdown/documents/promptotyping-specification-2026-07-31#^p014]]
- **AI harness**: the technical environment through which an agent receives context, accesses project resources, uses tools and obtains feedback. [[10_markdown/documents/promptotyping-specification-2026-07-31#^p015]]
- **Distillation**: the translation of the understanding produced through Preparation and Exploration into maintained knowledge documents from which implementation and verification can proceed. [[10_markdown/documents/promptotyping-specification-2026-07-31#^p036]]
- **Promptotype**: the accepted iteration state formed by maintained project knowledge, the digital research artefact, the referenced research-data state and the documented grounds of acceptance, for a stated purpose. [[10_markdown/documents/promptotyping-specification-2026-07-31#^p043]]
- **Agentic review**: a bounded, tool-supported investigation in which LLM-based agents examine outputs, data states, implementations or research artefacts against sources, references, requirements and criteria. [[10_markdown/documents/promptotyping-specification-2026-07-31#^p053]]
- **Critical Expert**: the person or group competent and accountable for judging whether the project knowledge adequately represents the research material and whether the artefact is suitable for its intended purpose. [[10_markdown/documents/promptotyping-specification-2026-07-31#^p043]]

## Open questions

- The paper states that agentic review yields probabilistic evidence but gives no rule for how much of it substitutes for, or reduces, human examination.
- It requires the accepted state to remain reconstructable without saying what minimum record makes a reconstruction possible.
- It names no procedure by which the adequacy of maintained project knowledge is judged apart from the practical test of continuation.

## Appraisal

A review draft, not peer-reviewed, written by the operator of this vault, and explicit about its own evidential limits, since it presents its project cases as methodologically guided reconstructions of documented practice rather than as comparative evaluation. Its strength for this vault lies in the definitions, which are stated rather than implied, and in the four differentiated forms of checking, which the vault's own three checking instances can be measured against. Its cases carry the weight of a single practice, so what follows from them about transferability stays a claim of the vault rather than a finding of the source.

## Related

- [[20_distillates/documents/pollin-2025-dissertation-ch74]]
- [[20_distillates/publications/anthropic-2025-context-engineering]]
