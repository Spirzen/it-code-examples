"""Модуль 6: простой логгер."""


def log(message: str, *, debug: bool = False) -> None:
    prefix = "[debug] " if debug else ""
    print(f"{prefix}{message}")
