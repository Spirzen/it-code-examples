#!/usr/bin/env python3
"""Модуль 10: точка входа, собирает практикум."""

from step01_greeting import greeting
from step02_version import version_line
from step03_args import first_arg
from step07_tasks import list_tasks
from step09_report import report


def main() -> None:
    who = first_arg("Вселенная IT")
    print(greeting())
    print(version_line())
    print(report(who, list_tasks()))


if __name__ == "__main__":
    main()
