---
name: build-assertions
description: Synthesize assertions in 30_assertions from the distillates of a topic and register them in the topic map. Use when the distillates of a topic are to be turned into atomic statements, when a contradiction between sources has to be recorded, or when existing assertions are revised after machine review.
---

# Build assertions

Follow `knowledge/operations.md` § Build assertions for the synthesis procedure and the review prompt, § Check for the machine review contract, and `knowledge/schema.md` § Assertion for frontmatter and section skeleton. The hard rules in `CLAUDE.md` apply unchanged, in particular that no own conclusion is filed as an assertion.

1. Read every distillate whose `topics` names the topic, and group the statements that concern the same matter.
2. Write one atomic assertion per group, and list every supporting statement ID in `grounding`.
3. Split an irreconcilable group into two `contested` assertions linked in both directions. Note a conclusion without support as a posit candidate, and read the appraisal sections of the distillates as posit candidates rather than as support.
4. Check every group for a displaced subject as `knowledge/operations.md` § Build assertions step 5 says. Machine review reports a displaced subject the assertion does not name as *overreaches*.
5. Register each assertion in its topic map, and put what the sources leave open under the map's open questions.
6. Run machine review over every assertion-statement pair, and rework whatever falls below *fully supports*.

Run `python tools/validate.py .` before reporting the assertions as done, and act on its findings as `knowledge/operations.md` § Check says.
