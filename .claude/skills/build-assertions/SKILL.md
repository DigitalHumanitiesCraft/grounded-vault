---
name: build-assertions
description: Synthesize assertions in 30_assertions from the distillates of a topic and register them in the topic map. Use when the distillates of a topic are to be turned into atomic statements, when a contradiction between sources has to be recorded, or when existing assertions are revised after machine review.
---

# Build assertions

The procedure is written once, in `knowledge/operations.md` § Build assertions (the eight steps from entering through the topic map to registering the assertion, the displaced-subject check, contested pairs, posit candidates and the assertion review prompt) and § Check for the machine review contract. The frontmatter and section skeleton are in `knowledge/schema.md` § Assertion. Follow those sections as written, and apply the hard rules of `CLAUDE.md` unchanged.

Run `uv run python tools/validate.py .` before reporting the assertions as done, and act on its findings as `knowledge/operations.md` § Check says.
