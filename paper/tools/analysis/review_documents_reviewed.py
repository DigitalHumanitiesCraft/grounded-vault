"""Documents covered by the first review pass, per layer."""

import csv
from collections import Counter
from pathlib import Path

DATA = Path("10_markdown/data/review-runs-2026-08-10.csv")


def main() -> None:
    documents: Counter[str] = Counter()
    with DATA.open(encoding="utf-8", newline="") as handle:
        for row in csv.DictReader(handle):
            documents[row["layer"]] += 1
    parts = [f"{layer} {documents[layer]}" for layer in sorted(documents)]
    print(f"{', '.join(parts)}, total {sum(documents.values())}")


if __name__ == "__main__":
    main()
