from pydantic import (
    BaseSettings, 
    Field, 
    validator, 
    root_validator,
    ValidationError,
    SecretStr
)
from typing import List, Optional
from enum import Enum

import sys

class LogLevel(str, Enum):
    DEBUG = "debug"
    INFO = "info"
    WARNING = "warning"
    ERROR = "error"
    CRITICAL = "critical"

class Environment(str, Enum):
    DEVELOPMENT = "development"
    STAGING = "staging"
    PRODUCTION = "production"

class DatabaseSettings(BaseSettings):
    """Настройки подключения к базе данных."""
    
    host: str = Field(
        ...,
        description="Хост базы данных",
        min_length=1,
        max_length=255
    )
    port: int = Field(
        5432,
        description="Порт базы данных",
        ge=1,
        le=65535
    )
    name: str = Field(
        ...,
        description="Имя базы данных",
        regex=r'^[a-zA-Z_][a-zA-Z0-9_]{0,62}$'
    )
    username: str = Field(
        ...,
        description="Имя пользователя",
        min_length=1
    )
    password: SecretStr = Field(
        ...,
        description="Пароль (секрет)"
    )
    
    pool_size: int = Field(
        10,
        description="Размер пула соединений",
        ge=1,
        le=100
    )
    max_overflow: int = Field(
        10,
        description="Максимальное переполнение пула",
        ge=0,
        le=50
    )
    pool_timeout: int = Field(
        30,
        description="Таймаут ожидания соединения (секунды)",
        ge=1,
        le=300
    )
    
    @validator('host')
    def validate_host(cls, v):
        """Проверка формата хоста."""
        if v in ('localhost', '127.0.0.1'):
            # Разрешено только в development
            env = os.environ.get('ENVIRONMENT', 'development')
            if env == 'production':
                raise ValueError(
                    "Использование localhost запрещено в production"
                )
        return v
    
    class Config:
        env_prefix = "DB_"
        case_sensitive = False

class RedisSettings(BaseSettings):
    """Настройки Redis."""
    
    url: str = Field(
        ...,
        description="URL подключения к Redis"
    )
    ttl_default: int = Field(
        300,
        description="TTL по умолчанию (секунды)",
        ge=0,
        le=86400
    )
    ttl_max: int = Field(
        3600,
        description="Максимальный TTL (секунды)",
        ge=0,
        le=86400
    )
    max_connections: int = Field(
        20,
        description="Максимум соединений в пуле",
        ge=1,
        le=100
    )
    
    @validator('url')
    def validate_url(cls, v):
        if not v.startswith(('redis://', 'rediss://')):
            raise ValueError("URL должен начинаться с redis:// или rediss://")
        return v
    
    @root_validator
    def validate_ttl_range(cls, values):
        ttl_default = values.get('ttl_default')
        ttl_max = values.get('ttl_max')
        
        if ttl_default is not None and ttl_max is not None:
            if ttl_max < ttl_default:
                raise ValueError(
                    f"ttl_max ({ttl_max}) должен быть >= ttl_default ({ttl_default})"
                )
        
        return values
    
    class Config:
        env_prefix = "REDIS_"

class SecuritySettings(BaseSettings):
    """Настройки безопасности."""
    
    jwt_secret: SecretStr = Field(
        ...,
        description="Секрет для подписи JWT",
        min_length=32
    )
    jwt_algorithm: str = Field(
        "HS256",
        description="Алгоритм подписи JWT"
    )
    jwt_expiration: int = Field(
        3600,
        description="Время жизни JWT (секунды)",
        ge=60,
        le=86400
    )
    
    cors_origins: List[str] = Field(
        default_factory=list,
        description="Разрешённые источники CORS"
    )
    
    rate_limit_per_minute: int = Field(
        60,
        description="Лимит запросов в минуту",
        ge=1,
        le=10000
    )
    
    @validator('jwt_secret')
    def validate_jwt_secret_strength(cls, v):
        """Проверка криптостойкости секрета."""
        secret = v.get_secret_value()
        
        # Проверка энтропии
        unique_chars = len(set(secret))
        if unique_chars < 20:
            raise ValueError(
                "JWT-секрет должен содержать не менее 20 уникальных символов"
            )
        
        # Запрет известных слабых секретов
        weak_secrets = {
            "secret", "password", "123456", "qwerty",
            "jwt_secret", "my_secret_key"
        }
        if secret.lower() in weak_secrets:
            raise ValueError("Использование слабого секрета запрещено")
        
        return v
    
    @root_validator
    def validate_cors_for_production(cls, values):
        env = os.environ.get('ENVIRONMENT', 'development')
        cors_origins = values.get('cors_origins', [])
        
        if env == 'production':
            if '*' in cors_origins:
                raise ValueError(
                    "Wildcard '*' запрещён в production для CORS"
                )
            if not cors_origins:
                raise ValueError(
                    "CORS origins должны быть явно указаны в production"
                )
        
        return values
    
    class Config:
        env_prefix = "SECURITY_"

class AppConfig(BaseSettings):
    """Корневая конфигурация приложения."""
    
    environment: Environment = Field(
        Environment.DEVELOPMENT,
        description="Текущее окружение"
    )
    log_level: LogLevel = Field(
        LogLevel.INFO,
        description="Уровень логирования"
    )
    
    database: DatabaseSettings
    redis: RedisSettings
    security: SecuritySettings
    
    service_name: str = Field(
        "myapp",
        description="Имя сервиса"
    )
    service_version: str = Field(
        ...,
        description="Версия сервиса"
    )
    
    @root_validator
    def validate_environment_specific(cls, values):
        """Проверка правил, специфичных для окружения."""
        env = values.get('environment')
        log_level = values.get('log_level')
        
        # Production не должен использовать DEBUG-логирование
        if env == Environment.PRODUCTION and log_level == LogLevel.DEBUG:
            raise ValueError(
                "DEBUG-логирование запрещено в production окружении"
            )
        
        return values
    
    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'
        case_sensitive = False
        validate_all = True

def load_config() -> AppConfig:
    """Загрузка и валидация конфигурации."""
    try:
        config = AppConfig()
        print(f"✓ Конфигурация загружена для окружения: {config.environment.value}")
        print(f"✓ Версия сервиса: {config.service_version}")
        return config
    except ValidationError as e:
        print("=" * 60)
        print("ОШИБКИ ВАЛИДАЦИИ КОНФИГУРАЦИИ:")
        print("=" * 60)
        
        for error in e.errors():
            location = " -> ".join(str(loc) for loc in error['loc'])
            print(f"\n[{location}]")
            print(f"  Проблема: {error['msg']}")
            print(f"  Тип: {error['type']}")
        
        print("\n" + "=" * 60)
        print("Приложение не может быть запущено с некорректной конфигурацией")
        print("=" * 60)
        sys.exit(1)
