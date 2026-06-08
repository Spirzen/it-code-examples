#!/bin/bash
# validateconfig.sh — проверка целостности и конфигурации

ETALON_DIR="/opt/security/etalon"
REPORT="/var/log/security/audit_$(date +%F_%H%M).log"

log() { echo "[$(date +'%Y-%m-%d %H:%M:%S')] $1" | tee -a "$REPORT"; }

log "=== Запуск аудита конфигурации ==="

# 1. Проверка хешей критичных файлов
log "Проверка контрольных сумм..."
diff <(sha256sum /etc/passwd /etc/shadow /bin/ls) "$ETALON_DIR/file_hashes.sha256" || log "ВНИМАНИЕ: несоответствие хешей"

# 2. Проверка списка пользователей
log "Проверка учётных записей..."
diff <(getent passwd | cut -d: -f1 | sort) "$ETALON_DIR/users.list" || log "ВНИМАНИЕ: несанкционированные пользователи"

# 3. Проверка открытых портов
log "Проверка сетевых портов..."
CURRENT_PORTS=$(ss -tuln | awk 'NR>1 {print $5}' | sort -u)
diff <(echo "$CURRENT_PORTS") "$ETALON_DIR/ports.list" || log "ВНИМАНИЕ: неожиданные открытые порты"

# 4. Проверка установленных пакетов (белый список)
log "Проверка ПО..."
INSTALLED=$(dpkg-query -W -f='${Package}\n' | sort)
diff <(comm -13 "$ETALON_DIR/whitelist.txt" <(echo "$INSTALLED"))) /dev/null || \
  log "ВНИМАНИЕ: обнаружено ПО вне белого списка: $(comm -13 "$ETALON_DIR/whitelist.txt" <(echo "$INSTALLED"))"

log "=== Аудит завершён ==="
