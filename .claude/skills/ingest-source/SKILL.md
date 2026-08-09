---
name: ingest-source
description: Bring a source from 00_sources into 10_markdown as a Markdown representation. Use when a new original file, dataset or bibliographic record has to enter the vault, when a source is to be converted to Markdown, or when block IDs have to be minted for a source.
---

# Ingest a source

Follow `knowledge/operations.md` § Acquire and § Ingest; that section is authoritative for converter choice, the two-step conversion and the per-source-type handling. The hard rules in `CLAUDE.md` apply unchanged, in particular that anchors are minted only at their own layer and that a Markdown representation is never edited after ingest.

1. Record the channel and place the original in `00_sources/`, or export the record into `references/` where the source is citable only.
2. Convert to structure-preserving Markdown with the converter the decision list names, and record it in `converter`.
3. Mint a block ID on every anchor-relevant paragraph, set the H1 from the original, fill the metadata block per `knowledge/schema.md`.
4. Update the source inventory row in `knowledge/state.md` to `ingested`.

Run `python tools/validate.py .` before reporting the ingest as done, and treat every warning marked `*` as a finding.
