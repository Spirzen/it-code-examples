
import shutil

from pathlib import Path

def incremental_backup(src: Path, dst: Path) -> list[Path]:
    dst.mkdir(parents=True, exist_ok=True)
    copied = []
    for f in src.rglob("*"):
        if not f.is_file():
            continue
        rel = f.relative_to(src)
        target = dst / rel
        target.parent.mkdir(parents=True, exist_ok=True)
        if not target.exists() or f.stat().st_mtime > target.stat().st_mtime:
            shutil.copy2(f, target)
            copied.append(rel)
    return copied
