"""Verdicts of contradicts or not in the text."""

import csv
from pathlib import Path

DATA = Path("10_markdown/data/review-findings-2026-08-10.csv")
HARD = {"contradicts", "not in the text"}


def main() -> None:
    with DATA.open(encoding="utf-8", newline="") as handle:
        count = sum(1 for row in csv.DictReader(handle) if row["verdict"] in HARD)
    print(str(count))


if __name__ == "__main__":
    main()
