#!/bin/bash

init_logging() {
    log_file="/var/log/myscript.log"
    exec 3>>"$log_file"
}

log_message() {
    local msg="$1"
    echo "$(date '+%Y-%m-%d %H:%M:%S') - $msg" >&3
}

cleanup() {
    exec 3>&-
}

trap cleanup EXIT

main() {
    init_logging
    log_message "Скрипт начал работу"
    
    # Основная логика
    log_message "Работа завершена"
}

main "$@"
