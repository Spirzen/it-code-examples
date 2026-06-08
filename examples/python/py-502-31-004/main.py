from pathlib import Path

def patch_file(path: Path, needle: str, replacement: str) -> None:
    raw = path.read_bytes()
    try:
        text = raw.decode("utf-8")
    except UnicodeDecodeError:
        text = raw.decode("utf-8-sig")

    if needle not in text:
        raise ValueError(f"Подстрока не найдена: {needle!r}")

    updated = text.replace(needle, replacement)
    normalized = updated.replace("\r\n", "\n").replace("\r", "\n")
    path.write_bytes(normalized.encode("utf-8"))
