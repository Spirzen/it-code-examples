safe_remove() {
    local file_path="$1"
    
    if [ -z "$file_path" ]; then
        echo "Ошибка: путь к файлу не указан."
        return 1
    fi
    
    if [ ! -e "$file_path" ]; then
        echo "Ошибка: файл не существует."
        return 1
    fi
    
    read -p "Удалить файл '$file_path'? (y/n): " confirm
    
    if [ "$confirm" = "y" ] || [ "$confirm" = "Y" ]; then
        rm -f "$file_path"
        echo "Файл удален."
        return 0
    else
        echo "Отмена удаления."
        return 1
    fi
}

safe_remove "/tmp/test.txt"
