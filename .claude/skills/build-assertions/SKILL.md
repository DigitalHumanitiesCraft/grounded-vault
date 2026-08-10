---
name: build-assertions
description: Synthesize cross-source assertions in 30_assertions from the distillates of a topic and register them in the topic map. Use when the distillates of a topic are to be turned into atomic statements, when a contradiction between sources has to be recorded, or when existing assertions are revised after machine review.
---

# Build assertions

Follow `knowledge/operations.md` § Build assertions for the synthesis procedure and the review prompt, and `knowledge/schema.md` § Assertion for frontmatter and section skeleton. The hard rules in `CLAUDE.md` apply unchanged, in particular that an own conclusion becomes a posit in the output and never an assertion.

1. Read every distillate the topic map registers, and group the statements that concern the same matter.
2. Write one atomic assertion per group, and list every supporting statement ID in `grounding`.
3. Split an irreconcilable group into two `contested` assertions linked in both directions; note a conclusion without support as a posit candidate, and read the appraisal sections of the distillates as posit candidates rather than as support.
4. Check every group for a displaced subject, meaning a statement whose passage supports it while its subject is not the matter the assertion is about. Either the source speaks about itself, about its own priority, reach or achievement, or it shows the matter in one state at one time, such as a restored object, a dated inventory or a plan. The first carries an assertion only with the speaker named, the second only with the state and its date named, and either may instead rest on a second and independent source. The coverage relation holds in both cases, so no check will stop you.
5. Register each assertion in its topic map, and put what the sources leave open under the map's open questions.
6. Run machine review over every assertion-statement pair, and rework whatever falls below *fully supports*.

Run `python tools/validate.py .` before reporting the assertions as done, and treat every warning as a finding.
