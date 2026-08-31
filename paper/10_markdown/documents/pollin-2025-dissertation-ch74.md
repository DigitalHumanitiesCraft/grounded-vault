---
type: representation
source-type: document
source: "[[00_sources/pollin-2025-diss.pdf]]"
converter: "PyMuPDF, with agent post-editing of broken ligature and quotation glyphs"
channel: handover
metadata:
  title: "Modelling, Operationalising and Exploring Historical Information. Using Historical Financial Sources as an Example — chapter 7.4"
  creator: "Christopher Pollin, Department of Digital Humanities, University of Graz (vault operator)"
  date: "2025"
  format: "pdf"
  identifier: "https://resolver.obvsg.at/urn:nbn:at:at-ubg:1-220602"
  license: "CC-BY-4.0; open access at the University of Graz repository without a stated licence, released under CC BY 4.0 here by the author, who is the vault operator."
  confidential: false
created: 2026-08-10
updated: 2026-08-10
---

# 7.4 LLM-Supported Prototyping and Exploration: Promptotyping

Scope: chapter 7.4 of the dissertation, printed pages 216 to 219, taken from the doctoral thesis submitted to the University of Graz in 2025. The remaining chapters are not represented in this vault. The PDF carries a defective ToUnicode mapping, so ligatures, apostrophes, en dashes and quotation marks were restored from the rendered glyphs; wording, spelling and punctuation are otherwise unchanged, including the misspelling "Experimantal". Footnote 233 is anchored in section 7.3 and is therefore omitted.

The overall aim of Theme 3 – how to implement functionalities to support the exploration of historical financial information through web interfaces based on scholar-centred design – has been achieved by combining (1) iterative engagement with historians’ non-linear research practices, (2) targeted review of selected Digital Humanities projects with relevant visualisation and interface solutions, and (3) an interface implementation in DEPCHA based on semantic web technologies, TEI XML encoding, and structured research data. RQ3a is addressed by demonstrating how working closely with historians supports interface decisions, ensuring that systems such as DEPCHA remain adaptable and transparent so that it is possible to understand how the interface and visualisations are created, thereby illustrating how scholar-centred design principles and historians’ information-seeking behaviour inform the development of combined visualisation and web interface design for historical research. RQ3b is addressed by the discussion of Digital Humanities projects (e.g., WarSampo, ResearchSpace, InTaVia) that use semantic modelling, knowledge graphs, and diverse visualisation techniques and interfaces to offer multiples and interactive views on research data, clarifying how existing information systems have implemented combined visualisation and web interface design to support scholarly engagement with cultural heritage and historical sources. Finally, RQ3c finds tangible expression in DEPCHA’s suite of interrelated views – Collections, Edition and Dashboard View – complemented by Experimantal Views such as network and treemap web-based information visualisations, demonstrating how the DEPCHA implementation follows these design principles for exploring and analysing historical financial information, while also highlighting current limitations. Reflections on these findings suggest a shift away from purely linear presentation methods towards multi-dimensional interfaces that capture the complex interrelationships within historical datasets. This shift aligns with established theoretical frameworks such as Ingwersen’s Cognitive Model and Marchionini’s Exploratory Search Model, both of which emphasise iterative, feedback-oriented approaches. ^b1

Following DEPCHA’s implementation results, several limitations warrant reflection. The system does not currently address uncertainty, largely because the project prioritised semantic structures and core functionality. Although recognising and visualising ambiguity is essential for scholarly accuracy, modelling uncertainty within standards such as TEI and RDF, and incorporating it into interface components, proved too complex at this stage. The generalised nature of the Dashboard View, although helpful for broad overviews, can overlook the requirements of, for instance, social and economic historians, potentially flattening context-specific details. Experimental features like interactive network visualisations and treemaps offer promising directions for more granular analysis, but fully integrating them into the platform would require significant adjustments to the underlying research data workflows and current implementation. The reliance on stable data structures and predefined workflows in digital repository systems necessitates certain constraints on customisation capabilities, as structured metadata and standardised processes inherently limit the flexibility of implementation solutions. ^b2

These limitations in flexibility and customisation capabilities point to the need for more agile development approaches in Digital Humanities research interfaces. The exploration of LLM-supported approaches to research interface development (RQ4c) introduces the concept of Promptotyping, a methodology that merges prompt engineering with user-centred design to produce customisable web interfaces. Promptotyping proceeds through systematically structured cycles, beginning with requirements gathering recorded as epics, user stories, and domain contexts into concise Promptotype Documents – context-compressed Markdown files capturing all relevant semantics. The analysis phase systematically identifies specific tasks and research needs, while the design phase employs prompt engineering methods to convert these into functional and technical specifications. During the prototyping phase, frontier LLMs (such as the o1 model family) leverage advanced prompting techniques – including CoT or ToT – to generate and refine both reasoning steps and prototype code for interface components. Throughout these phases, the evaluation process engages domain experts in continuous validation cycles, ensuring consistent alignment with scholarly objectives and requirements. The cyclical feedback loop harnesses model reasoning capabilities while remaining mindful of technical constraints like context window size and potential limitations arising from bias and hallucinations, which are actively mitigated through an experts-in-the-loop approach incorporating both Digital Humanities developers and domain scholars in the validation process. The Promptotyping approach, combining Markdown-based specifications with frontier AI models and prompt engineering, requires empirical evaluation to determine its effectiveness for developing customisable research interfaces. ^b3

Code Example 32 shows a general Promptotyping template. In the DEPCHA example, epics and user stories (see Chapter 4.6.4) define tasks related to the Wheaton Day Book, while the Bookkeeping Ontology and TEI XML serve as data models. By systematically capturing this context in Markdown and leveraging frontier LLMs with advanced prompting, developers can rapidly build and refine specialised interfaces for historical financial information. ^b4

````
## Epics and User Stories
```
* [Insert your high-level epics here: large-scale requirements or use cases]
  * [Insert individual user stories here, e.g., "As a [user role], I want to
[action], so that I can [benefit]."]
```
## Domain Context
```
[Describe the domain, background, key terminology, and constraints]
```

## Data Model
```
[Include an outline or schema of the data you'll be using, referencing
tables, relationships, or data formats]
```

## Design Document
```
[Provide design specifications, UI/UX notes, architecture diagrams, or
wireframes]
```

## Implementation Instructions
```
[Detail any technical guidelines, frameworks, libraries, or coding styles to
follow]
```
````

Code Example 32: Promptotyping Template ^b5

This template structure maps directly to the Promptotyping methodology’s phases: the epics and user stories sections inform the analysis phase by capturing scholarly requirements; the Domain Context and Data Model sections support the design phase by providing the semantic foundation for prompt engineering; whilst the Design Document and Implementation Instructions guide the prototyping phase where LLMs generate interface components. For instance, in DEPCHA’s implementation, the Domain Context incorporates the Bookkeeping Ontology, which informs the generation of specialised visualisation components through targeted prompting techniques. Each section's content is systematically processed through the experts-in-the-loop validation cycle, ensuring the generated interfaces maintain scholarly rigour whilst enabling rapid iteration. ^b6

The development of scholar-centred interfaces facilitated by Promptotyping methodologies demonstrates the potential of integrating information, models, and frontier LLM capabilities in Digital Humanities tasks. This approach necessitates high-performance computing infrastructure and specialised AI models, currently provided primarily through corporate platforms, introducing dependencies on proprietary technologies. Such reliance raises questions regarding academic autonomy and sustainable development practices. The computational requirements for interface generation and refinement present considerations about energy consumption and environmental impact.[234] As Digital Humanities continues to integrate AI-driven methodologies, the field faces the task of balancing enhanced research capabilities with sustainability, institutional independence, and ethical considerations in AI deployment – factors that influence the development of digital research infrastructure. Ultimately, these findings underscore how the Promptotyping framework can streamline the creation of flexible, scholar-centric tools while highlighting the need for responsible governance of emerging technologies. This balance between innovation and accountability not only facilitates more nuanced historical analysis but also offers a blueprint for sustainable, open, and ethically grounded infrastructure across the Digital Humanities. ^b7

234 Digital Humanities infrastructure exemplifies Crawford's Atlas of AI (2021) analysis of technological systems as resource-extractive. The Greening DH initiative responds through concrete measures: standardised formats, versioning protocols and sustainable archiving strategies, addressing the material implications of digital scholarship. https://dhd-greening.github.io ^b8
