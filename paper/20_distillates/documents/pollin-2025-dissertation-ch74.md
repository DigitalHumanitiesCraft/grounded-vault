---
type: distillate
source-type: document
representation: "[[10_markdown/documents/pollin-2025-dissertation-ch74]]"
topics: ["[[Architecture]]", "[[Agentic Workflow]]"]
status: validated
checked:
  validation: 2026-08-10
  machine-review: 2026-08-10
created: 2026-08-10
updated: 2026-08-10
---

# Distillate: Pollin 2025, dissertation chapter 7.4

The chapter in which the term Promptotyping is first introduced, as an outlook on LLM-supported interface development following the DEPCHA implementation and its limitations.

## Core statements

- The chapter reports that the aim of Theme 3, implementing functionalities that support the exploration of historical financial information through web interfaces based on scholar-centred design, was addressed by combining iterative engagement with historians' non-linear research practices, a targeted review of selected Digital Humanities projects with relevant visualisation and interface solutions, and an interface implementation in DEPCHA based on semantic web technologies, TEI XML encoding and structured research data. [[10_markdown/documents/pollin-2025-dissertation-ch74#^b1]] ^s1

- The chapter names limitations of the DEPCHA implementation, among them that the system does not currently address uncertainty, largely because the project prioritised semantic structures and core functionality, and that the reliance on stable data structures and predefined workflows in digital repository systems constrains customisation. [[10_markdown/documents/pollin-2025-dissertation-ch74#^b2]] ^s2

- The chapter introduces Promptotyping as a methodology that merges prompt engineering with user-centred design to produce customisable web interfaces, proceeding through systematically structured cycles in which requirements are gathered as epics, user stories and domain contexts into Promptotype Documents, described there as context-compressed Markdown files, then run through an analysis, a design and a prototyping phase with domain experts engaged in continuous validation cycles, and it states that this approach requires empirical evaluation to determine its effectiveness. [[10_markdown/documents/pollin-2025-dissertation-ch74#^b3]] ^s3

- The chapter illustrates the method on DEPCHA, where epics and user stories define tasks related to the Wheaton Day Book while the Bookkeeping Ontology and TEI XML serve as data models. [[10_markdown/documents/pollin-2025-dissertation-ch74#^b4]] ^s4

- The chapter prints a Promptotyping template as Code Example 32. [[10_markdown/documents/pollin-2025-dissertation-ch74#^b5]] ^s5

- The chapter maps the template sections onto the phases of the method, with epics and user stories informing the analysis phase, Domain Context and Data Model supporting the design phase, and Design Document and Implementation Instructions guiding the prototyping phase, and it states that each section's content passes through the experts-in-the-loop validation cycle. [[10_markdown/documents/pollin-2025-dissertation-ch74#^b6]] ^s6

- The chapter states that this approach necessitates high-performance computing infrastructure and specialised AI models currently provided primarily through corporate platforms, which introduces dependencies on proprietary technologies and raises questions of academic autonomy and sustainable development practice, while the chapter attributes considerations of energy consumption and environmental impact to the computational requirements of interface generation and refinement. [[10_markdown/documents/pollin-2025-dissertation-ch74#^b7]] ^s7

## Terms

- **Promptotyping**: as used in this chapter, a methodology that merges prompt engineering with user-centred design to produce customisable web interfaces. [[10_markdown/documents/pollin-2025-dissertation-ch74#^b3]]
- **Promptotype Documents**: the concise, context-compressed Markdown files into which epics, user stories and domain contexts are recorded. [[10_markdown/documents/pollin-2025-dissertation-ch74#^b3]]
- **Experts-in-the-loop**: the validation arrangement in which Digital Humanities developers and domain scholars take part in the validation process. [[10_markdown/documents/pollin-2025-dissertation-ch74#^b3]]

## Open questions

- The chapter names the phases analysis, design, prototyping and evaluation but does not say by what criterion a phase is finished or an iteration accepted.
- It calls the Promptotype Documents context-compressed without stating what is compressed away or by what rule.
- It asserts that empirical evaluation is still owed and names no evaluation design.

## Appraisal

The earliest written statement of the term in this source situation, and therefore the point of origin the vault needs, but it is an outlook section of a thesis whose subject lies elsewhere, so its account stays programmatic. The method is described from the phase model of the older prompt-engineering framing, and the passage itself concedes that empirical evaluation is outstanding. For the vault it carries the origin and the early terminology; the load-bearing method definition must come from the later specification.

## Related

- [[20_distillates/documents/promptotyping-specification-2026-07-31]]
