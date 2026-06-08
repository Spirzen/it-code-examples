# Безопасный способ загрузки переменных окружения

import os

from dotenv import load_dotenv

# Загрузка из .env файла только локально
load_dotenv()

# А в продакшене — только системные переменные
db_host = os.getenv('DB_HOST')
db_port = os.getenv('DB_PORT', '5432')
db_user = os.getenv('DB_USER')
db_password = os.getenv('DB_PASSWORD')
