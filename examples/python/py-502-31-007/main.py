
import csv

from pathlib import Path

def filter_csv(src: Path, dst: Path, min_age: int) -> None:
    with src.open(encoding="utf-8", newline="") as fin, dst.open(
        "w", encoding="utf-8", newline=""
    ) as fout:
        reader = csv.DictReader(fin)
        writer = csv.DictWriter(fout, fieldnames=reader.fieldnames)
        writer.writeheader()
        for row in reader:
            if int(row["age"]) >= min_age:
                writer.writerow(row)
