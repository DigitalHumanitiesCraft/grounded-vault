"""Refresh the invariant knowledge documents of the nested instances from the root.

Every instance is a copy of the template, so the instances nested in this
repository carry copies of knowledge/index.md, schema.md and operations.md.
tests/test_instances.py fails when a copy drifts from the root, and this tool
is the fix: it rewrites each copy from the root document, keeps the frontmatter
values the instance filled (project name, repository, created) and sets
updated to the given date.

Usage:
    python tools/sync_instances.py --date YYYY-MM-DD [INSTANCE ...]

Without instance paths it refreshes examples/prov-entity and paper where present.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

import yaml

from validate import iso_date, split_frontmatter

ROOT = Path(__file__).resolve().parents[1]
INVARIANT = ("index", "schema", "operations")
DEFAULT_INSTANCES = ("examples/prov-entity", "paper")


def sync(instance: Path, date: str) -> list[str]:
    written = []
    for doc in INVARIANT:
        copy = instance / "knowledge" / f"{doc}.md"
        current = yaml.safe_load(
            split_frontmatter(copy.read_text(encoding="utf-8").replace("\r\n", "\n"))[0]
        )
        text = (
            (ROOT / "knowledge" / f"{doc}.md")
            .read_text(encoding="utf-8")
            .replace("\r\n", "\n")
        )
        text = text.replace('"{{PROJECT_NAME}}"', f'"{current["project"]["name"]}"')
        text = text.replace('"{{REPOSITORY}}"', f'"{current["project"]["repository"]}"')
        text = text.replace('created: "{{DATE}}"', f'created: "{current["created"]}"')
        text = text.replace('updated: "{{DATE}}"', f'updated: "{date}"')
        if "{{" in text:
            raise SystemExit(
                f"{copy}: a placeholder of the root document has no value in the copy"
            )
        copy.write_text(text, encoding="utf-8", newline="")
        written.append(str(copy.relative_to(ROOT)))
    return written


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument(
        "--date", required=True, help="the updated date to record, ISO 8601"
    )
    parser.add_argument(
        "instances",
        nargs="*",
        help="instance roots, default examples/prov-entity and paper",
    )
    args = parser.parse_args(argv)
    if iso_date(args.date) is None:
        parser.error(f"not a strict ISO date YYYY-MM-DD: {args.date!r}")
    roots = [ROOT / p for p in args.instances] or [
        ROOT / p for p in DEFAULT_INSTANCES if (ROOT / p).is_dir()
    ]
    for instance in roots:
        for path in sync(instance, args.date):
            print(f"OK {path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
