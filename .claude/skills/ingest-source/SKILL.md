---
name: ingest-source
description: Bring a document or data source into 10_markdown as a Markdown representation with minted block IDs, or register a citable-only publication in references/. Use when a new original file, dataset or bibliographic record has to enter the vault.
---

# Ingest a source

The procedure is written once, in `knowledge/operations.md` § Acquire (channels, where an original or a bibliographic record goes) and § Ingest (converter choice, the two-step conversion, the per-source-type handling and the inventory run). The document skeletons are in `knowledge/schema.md` § Document types and § Source metadata. Follow those sections as written, and apply the hard rules of `CLAUDE.md` unchanged.

Run `uv run python tools/validate.py .` before reporting the ingest as done, and act on its findings as `knowledge/operations.md` § Check says.
