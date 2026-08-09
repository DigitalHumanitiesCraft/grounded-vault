---
title: State
project:
  name: "Grounded Vault Paper"
  repository: "DigitalHumanitiesCraft/grounded-vault"
method:
  name: Promptotyping
  url: https://dhcraft.org/Promptotyping/
status: draft
language: en
created: "2026-08-09"
updated: "2026-08-09"
related: [operations, journal]
---

# State

Everything volatile in one place, so the rule documents stay stable. Update rows here as work proceeds; never record processing state anywhere else.

## Source inventory

One row per source. Processing status: `new` → `ingested` → `distilled`. No source has entered yet; acquisition is the next chain to run.

| Source | Type | Channel | Markdown representation | Distillate | Status |
|---|---|---|---|---|---|
| | | | | | |

## Chapter register

One row per chapter of the output. Writing status mirrors the chapter's frontmatter once the file exists; `planned` marks a chapter that has no file yet. The register holds the intended shape of the article, and no chapter has been written.

| Chapter | File | Status | Notes |
|---|---|---|---|
| 1. Introduction | `40_output/01-introduction.md` | planned | The problem of unauditable model output and the claim that provenance is enforceable structurally. Carries claim 1. |
| 2. Related work | `40_output/02-related-work.md` | planned | Provenance models, scholarly editing practice, retrieval-augmented generation and agentic knowledge systems. Rests on the `publication` sources. |
| 3. Architecture | `40_output/03-architecture.md` | planned | The layer chain, the anchor mechanics per source type, the three checking instances and the status ladder. Carries claims 4 and 6. |
| 4. The two instances | `40_output/04-instances.md` | planned | Case description of both real instances, their source situations and their migrations. Carries claim 3. |
| 5. Findings | `40_output/05-findings.md` | planned | What the migrations and the review runs show, read off the `data` sources. Carries claims 2 and 5. |
| 6. Limitations | `40_output/06-limitations.md` | planned | The missing controlled comparison, the human bottleneck, the retroactivity limit and the scope of what an anchor guarantees. Restates the negative half of claims 2, 4 and 6. |
| 7. Conclusion | `40_output/07-conclusion.md` | planned | What the architecture settles and what it leaves open. |

## Open work

<!-- Short, current list; done items are deleted, decisions go to the journal. -->

- Acquire the instance histories of both real instances as `document` sources, meaning journals, commit logs and check reports.
- Assemble the validator run counts of both migrations into one `data` source with a deterministic computation over it.
- Locate the related literature for chapter 2 and export it as CSL JSON into `references/`.
- Decide per claim whether it reaches an assertion or has to enter the article as a posit, once the sources are distilled.
