#!/bin/bash

age=25

if [ "$age" -ge 18 ]; then
    echo "Пользователь совершеннолетний"
else
    echo "Пользователь несовершеннолетний"
fi

count=10
if [ "$count" -lt 20 ]; then
    echo "Счетчик меньше двадцати"
fi
