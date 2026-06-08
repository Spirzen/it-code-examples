#!/bin/bash
# ssh_bruteforce_pipeline.sh

LOG="/var/log/auth.log"
TEMP="/tmp/ssh_analysis"
ALERTS="/var/log/security/alerts.log"
BLOCKLIST="/etc/ssh/blocklist.conf"

# 1. Сбор и фильтрация
grep "Failed password" "$LOG" > "$TEMP/raw.txt"

# 2. Нормализация (извлечение IP и временных меток)
awk '{
  gsub(/\[|\]/, "", $3);
  split($3, dt, ":");
  time = mktime("2025 11 " dt[1] " " dt[2] " " dt[3] " " dt[4]);
  print time, $11
}' "$TEMP/raw.txt" > "$TEMP/normalized.txt"

# 3. Агрегация по 5-минутным окнам
awk '{
  window = int($1 / 300);
  ip_count[$2, window]++;
}
END {
  for (key in ip_count) {
    split(key, a, SUBSEP);
    ip = a[1]; win = a[2];
    if (ip_count[key] >= 10) {
      print win, ip, ip_count[key] > "/tmp/alert_candidates.txt"
    }
  }
}' "$TEMP/normalized.txt"

# 4. Корреляция — исключение доверенных IP
comm -23 <(sort /tmp/alert_candidates.txt | cut -f2) <(sort /etc/security/trusted_ips.txt) > /tmp/malicious_ips.txt

# 5. Оповещение и реагирование
while read ip; do
  if ! grep -q "$ip" "$BLOCKLIST"; then
    echo "deny from $ip" >> "$BLOCKLIST"
    systemctl reload sshd  # или iptables -A INPUT -s $ip -j DROP
    logger -t SSH_SECURITY "Blocked $ip for bruteforce"
    echo "$(date -Isec) | SSH_BRUTEFORCE | $ip" >> "$ALERTS"
    echo "SSH brute-force from $ip" | mail -s "БЕЗОПАСНОСТЬ ALERT" soc@example.com
  fi
done < /tmp/malicious_ips.txt
