#!/bin/bash

SOURCE_DIR="/data/projects"
BACKUP_DIR="/backup/daily"
DATE=$(date +%Y-%m-%d)
LOG_FILE="/var/log/rsync_backup.log"

mkdir -p "$BACKUP_DIR"

rsync -avz --delete "$SOURCE_DIR/" "$BACKUP_DIR/${DATE}/" >> "$LOG_FILE" 2>&1

if [ $? -eq 0 ]; then
    echo "✅ Резервное копирование завершено успешно" >> "$LOG_FILE"
else
    echo "❌ Ошибка при резервном копировании" >> "$LOG_FILE"
fi
