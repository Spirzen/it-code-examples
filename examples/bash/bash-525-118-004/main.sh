format_date() {
    local timestamp="$1"
    local format="%Y-%m-%d %H:%M:%S"
    
    if [ -z "$timestamp" ]; then
        date +"$format"
        return 0
    fi
    
    date -d "@$timestamp" +"$format" 2>/dev/null
    return $?
}

current_time=$(format_date)
echo "Текущее время: $current_time"

past_time=$(format_date 1640995200)
echo "Прошлое время: $past_time"
