# Grounded Vault Agent Instructions

Read `CLAUDE.md` as the canonical action layer, then follow its session-start and task-routing instructions. The rules in `knowledge/` apply in every agent environment. Read `Codex.local.md` explicitly when present and keep machine-local instructions out of commits.

The repository root is the reusable template. `paper/` is a separate internal manuscript instance and has its own action layer. The public worked example is in `examples/prov-entity/`.

Use `uv sync --locked` and execute Python commands through `uv run python`. Before reporting tool changes as complete, run the Quickstart commands from `README.md`, which are the same set the CI workflow runs.
