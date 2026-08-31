"""Recorded verdicts below fully supports, per layer."""

import csv
from collections import Counter
from pathlib import Path

DATA = Path("10_markdown/data/review-findings-2026-08-10.csv")


def main() -> None:
    failures: Counter[str] = Counter()
    with DATA.open(encoding="utf-8", newline="") as handle:
        for row in csv.DictReader(handle):
            if row["verdict"] != "fully supports":
                failures[row["layer"]] += 1
    parts = [f"{layer} {failures[layer]}" for layer in sorted(failures)]
    print(f"{', '.join(parts)}, total {sum(failures.values())}")


if __name__ == "__main__":
    main()
