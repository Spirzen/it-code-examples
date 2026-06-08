#!/bin/bash

usage() {
    echo "Использование: $0 <действие> [параметры]"
    echo "Действия: start, stop, status"
    exit 1
}

if [ $# -lt 1 ]; then
    usage
fi

action="$1"

case "$action" in
    start)
        echo "Запуск сервиса..."
        ;;
    stop)
        echo "Остановка сервиса..."
        ;;
    status)
        echo "Проверка статуса..."
        ;;
    *)
        echo "Неизвестное действие: $action"
        usage
        ;;
esac
