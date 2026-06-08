from pathlib import Path

def longest_txt_file(folder: str) -> tuple[Path | None, int]:
    best: Path | None = None
    best_lines = -1
    for path in Path(folder).glob("*.txt"):
        with path.open("r", encoding="utf-8") as f:
            count = sum(1 for _ in f)
        if count > best_lines:
            best_lines = count
            best = path
    return best, best_lines

winner, line_count = longest_txt_file(".")
if winner:
    print(winner, "— строк:", line_count)
