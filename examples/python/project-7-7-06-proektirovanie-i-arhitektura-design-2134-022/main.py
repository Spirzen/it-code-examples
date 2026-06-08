from pydantic import BaseSettings, validator
from typing import Optional

class AppConfig(BaseSettings):
    # Обязательные параметры
    database_url: str
    redis_url: str
    secret_key: str
    
    # Опциональные с значениями по умолчанию
    log_level: str = "info"
    max_connections: int = 100
    request_timeout: int = 30
    
    # Валидация значений
    @validator('log_level')
    def validate_log_level(cls, v):
        allowed = {"debug", "info", "warning", "error", "critical"}
        if v.lower() not in allowed:
            raise ValueError(f"Допустимые уровни: {allowed}")
        return v.lower()
    
    @validator('max_connections')
    def validate_max_connections(cls, v):
        if v < 1 or v > 1000:
            raise ValueError("Должно быть в диапазоне 1-1000")
        return v
    
    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'
        case_sensitive = False

# Проверка при старте приложения
def load_config() -> AppConfig:
    try:
        return AppConfig()
    except Exception as e:
        print(f"Ошибка конфигурации: {e}")
        sys.exit(1)
