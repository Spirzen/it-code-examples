#!/bin/bash

SERVICE_NAME="nginx"
MAX_RESTARTS=3
restart_count=0

while true; do
    if pgrep -x "$SERVICE_NAME" > /dev/null; then
        echo "$(date): Сервис $SERVICE_NAME работает"
        restart_count=0
    else
        echo "$(date): Сервис $SERVICE_NAME не работает. Перезапуск..."
        systemctl start "$SERVICE_NAME"
        restart_count=$((restart_count + 1))
        
        if [ "$restart_count" -ge "$MAX_RESTARTS" ]; then
            echo "$(date): Достигнуто максимальное количество попыток перезапуска ($MAX_RESTARTS)"
            exit 1
        fi
    fi
    
    sleep 60
done
