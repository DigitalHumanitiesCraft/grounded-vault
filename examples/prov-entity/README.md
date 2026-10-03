# PROV-DM entity worked example

The example follows the entity definition in the [dated PROV-DM Recommendation](https://www.w3.org/TR/2013/REC-prov-dm-20130430/#term-entity) through a complete source-to-output chain. [HOME](HOME.md) provides the reading path, and [knowledge/specification](knowledge/specification.md) records the example parameters.

## Source and rights

The retained source is one selected excerpt in [00_sources/prov-entity.txt](00_sources/prov-entity.txt). The complete Recommendation is available at the original URL. Its status and copyright notice accompany the excerpt. The source retains the [W3C document license](https://www.w3.org/copyright/document-license-2023/), which permits redistribution of portions with the required notices. Authored example prose is licensed under CC BY 4.0. [manifest.json](manifest.json) records the exact source and immutable Markdown representation using SHA-256 hashes.

## Run the deterministic checks

Run the commands from the repository root. The example uses the repository tools and dependencies.

```sh
uv sync --locked
uv run python tools/inventory.py examples/prov-entity --write
uv run python tools/validate.py examples/prov-entity
uv run python tools/validate.py examples/prov-entity --chapter 40_output/01-entity-definition
uv run pytest tests/test_example.py
```

Validation checks structure and resolvable anchors. A clean chapter result establishes formal conformance. Human verification remains with the designated reader.

The committed distillate, assertion and chapter stand at `validated`. Formal validation ran on 3 October 2026. A Codex subagent with fresh context judged the exported source and assertion prompts, and the actual results are retained in [checks/review-2026-10-03.jsonl](checks/review-2026-10-03.jsonl). The reviewer used the inherited session default. Independence across model families was not established, and human verification has not been performed.

## Review the supporting pairs

Export the pairs into a directory outside the repository, then give each exported prompt to an independently instructed reviewer. Keep the producer's reasoning out of the review prompt. The placeholder paths below refer to local files selected for the review.

```sh
uv run python tools/review.py emit examples/prov-entity --out <prompts.jsonl>
```

Each exported record contains an `id`, its `prompt` and a `prompt_hash`. The hash binds the review to the exact prompt. Preserve the exported `id` and `prompt_hash` in the returned record, and supply the actual judgement. The response schema is:

```json
{"id": "<exported id>", "prompt_hash": "<exported prompt_hash>", "verdict": "<actual verdict>"}
```

The allowed verdicts are `fully supports`, `partially supports`, `overreaches`, `contradicts` and `not in the text`. Only `fully supports` passes. An actual reviewer may instead return `response`, with the verdict on its first line and a justification after it. Record the reviewer and actual review date alongside the verdicts.

```sh
uv run python tools/review.py judge examples/prov-entity --verdicts <verdicts.jsonl>
uv run python tools/review.py judge examples/prov-entity --verdicts <verdicts.jsonl> --apply
uv run python tools/validate.py examples/prov-entity
```

The first judge command reports results without changing the example. Use `--apply` only for genuine returned judgements. It records `checked.machine-review` on documents whose pairs all pass. Status advancement additionally requires an actual clean validation and its recorded date. It must respect the status of the supporting documents. Human expert verification alone permits `verified`.

The regression test uses explicitly simulated judgements inside a temporary copy to exercise the export and import commands. That simulation establishes no semantic review of the committed example.
