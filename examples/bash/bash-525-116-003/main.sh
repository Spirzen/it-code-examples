#!/bin/bash

read -p "Как вас зовут? " user_name
read -p "Сколько вам лет? " user_age
read -s -p "Введите ваш секретный код: " secret_code
echo ""

if [ -z "$secret_code" ]; then
    echo "Секретный код не введен."
    exit 1
fi

echo "Данные получены:"
echo "Имя: $user_name"
echo "Возраст: $user_age"
echo "Код получен."
