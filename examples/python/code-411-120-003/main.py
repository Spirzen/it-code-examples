#!/usr/bin/env python3
"""Простой установщик: копирует payload/ в каталог приложения."""

from __future__ import annotations

import argparse
import platform
import shutil
import sys
from pathlib import Path

APP_NAME = "MyDemoApp"
VERSION = "1.0.0"


def default_install_dir() -> Path:
    system = platform.system()
    if system == "Windows":
        base = Path.home() / "AppData" / "Local" / "Programs"
    elif system == "Darwin":
        base = Path.home() / "Applications"
    else:
        base = Path.home() / ".local" / "share"
    return base / APP_NAME


def install(target: Path, payload: Path) -> None:
    if not payload.is_dir():
        raise FileNotFoundError(f"Нет папки payload: {payload}")
    if target.exists():
        shutil.rmtree(target)
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copytree(payload, target)
    print(f"{APP_NAME} {VERSION} установлен в {target}")


def main() -> int:
    parser = argparse.ArgumentParser(description=f"Установщик {APP_NAME}")
    parser.add_argument(
        "--dir",
        type=Path,
        default=default_install_dir(),
        help="Каталог установки",
    )
    args = parser.parse_args()
    script_dir = Path(__file__).resolve().parent
    payload = script_dir / "payload"
    try:
        install(args.dir.resolve(), payload)
    except OSError as exc:
        print(f"Ошибка: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
