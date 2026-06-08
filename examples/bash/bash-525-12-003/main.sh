#!/bin/bash
set -euo pipefail

cleanup_files() {
    local files=(file1.txt file2.txt file3.txt)
    
    for file in "${files[@]}"; do
        if [ -f "$file" ]; then
            echo "Удаление $file..."
            rm -f "$file" || {
                echo "Не удалось удалить $file" >&2
                continue
            }
        fi
    done
}

cleanup_files
echo "Очистка завершена"
