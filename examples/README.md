# Examples

Two example instances, both fixtures for `tests/test_validate.py` and documentation by example. Their content is fictional.

- `minimal/` — a complete valid pass through every layer: one source per source type (document, publication, data), one distillate each, one claim grounded across all three, one deliverable paragraph with a grounded footnote and a posit. `python tools/validate.py examples/minimal --run-computations` passes clean.
- `broken/` — one specimen per defect class the validator must catch: dead block reference, topic outside the backbone, orphan claim, one-sided contested relation, illegal frontmatter, status without recorded checks, missing computation script, unrecorded quotation check, footnote without keyword, marker without definition, mirror out of sync.

Delete this folder after instantiating the template.
