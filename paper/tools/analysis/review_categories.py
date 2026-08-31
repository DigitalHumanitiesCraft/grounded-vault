"""Recorded defect categories, most frequent first."""

import csv
from collections import Counter
from pathlib import Path

DATA = Path("10_markdown/data/review-findings-2026-08-10.csv")


def main() -> None:
    categories: Counter[str] = Counter()
    with DATA.open(encoding="utf-8", newline="") as handle:
        for row in csv.DictReader(handle):
            if row["category"]:
                categories[row["category"]] += 1
    parts = [f"{name} {count}" for name, count in categories.most_common()]
    print(", ".join(parts))


if __name__ == "__main__":
    main()
