#!/bin/bash

TARGET="192.168.1.100"
TASK_NAME="Weekly Security Scan"

# Создание задачи
TASK_ID=$(omp -u admin -w password -X "<create_task><name>$TASK_NAME</name><config id='daba56c8-73ec-11df-a475-002264764cea'/><target id='target_id'/></create_task>" | grep task | cut -d' ' -f2 | cut -d'"' -f2)

# Запуск сканирования
omp -u admin -w password -X "<start_task task_id='$TASK_ID'/>"

# Ожидание завершения
while [ "$(omp -u admin -w password -X "<get_tasks task_id='$TASK_ID'/>" | grep progress | cut -d'>' -f2 | cut -d'<' -f1)" != "100" ]; do
    sleep 30
done

# Получение результатов
omp -u admin -w password -X "<get_reports report_id='$REPORT_ID'/>" > scan_results.xml
