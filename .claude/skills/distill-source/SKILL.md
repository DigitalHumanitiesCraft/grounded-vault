---
name: distill-source
description: Produce the distillate of one ingested source in 20_distillates, with one anchored statement per source location. Use when a source has been ingested and its core statements are to be extracted, or when an existing distillate has to be reworked after a failed fidelity or review check.
---

# Distill a source

Follow `knowledge/operations.md` § Distill for the three-stage chain and the canonical extraction prompt, and `knowledge/schema.md` § Distillate for frontmatter and section skeleton. The hard rules in `CLAUDE.md` apply unchanged; statement IDs are minted here and nowhere else.

1. Extract the core statements of this one source with the canonical prompt, one statement per anchor, without evaluation, interpretation or cross-source merging.
2. Format deterministically into the section skeleton, with statement IDs and the anchor syntax the source type requires.
3. Run the fidelity check against each anchor, for publications including the quotation check recorded as `checked.quote`.
4. Iterate: reformulate or discard a statement that fails, and check again until every remaining statement passes.
5. Where the source is to be judged, write the optional Appraisal section afterwards, with no ID on any of its lines.
6. Set `status: grounded` and regenerate the source inventory with `python tools/inventory.py . --write`.

Run `python tools/validate.py .` before reporting the distillate as done, and treat every warning as a finding.
