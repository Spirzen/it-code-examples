from pydantic import BaseSettings, validator, Field
from typing import List, Optional

import sys

class DatabaseConfig(BaseSettings):
    url: str = Field(..., env="DATABASE_URL")
    pool_size: int = Field(20, env="DB_POOL_SIZE")
    max_overflow: int = Field(10, env="DB_MAX_OVERFLOW")
    pool_timeout: int = Field(30, env="DB_POOL_TIMEOUT")
    
    @validator("url")
    def validate_url(cls, v):
        if not v.startswith(("postgresql://", "postgresql+asyncpg://")):
            raise ValueError("Поддерживается только PostgreSQL")
        return v
    
    @validator("pool_size")
    def validate_pool_size(cls, v):
        if v < 1 or v > 500:
            raise ValueError("pool_size должен быть в диапазоне 1-500")
        return v

class CacheConfig(BaseSettings):
    url: str = Field(..., env="REDIS_URL")
    ttl_default: int = Field(300, env="CACHE_TTL_DEFAULT")
    ttl_max: int = Field(3600, env="CACHE_TTL_MAX")
    
    @validator("ttl_max")
    def validate_ttl_max(cls, v, values):
        default_ttl = values.get("ttl_default", 0)
        if v < default_ttl:
            raise ValueError("ttl_max должен быть >= ttl_default")
        return v

class AppConfig(BaseSettings):
    environment: str = Field(..., env="ENVIRONMENT")
    log_level: str = Field("info", env="LOG_LEVEL")
    database: DatabaseConfig
    cache: CacheConfig
    
    @validator("environment")
    def validate_environment(cls, v):
        allowed = {"development", "staging", "production"}
        if v not in allowed:
            raise ValueError(f"Допустимые окружения: {allowed}")
        return v
    
    @validator("log_level")
    def validate_log_level(cls, v, values):
        env = values.get("environment")
        if env == "production" and v.lower() in {"debug", "trace"}:
            raise ValueError("DEBUG/TRACE запрещены в production")
        return v

def load_and_validate_config() -> AppConfig:
    """Загрузка и валидация конфигурации при старте."""
    try:
        config = AppConfig()
        print(f"Конфигурация загружена для окружения: {config.environment}")
        return config
    except Exception as e:
        print(f"КРИТИЧЕСКАЯ ОШИБКА КОНФИГУРАЦИИ: {e}")
        sys.exit(1)
