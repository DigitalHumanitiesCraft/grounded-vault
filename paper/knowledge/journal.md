---
title: Journal
project:
  name: "Grounded Vault internal method manuscript"
  repository: "https://github.com/DigitalHumanitiesCraft/grounded-vault"
method:
  name: Promptotyping
  url: https://dhcraft.org/Promptotyping/
status: active
language: en
created: 2026-08-21
updated: 2026-09-27
related: [specification, state]
---

# Journal

Chronological decision and provenance record of the internal manuscript instance. Newest entries stand last.

## 2026-08-21 — One internal manuscript line

The earlier plan separated a German research blog from an English scholarly article on the same assertion layer. The source instance produced one validated blog chapter, while the article output directory remained empty. The two lines are consolidated here into one English methods manuscript. This manuscript is an internal research artefact and has no submission target. The Promptotyping paper remains a separate project and the publication line intended for submission.

## 2026-08-21 — Research foundation imported

The production foundation was copied from the read-only repository `chpollin/grounded-vault-paper` at commit `3045fb48b4ca4570498ff8628ca9995d40aa9374`. The imported Markdown representations, distillates, assertions, glossary records, references, and analysis scripts retain their source bytes and identifiers. The earlier blog chapter stays in the source repository as the historical output whose argument and empirical findings were incorporated into the new manuscript. Invariant schema, operations, validator, and reviewer remain at the target repository root, which avoids a second governance copy.

## 2026-08-21 — Consolidated manuscript validated

The imported production foundation contains 112 files whose SHA-256 hashes match the source commit. Inventory generation registered 29 sources in the instance state. Whole-instance and chapter-specific validation completed with zero errors and zero warnings. The root test suite completed with 111 passing tests after adding coverage for links in the generated project page. Root validation retains 32 warnings because the repository root remains an uninstantiated template with declared placeholders and empty production layers. These warnings do not arise from the nested manuscript instance. The project page was rebuilt from the updated canonical documents.

## 2026-09-05 — Template gains coverage and version records; the chapter loses its ready verdict

The template now asks two questions the chain did not ask. The source inventory carries per document representation the share of blocks the distillates anchor, and validation warns below half. In this instance eight of eighteen document representations fall below that share, the legal research tools study lowest, with roughly one block in nine anchored; each is either a distillate to extend or a scoping decision to record here. Publication distillates now name in `checked-against` the text version their quotation check ran on, and all nine of this instance's publications lack the field, because the intake records of the imported foundation did not carry it. The chapter therefore stands at NOT READY until the nine values are filled from the intake notes of the source repository; they cannot be reconstructed from the vault and are not guessed. Machine review with a reviewer from another model family remains the next step after that.

## 2026-09-05 — Version records filled from the instance's own references

The nine `checked-against` values were not in the source repository's journal, which does not exist, but in the `note` and `accessed` fields of the CSL records in `references/`, written at intake on 2026-08-10. The values are taken from there verbatim in substance: the publisher version for the attribution article, arXiv version 2 of 1 May 2024 for the jury paper, the named digitisations for the two historical method handbooks, and the page as accessed on 2026-08-10 for the five web sources. The `updated` date of the distillates stays at 2026-08-10, because the field records a property of the check that ran on that day and adds no content the check would have to cover again. The chapter is READY again; the eight coverage findings stand.

## 2026-09-22 — Subject binding for pinned and self-describing sources

The template changelog entry of 2026-08-10 names the displaced subject and asks running instances to walk their assertions for statements taken from a dated state. Six assertions of the Architecture topic rested only on the schema and operations documents of the template pinned at commit `c726eb5` of 2026-08-10 and stated the properties of the architecture as such. One assertion of the Agentic Workflow topic rested on the Promptotyping method paper in its review draft of 2026-07-31 and stated the method as such, while its distillate reports what the paper defines and states. Both are the state report and self-report cases of `knowledge/schema.md`. Each of the seven now names its state with commit or date in the H1 and in the first sentence of the statement, and the Promptotyping assertion names the method paper as its speaker. Their content, grounding, slugs and statement IDs are unchanged. The template provides no separate subject field, so the binding lives in the assertion sentence itself.

The seven assertions returned from `validated` to `grounded` and keep only the new validation date, because their machine review predates the changed wording. The manuscript sentences grounded in them now name the state as well, and the topic map entries carry it in their orientation clause. Whole-instance and chapter validation passed without errors or warnings.

The pass is limited to assertions grounded in pinned or self-describing sources. The three assertions on the machine review data of 2026-08-10 already name that date in their statements and stay unchanged. The Obsidian help and API documentation, the vendor post on context engineering and all other sources were not walked. The distillates of the pinned sources carry the commit in their lead and not in each statement, and they stay unchanged because their statement IDs and imported bytes are fixed.

Provenance. Decided by the main instance after delegation by the operator on 2026-09-22, revisable.

## 2026-09-26 — Terminology of the profile ingested; glossary entry re-grounded

The template now defines the distillate as the source-bound knowledge document of one source instead of the set of single statements extracted from it, and it defines every term in one place, `knowledge/index.md` § Terminology. The glossary entry `glossary/distillate.md` carried the old wording without an anchor. The Terminology section at commit `79cd1d3` was therefore ingested as the new source `grounded-vault-index-79cd1d3` and distilled with eighteen core statements, covering 18 of 25 blocks, and the glossary entry now quotes the new definition with an anchor into that representation. The schema representation at `c726eb5` stays untouched as the record of the earlier state. The assertion on the layer model still describes that earlier state and is listed as open work in [[knowledge/state]].

## 2026-09-27 — Subject binding and terminology ingest merged

The subject binding pass of 2026-09-22 and the terminology ingest of 2026-09-26 ran on separate lines and were merged. The open item the terminology entry names for `layer-model-assigns-each-layer-its-anchor-form` is settled by the subject binding pass, which already names commit `c726eb5` and its date in the H1 and the statement, so the assertion reports the earlier state as that state. It stays grounded in the schema representation at `c726eb5` and leaves the open work list. Machine review now has to cover both the seven rebound assertions and the terminology distillate.
