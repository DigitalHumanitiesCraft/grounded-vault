# {{PROJECT_NAME}}

Human entry point of this vault. What this vault produces and on what topic is stated in the purpose section of [[knowledge/specification]]. Every load-bearing statement here is anchored to its source material, and the checking state of every statement is readable at the statement itself.

## The chain

```
00_sources → 10_markdown → 20_distillates → 30_assertions → 40_output
```

`00_sources/` holds the originals as they arrived, and `10_markdown/` their Markdown representations with the block anchors that every layer above binds to. The layer rules are set out in [[knowledge/schema]] § Layer model, the handling of originals in [[knowledge/operations]] § Acquire.

## Read the output

- `40_output/` holds the chapters. Footnotes lead to assertions, and from there you click through to the supporting passages.

## Explore the knowledge

<!-- Instantiation: replace the line below with one wikilink per topic of the controlled
     topic set, in the same order as the MOC files created in 30_assertions/. -->

- One topic map per topic of the controlled topic set, in `30_assertions/`.
- `glossary/` holds the project's terms.

## Understand the machine room

- [[knowledge/index]] for navigation and terminology.
- [[knowledge/state]] for the source inventory and the chapter register.
- [[knowledge/journal]] for why things are the way they are.

## How to read a status

What each status means is defined under status ladder in [[knowledge/index]] § Terminology, and which check sets it in [[knowledge/operations]] § Check.
