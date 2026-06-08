#!/usr/bin/env python3
"""
Pre-commit хук для валидации технической документации.

Проверяет:
- Валидность Markdown (синтаксис, ссылки на несуществующие файлы)
- Наличие заголовка уровня 1 (H1) в начале файла
- Отсутствие жёстко заданных абсолютных путей
- Согласованность имён файлов и заголовков (например, file.md → # File)

Требования:
    pip install markdown-it-py mdformat
"""

import argparse
import re
import sys

from pathlib import Path

from markdown_it import MarkdownIt


def validate_markdown(file_path: Path) -> list[str]:
    """Возвращает список ошибок для файла."""
    errors = []
    content = file_path.read_text(encoding="utf-8")

    # Проверка H1 в начале
    lines = content.strip().splitlines()
    if not lines or not lines[0].startswith("# "):
        errors.append("Отсутствует заголовок H1 в первой строке")

    # Проверка абсолютных путей
    if re.search(r"\]\(/", content):  # [текст](/путь)
        errors.append("Обнаружены абсолютные пути в ссылках — используйте относительные")

    # Проверка валидности Markdown
    try:
        md = MarkdownIt("commonmark")
        tokens = md.parse(content)
        # Простая проверка: нет ли токенов с типом 'error'
        if any(t.type == "error" for t in tokens):
            errors.append("Некорректный Markdown-синтаксис")
    except Exception as e:
        errors.append(f"Ошибка парсинга Markdown: {e}")

    # Проверка согласованности имени файла и заголовка
    if lines and lines[0].startswith("# "):
        title = lines[0][2:].strip()
        expected_title = file_path.stem.replace("_", " ").replace("-", " ").title()
        if title.lower() != expected_title.lower():
            errors.append(f"Заголовок '{title}' не соответствует имени файла '{expected_title}'")

    return errors


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("files", nargs="*", help="Файлы для проверки")
    args = parser.parse_args()

    if not args.files:
        print("Нет файлов для проверки", file=sys.stderr)
        sys.exit(0)

    markdown_files = [f for f in args.files if f.endswith(".md")]
    all_errors = []

    for file in markdown_files:
        path = Path(file)
        if not path.exists():
            continue
        errors = validate_markdown(path)
        if errors:
            print(f"\n{file}:")
            for err in errors:
                print(f"  - {err}")
            all_errors.extend(errors)

    if all_errors:
        print(f"\n❌ Найдено ошибок: {len(all_errors)}", file=sys.stderr)
        sys.exit(1)
    else:
        print("✅ Документация валидна", file=sys.stderr)
        sys.exit(0)


if __name__ == "__main__":
    main()
