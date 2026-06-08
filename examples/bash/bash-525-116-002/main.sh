#!/bin/bash

if [ $# -lt 2 ]; then
    echo "Использование: $0 <имя> <возраст>"
    exit 1
fi

name=$1
age=$2

if ! [[ "$age" =~ ^[0-9]+$ ]]; then
    echo "Ошибка: возраст должен быть числом"
    exit 1
fi

echo "Привет, $name! Тебе $age лет."
