#!/bin/bash
# Функция для проверки статуса сервиса
check_service() {
    local service_name=$1
    if systemctl is-active --quiet "$service_name"; then
        echo "Сервис $service_name активен"
        return 0
    else
        echo "Сервис $service_name не активен"
        return 1
    fi
}

check_service "$@"
