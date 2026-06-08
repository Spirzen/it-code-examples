#!/bin/bash
# simple_ids.sh

IOC_FILE="/opt/security/iocs.txt"  # список IP, хешей, сигнатур

# Сбор сетевых соединений каждые 10 сек
while true; do
  ss -tuln | awk 'NR>1 {print $5}' | cut -d: -f1 > /tmp/curr_ips.txt
  # Сравнение с IOC
  comm -12 <(sort /tmp/curr_ips.txt) <(sort "$IOC_FILE") | \
    while read ip; do
      logger -t IDS "ALERT: IOC match — $ip"
      iptables -A INPUT -s "$ip" -j DROP
      echo "Blocked $ip" | mail -s "БЕЗОПАСНОСТЬ BLOCK" admin@example.com
    done
  sleep 10
done
