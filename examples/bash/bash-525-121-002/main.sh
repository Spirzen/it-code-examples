#!/bin/bash

URL="https://example.com"
MAX_RETRIES=3
DELAY=5
LOG_FILE="/var/log/service_check.log"

for i in $(seq 1 $MAX_RETRIES); do
    STATUS_CODE=$(curl -s -o /dev/null -w "%{http_code}" --connect-timeout 5 "$URL")
    
    if [ "$STATUS_CODE" -eq 200 ]; then
        echo "$(date '+%Y-%m-%d %H:%M:%S') - Сервис доступен (HTTP $STATUS_CODE)" >> "$LOG_FILE"
        exit 0
    else
        echo "$(date '+%Y-%m-%d %H:%M:%S') - Попытка $i: Сервис недоступен (HTTP $STATUS_CODE)" >> "$LOG_FILE"
        sleep $DELAY
    fi
done

echo "$(date '+%Y-%m-%d %H:%M:%S') - Сервис недоступен после $MAX_RETRIES попыток" >> "$LOG_FILE"
exit 1
