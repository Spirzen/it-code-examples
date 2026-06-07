"""Модуль 4: пути и файлы."""

from pathlib import Path


def project_root() -> Path:
    return Path(__file__).resolve().parent
