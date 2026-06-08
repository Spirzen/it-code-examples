copy_files() {
    local source_dir="$1"
    local dest_dir="$2"
    
    if [ -z "$source_dir" ] || [ -z "$dest_dir" ]; then
        echo "Ошибка: необходимы оба аргумента."
        return 1
    fi
    
    if [ ! -d "$source_dir" ]; then
        echo "Ошибка: источник не является директорией."
        return 1
    fi
    
    mkdir -p "$dest_dir"
    if [ $? -ne 0 ]; then
        echo "Ошибка: невозможно создать целевую директорию."
        return 1
    fi
    
    cp -r "$source_dir"/* "$dest_dir"/
    if [ $? -ne 0 ]; then
        echo "Ошибка: копирование файлов завершилось неудачей."
        return 1
    fi
    
    echo "Копирование завершено успешно."
    return 0
}
