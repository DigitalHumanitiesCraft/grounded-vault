---
type: distillate
source-type: data
representation: "[[10_markdown/documents/note]]"
topics: ["[[Broken]]"]
status: grounded
checked: {}
created: 2026-09-27
updated: 2026-09-27
---

# Distillate: Computation defects

Fixture: each statement below declares its computation in a way the validator refuses, a stated result the script does not print, a script that fails, no script at all, a path that walks out of `tools/analysis/`, arguments after the script, and no computation (defect: computation anchor).

## Core statements

- The stated result differs from what the script prints. ^s1
  - computation: `python tools/analysis/answer.py` → `41`
- The script exits with an error. ^s2
  - computation: `python tools/analysis/fails.py` → `42`
- The computation names a module instead of a script. ^s3
  - computation: `python -m answer` → `42`
- The script path climbs out of the analysis folder. ^s4
  - computation: `python tools/analysis/../../outside.py` → `42`
- The script is called with an argument. ^s5
  - computation: `python tools/analysis/answer.py --verbose` → `42`
- This statement declares no computation at all. ^s6

## Related
