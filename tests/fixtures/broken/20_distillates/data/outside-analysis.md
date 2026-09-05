---
type: distillate
source-type: data
representation: "[[10_markdown/documents/note]]"
topics: ["[[Broken]]"]
status: grounded
checked: {}
created: 2026-09-05
updated: 2026-09-05
---

# Distillate: Computation outside the analysis folder

Fixture: the computation names a script outside `tools/analysis/`, which the validator refuses to run (defect: computation anchor, trust boundary).

## Core statements

- This statement rests on a script the vault may not execute. ^s1
  - computation: `python tools/validate.py` → `42`

## Related
