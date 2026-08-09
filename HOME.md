# {{PROJECT_NAME}}

Human entry point of this vault. What this vault produces and on what topic is stated in the purpose section of [[knowledge/specification]]. Every load-bearing statement here is anchored to its source material, and the checking state of every statement is readable at the statement itself.

## The chain

```
00_sources → 10_markdown → 20_distillates → 30_assertions → 40_output
```

`00_sources/` holds the originals as they arrived and stays unchecked, because it is the material every layer above it is checked against. `10_markdown/` holds the Markdown representations with their block anchors, and every anchor above binds downward from there.

## Read the output

- [[40_output/]] — the chapters. Footnotes lead to assertions; click through to the supporting passages.

## Explore the knowledge

<!-- Instantiation: replace the line below with one wikilink per topic of the controlled
     topic set, in the same order as the MOC files created in 30_assertions/. -->

- Topic maps: one per topic of the controlled topic set, in `30_assertions/`.
- [[glossary/]] — the project's terms.

## Understand the machine room

- [[knowledge/index]] — navigation and terminology.
- [[knowledge/state]] — source inventory and chapter register.
- [[knowledge/journal]] — why things are the way they are.

## How to read a status

`grounded` means an agent produced the anchor structure. `validated` means deterministic checks and an adversarial machine review passed. `verified` means the human expert confirmed it; only this is evidence. `contested` means sources conflict, which is itself information.
