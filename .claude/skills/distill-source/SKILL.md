---
name: distill-source
description: Produce the distillate of one ingested source in 20_distillates, each core statement carrying exactly one anchor into its source. Use when a source has been ingested and its core statements are to be extracted, or when an existing distillate has to be reworked after a failed fidelity or review check.
---

# Distill a source

The procedure is written once, in `knowledge/operations.md` § Distill (the three-stage chain, the canonical extraction prompt, the fidelity and quotation checks with their records, the coverage question and the appraisal). The frontmatter and section skeleton are in `knowledge/schema.md` § Distillate. Follow those sections as written, and apply the hard rules of `CLAUDE.md` unchanged.

Run `uv run python tools/validate.py .` before reporting the distillate as done, and act on its findings as `knowledge/operations.md` § Check says.
