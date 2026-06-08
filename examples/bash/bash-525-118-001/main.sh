check_file() {
    local file_path="$1"
    
    if [ -f "$file_path" ]; then
        echo "Файл существует."
        return 0
    else
        echo "Файл не найден."
        return 1
    fi
}

if check_file "/etc/passwd"; then
    echo "Процесс успешно завершен."
else
    echo "Процесс прерван из-за ошибки."
fi
