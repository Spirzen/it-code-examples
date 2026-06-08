#!/bin/bash
set -euo pipefail

check_dependency() {
    local cmd="$1"
    if ! command -v "$cmd" &> /dev/null; then
        echo "Ошибка: необходим пакет '$cmd'" >&2
        exit 127
    fi
}

check_dependency "git"
check_dependency "python3"
check_dependency "docker"

echo "Все зависимости установлены"
