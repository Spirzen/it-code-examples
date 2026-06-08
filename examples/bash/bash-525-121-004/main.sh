#!/bin/bash

SEARCH_DIR="/home/user"
MIN_SIZE_MB=100

echo "Поиск файлов размером более ${MIN_SIZE_MB} МБ..."

fd -t f -g "*.*" "$SEARCH_DIR" | while read file; do
    size_mb=$(du -sm "$file" | cut -f1)
    
    if [ "$size_mb" -ge "$MIN_SIZE_MB" ]; then
        echo "📦 $file (${size_mb} MB)"
    fi
done
