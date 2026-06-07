"""Модуль 3: разбор аргументов (упрощённо)."""

import sys


def first_arg(default: str = "world") -> str:
    return sys.argv[1] if len(sys.argv) > 1 else default
