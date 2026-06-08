
import re

from collections import Counter
from pathlib import Path

def aggregate_log(path: Path) -> Counter:
    pattern = re.compile(r"\b(ERROR|WARNING|INFO)\b")
    counts: Counter = Counter()
    for line in path.read_text(encoding="utf-8", errors="replace").splitlines():
        m = pattern.search(line)
        if m:
            counts[m.group(1)] += 1
    return counts
