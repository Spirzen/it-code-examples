#!/bin/bash

user_input=""

if [ -z "$user_input" ]; then
    echo "Вы ничего не ввели"
else
    echo "Вы ввели: $user_input"
fi

name="Timur"
if [ "$name" = "Timur" ]; then
    echo "Имя совпадает"
fi
