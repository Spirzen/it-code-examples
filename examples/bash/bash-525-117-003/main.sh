#!/bin/bash

day="monday"

case "$day" in
    monday)
        echo "Начало недели"
        ;;
    tuesday)
        echo "Вторник"
        ;;
    wednesday)
        echo "Среда"
        ;;
    *)
        echo "Остальные дни"
        ;;
esac
