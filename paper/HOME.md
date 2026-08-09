# Grounded Vault Paper

Human entry point of this vault. What this vault produces and on what topic is stated in the purpose section of [[knowledge/specification]]. Every load-bearing statement here is anchored to its source material, and the checking state of every statement is readable at the statement itself.

## The chain

```
00_sources → 10_markdown → 20_distillates → 30_assertions → 40_output
```

`00_sources/` holds the originals as they arrived and stays unchecked, because it is the material every layer above it is checked against. `10_markdown/` holds the Markdown representations with their block anchors, and every anchor above binds downward from there.

## Read the output

- [[40_output/]] — the chapters. Footnotes lead to assertions; click through to the supporting passages. The chapter register in [[knowledge/state]] holds the intended shape of the article.

## Explore the knowledge

- [[30_assertions/MOC-Provenance]] — what an anchor is, what it guarantees, and where provenance is enforced rather than reported.
- [[30_assertions/MOC-Verification]] — the three checking instances, their authority and the human bottleneck at the top rung.
- [[30_assertions/MOC-Architecture]] — the layer chain, the anchor mechanics per source type and the status ladder.
- [[30_assertions/MOC-Agentic-Workflow]] — how producing agents, reviewing models and human roles divide the work.
- [[30_assertions/MOC-Instances]] — the two real instances, their source situations, migrations and measured runs.
- [[glossary/]] — the project's terms.

## Understand the machine room

- [[knowledge/index]] — navigation and terminology.
- [[knowledge/state]] — source inventory and chapter register.
- [[knowledge/journal]] — why things are the way they are.

## How to read a status

`grounded` means an agent produced the anchor structure. `validated` means deterministic checks and an adversarial machine review passed. `verified` means the human expert confirmed it; only this is evidence. `contested` means sources conflict, which is itself information.
