# Grounded Vault Agent Instructions

Read `CLAUDE.md` as the canonical action layer, then follow its session-start and task-routing instructions. The rules in `knowledge/` apply in every agent environment. Read `Codex.local.md` explicitly when present and keep machine-local instructions out of commits.

The repository root is the reusable template. `paper/` is the internal manuscript instance and `examples/prov-entity/` the public worked example. Each carries its own action layer `CLAUDE.md` and its own copies of the invariant knowledge documents, which `tests/test_instances.py` holds equal to the root and `tools/sync_instances.py` refreshes.

Use `uv sync --locked` and execute Python commands through `uv run python`. Before reporting tool changes as complete, run the Quickstart commands from `README.md`, which are the same set the CI workflow runs.
