check_disk_space() {
    local usage=$(df -h / | tail -1 | awk '{print $5}' | tr -d '%')
    
    if [ "$usage" -gt 90 ]; then
        echo "Критический уровень заполнения диска: ${usage}%"
        return 2
    elif [ "$usage" -gt 80 ]; then
        echo "Предупреждение: заполнено ${usage}%"
        return 1
    else
        echo "Диск в норме: ${usage}%"
        return 0
    fi
}

check_disk_space
status=$?
if [ $status -eq 2 ]; then
    echo "Требуется срочное вмешательство!"
elif [ $status -eq 1 ]; then
    echo "Нужно запланировать очистку"
fi
