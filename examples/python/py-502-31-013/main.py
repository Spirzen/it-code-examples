
import hashlib
import json

from pathlib import Path

def build_manifest(folder: Path) -> dict:
    manifest = {}
    for f in folder.rglob("*"):
        if f.is_file():
            h = hashlib.sha256()
            h.update(f.read_bytes())
            manifest[str(f.relative_to(folder))] = h.hexdigest()
    return manifest

def verify_manifest(folder: Path, manifest_path: Path) -> list[str]:
    expected = json.loads(manifest_path.read_text(encoding="utf-8"))
    errors = []
    for rel, digest in expected.items():
        path = folder / rel
        if not path.exists():
            errors.append(f"нет файла: {rel}")
            continue
        if sha256_file(path) != digest:
            errors.append(f"хеш не совпадает: {rel}")
    return errors
