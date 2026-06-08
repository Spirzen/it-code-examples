# Антипаттерн — конфигурация в коде
DATABASE_URL = "postgresql://admin:secret_password@prod-db.internal:5432/myapp"
API_KEY = "sk_live_4eC39HqLyjWDarjtT1zdp7dc"
DEBUG_MODE = False

def get_connection():
    return psycopg2.connect(DATABASE_URL)

# Правильный паттерн — конфигурация из окружения

import os

from urllib.parse import urlparse

def get_database_url() -> str:
    """Получение URL базы данных из переменной окружения."""
    url = os.environ.get("DATABASE_URL")
    if not url:
        raise RuntimeError("Переменная DATABASE_URL не установлена")
    return url

def get_api_key(service: str) -> str:
    """Получение API-ключа сервиса из окружения."""
    key = os.environ.get(f"{service.upper()}_API_KEY")
    if not key:
        raise RuntimeError(f"API-ключ для {service} не настроен")
    return key

def is_debug_mode() -> bool:
    """Проверка режима отладки."""
    return os.environ.get("DEBUG", "false").lower() == "true"
