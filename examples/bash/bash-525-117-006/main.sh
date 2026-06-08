#!/bin/bash

while true; do
    echo "Выберите действие:"
    echo "1. Добавить"
    echo "2. Удалить"
    echo "3. Выйти"
    read -p "Введите номер: " choice
    
    case $choice in
        1)
            echo "Добавление..."
            ;;
        2)
            echo "Удаление..."
            ;;
        3)
            echo "Выход"
            break
            ;;
        *)
            echo "Неверный выбор"
            ;;
    esac
done
