from pathlib import Path

import shutil

MAGIC = {
    b"\x89PNG\r\n\x1a\n": ".png",
    b"%PDF": ".pdf",
    b"PK\x03\x04": ".zip",
}

def detect_signature(path: Path) -> str:
    with path.open("rb") as f:
        head = f.read(8)
    for sig, label in MAGIC.items():
        if head.startswith(sig):
            return label
    return path.suffix or ".unknown"

def organize_by_extension(src: Path, dst_root: Path) -> None:
    for f in src.iterdir():
        if not f.is_file():
            continue
        bucket = dst_root / f.suffix.lower().lstrip(".") or "no_ext"
        bucket.mkdir(parents=True, exist_ok=True)
        shutil.move(str(f), bucket / f.name)

def sort_listing(folder: Path, key="mtime"):
    files = [p for p in folder.iterdir() if p.is_file()]
    if key == "mtime":
        return sorted(files, key=lambda p: p.stat().st_mtime, reverse=True)
    if key == "size":
        return sorted(files, key=lambda p: p.stat().st_size, reverse=True)
    if key == "signature":
        return sorted(files, key=lambda p: detect_signature(p))
    return sorted(files, key=lambda p: p.name.lower())
