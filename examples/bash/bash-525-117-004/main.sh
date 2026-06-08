#!/bin/bash

filename="report.pdf"

case "$filename" in
    *.pdf)
        echo "Это PDF документ"
        ;;
    *.txt|*.doc|*.docx)
        echo "Это текстовый документ"
        ;;
    *.sh)
        echo "Это скрипт"
        ;;
    *)
        echo "Неизвестный формат"
        ;;
esac
