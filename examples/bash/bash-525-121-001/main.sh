#!/bin/bash

CPU_THRESHOLD=80
MEM_THRESHOLD=90
LOG_FILE="/var/log/system_monitor.log"

check_load() {
    local cpu_usage=$(top -bn1 | grep "Cpu(s)" | awk '{print $2}' | cut -d'%' -f1)
    local mem_usage=$(free | awk '/Mem:/ {printf "%.0f", $3/$2 * 100}')
    
    echo "$(date '+%Y-%m-%d %H:%M:%S') - CPU: ${cpu_usage}%, Memory: ${mem_usage}%" >> "$LOG_FILE"
    
    if (( $(echo "$cpu_usage > $CPU_THRESHOLD" | bc -l) )); then
        echo "⚠️ Предупреждение: Загрузка процессора выше ${CPU_THRESHOLD}%" >> "$LOG_FILE"
    fi
    
    if (( $(echo "$mem_usage > $MEM_THRESHOLD" | bc -l) )); then
        echo "⚠️ Предупреждение: Использование памяти выше ${MEM_THRESHOLD}%" >> "$LOG_FILE"
    fi
}

while true; do
    check_load
    sleep 60
done
