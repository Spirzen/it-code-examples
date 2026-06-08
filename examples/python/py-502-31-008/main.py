
import tarfile
import zipfile

from pathlib import Path

def pack_dir(folder: Path, archive: Path) -> None:
    with tarfile.open(archive, "w:gz") as tar:
        tar.add(folder, arcname=folder.name)

def split_file(path: Path, chunk_size: int = 50 * 1024 * 1024) -> None:
    data = path.read_bytes()
    for i in range(0, len(data), chunk_size):
        part = path.with_suffix(path.suffix + f".part{i // chunk_size:03d}")
        part.write_bytes(data[i : i + chunk_size])

def merge_parts(parts: list[Path], out: Path) -> None:
    with out.open("wb") as fout:
        for part in sorted(parts):
            fout.write(part.read_bytes())
