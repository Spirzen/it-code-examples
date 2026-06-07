"""Модуль 7: список задач."""

TASKS = ("read", "parse", "render")


def list_tasks() -> str:
    return ", ".join(TASKS)
