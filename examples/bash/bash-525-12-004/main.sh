#!/bin/bash
set -euo pipefail

if [ $# -eq 0 ]; then
    echo "Использование: $0 <файл>" >&2
    exit 2
fi

input_file="$1"

if [ ! -f "$input_file" ]; then
    echo "Ошибка: файл '$input_file' не найден" >&2
    exit 1
fi

echo "Обработка файла: $input_file"
# Дальнейшая логика
