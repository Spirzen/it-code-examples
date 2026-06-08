from dataclasses import dataclass, field
from typing import Optional

import os
import yaml
import argparse

@dataclass
class AppConfig:
    """Конфигурация приложения с иерархическим переопределением."""
    
    # Значения по умолчанию (низший приоритет)
    database_host: str = "localhost"
    database_port: int = 5432
    database_name: str = "myapp"
    database_pool_size: int = 10
    log_level: str = "info"
    request_timeout: int = 30
    cache_ttl: int = 300
    debug: bool = False
    
    @classmethod
    def load(cls) -> 'AppConfig':
        """Загрузка конфигурации с учётом иерархии источников."""
        config = cls()
        
        # Уровень 4: удалённое хранилище (Consul, etcd)
        remote_config = cls._load_from_remote()
        if remote_config:
            config._merge(remote_config)
        
        # Уровень 3: локальный конфигурационный файл
        file_config = cls._load_from_file()
        if file_config:
            config._merge(file_config)
        
        # Уровень 2: переменные окружения
        env_config = cls._load_from_environment()
        config._merge(env_config)
        
        # Уровень 1: аргументы командной строки
        cli_config = cls._load_from_cli()
        if cli_config:
            config._merge(cli_config)
        
        return config
    
    @classmethod
    def _load_from_file(cls) -> dict:
        config_path = os.environ.get("CONFIG_FILE", "config.yaml")
        if os.path.exists(config_path):
            with open(config_path) as f:
                return yaml.safe_load(f) or {}
        return {}
    
    @classmethod
    def _load_from_environment(cls) -> dict:
        """Загрузка всех параметров из переменных окружения."""
        prefix = "MYAPP_"
        config = {}
        
        for key, value in os.environ.items():
            if key.startswith(prefix):
                param_name = key[len(prefix):].lower()
                config[param_name] = cls._cast_value(param_name, value)
        
        return config
    
    @classmethod
    def _load_from_cli(cls) -> dict:
        parser = argparse.ArgumentParser()
        parser.add_argument("--database-host")
        parser.add_argument("--database-port", type=int)
        parser.add_argument("--log-level")
        parser.add_argument("--debug", action="store_true")
        
        args, _ = parser.parse_known_args()
        return {k: v for k, v in vars(args).items() if v is not None}
    
    @classmethod
    def _load_from_remote(cls) -> dict:
        """Загрузка из удалённого хранилища конфигураций."""
        # Интеграция с Consul, etcd или аналогичным сервисом
        pass
    
    def _merge(self, overrides: dict):
        """Применение переопределений с приведением типов."""
        for key, value in overrides.items():
            if hasattr(self, key):
                current_value = getattr(self, key)
                setattr(self, key, type(current_value)(value))
    
    @classmethod
    def _cast_value(cls, name: str, value: str):
        """Приведение строкового значения к нужному типу."""
        type_mapping = {
            "database_port": int,
            "database_pool_size": int,
            "request_timeout": int,
            "cache_ttl": int,
            "debug": lambda v: v.lower() in ("true", "1", "yes"),
        }
        
        caster = type_mapping.get(name, str)
        return caster(value)
