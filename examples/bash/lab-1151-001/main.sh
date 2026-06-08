#!/usr/bin/env bash
set -euo pipefail

target="${1:?укажите путь: $0 <путь>}"

if [[ -d "$target" ]]; then
  count=$(find "$target" -type f | wc -l)
  echo "Каталог. Файлов внутри: $count"
elif [[ -f "$target" ]]; then
  bytes=$(wc -c < "$target")
  echo "Файл. Размер: $bytes байт"
else
  echo "Не найдено: $target" >&2
  exit 1
fi
