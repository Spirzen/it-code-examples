#!/bin/bash

BACKUP_DIR="/backup"
SOURCE_DIR="/home/user/data"
MIN_SPACE_MB=100

# Проверка существования директории резервных копий
if [ ! -d "$BACKUP_DIR" ]; then
    echo "Создание директории резервных копий..."
    mkdir -p "$BACKUP_DIR"
fi

# Проверка свободного места
free_space=$(df -m "$BACKUP_DIR" | awk 'NR==2 {print $4}')

if [ "$free_space" -lt "$MIN_SPACE_MB" ]; then
    echo "Ошибка: недостаточно места на диске. Доступно: ${free_space}MB, требуется: ${MIN_SPACE_MB}MB"
    exit 1
fi

echo "Начало резервного копирования..."

# Копирование файлов
for file in "$SOURCE_DIR"/*; do
    if [ -f "$file" ]; then
        filename=$(basename "$file")
        echo "Копирование: $filename"
        
        # Проверка успешности копирования
        if cp "$file" "$BACKUP_DIR/"; then
            echo "Успешно: $filename"
        else
            echo "Ошибка копирования: $filename"
            # Продолжаем копирование остальных файлов
            continue
        fi
    fi
done

echo "Резервное копирование завершено."
