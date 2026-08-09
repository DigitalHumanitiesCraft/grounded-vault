# Examples

Two example instances, both fixtures for `tests/test_validate.py` and documentation by example. Their content is fictional.

- `minimal/` — a complete valid pass through every layer: one source per source type (document, publication, data), one distillate each, one claim grounded across all three, one deliverable paragraph with a grounded footnote and a posit. Its `knowledge/state.md` is the inventory register that records the Markdown representations and distillates. `python tools/validate.py examples/minimal --run-computations` passes clean and without a warning.
- `broken/` — one specimen per defect class the validator must catch: dead block reference, topic outside the backbone, orphan claim, one-sided contested relation, illegal frontmatter, status without recorded checks, missing computation script, unrecorded quotation check, footnote without keyword, marker without definition, mirror out of sync, document in no inventory register. Each fixture names its own defect in its lead sentence.

Keep this folder in your instance. The suite that proves the validator catches anything at all has no other subject, and without the fixtures those tests run against directories that do not exist, where passing means nothing.

The validator reads only the content folders and the inventory register at the root it is given, so the fixtures stay invisible to a run over the vault itself and can be broken deliberately without touching the evidence layer.
