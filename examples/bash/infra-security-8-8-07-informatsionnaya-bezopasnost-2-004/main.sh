#!/bin/bash
# remote_collect.sh — вызывается удалённо

HOST=$(hostname -s)
TIMESTAMP=$(date -u +%Y%m%dT%H%M%SZ)
OUT_DIR="/tmp/forensic_$HOST"
mkdir -p "$OUT_DIR"

# 1. Состояние процессов
ps auxfww > "$OUT_DIR/processes.txt"
cat /proc/*/cmdline 2>/dev/null | tr '\0' '\n' > "$OUT_DIR/cmdlines.txt"

# 2. Сеть
ss -tulnp > "$OUT_DIR/net_ss.txt"
cat /proc/net/tcp /proc/net/udp > "$OUT_DIR/net_raw.txt"

# 3. Пользователи
getent passwd > "$OUT_DIR/passwd.txt"
ls -la /home > "$OUT_DIR/home_dirs.txt"

# 4. Автозагрузка
systemctl list-unit-files --type=service --state=enabled > "$OUT_DIR/systemd_enabled.txt"
crontab -l -u root 2>/dev/null > "$OUT_DIR/crontab_root.txt"

# Архивация и шифрование (ключ предварительно развёрнут)
tar czf - "$OUT_DIR" | openssl enc -aes-256-cbc -pbkdf2 -k "$SECRET_KEY" | \
  nc -w 10 collector.example.com 8888
