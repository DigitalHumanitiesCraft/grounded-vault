"""Pairs reviewed in the first pass, per layer."""

import csv
from collections import Counter
from pathlib import Path

DATA = Path("10_markdown/data/review-runs-2026-08-10.csv")


def main() -> None:
    totals: Counter[str] = Counter()
    with DATA.open(encoding="utf-8", newline="") as handle:
        for row in csv.DictReader(handle):
            totals[row["layer"]] += int(row["pairs_reviewed"])
    parts = [f"{layer} {totals[layer]}" for layer in sorted(totals)]
    print(f"{', '.join(parts)}, total {sum(totals.values())}")


if __name__ == "__main__":
    main()
