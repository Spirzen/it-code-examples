#!/bin/bash
set -euo pipefail
BACKUP_DIR="/backups/orion/$(date +%Y%m%d_%H%M)"
mkdir -p "$BACKUP_DIR"

tar -czf "$BACKUP_DIR/config.tar.gz" -C /opt/orion config/
cp /opt/orion/Данные/metadata.mv.db "$BACKUP_DIR/"

# Проверка целостности
tar -tzf "$BACKUP_DIR/config.tar.gz" >/dev/null && echo "✅ Config OK"
[ -f "$BACKUP_DIR/metadata.mv.db" ] && echo "✅ Metadata copied"

# Отправка в MinIO
mc cp "$BACKUP_DIR/" minio/backups/orion/
