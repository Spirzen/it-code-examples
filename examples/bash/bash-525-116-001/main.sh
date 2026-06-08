#!/bin/bash

# Определение конфигурационных переменных
APP_NAME="MyApp"
VERSION="1.0.0"
LOG_DIR="/var/log/myapp"
DEBUG_MODE=false

# Проверка режима отладки
if [ "$DEBUG_MODE" = true ]; then
    echo "Запуск в режиме отладки..."
    export LOG_LEVEL="debug"
else
    export LOG_LEVEL="info"
fi

echo "Приложение: $APP_NAME версии $VERSION"
echo "Логирование: $LOG_LEVEL"
echo "Директория логов: $LOG_DIR"
