
import os

from typing import Dict, Optional

class SafeConfigManager:
    """Менеджер безопасной конфигурации"""
    
    def __init__(self):
        self._secrets_patterns = [
            'password', 'secret', 'key', 'token', 
            'credential', 'api_key', 'auth'
        ]
    
    def is_sensitive(self, key: str) -> bool:
        """Проверка на чувствительность переменной"""
        key_lower = key.lower()
        return any(pattern in key_lower for pattern in self._secrets_patterns)
    
    def get_masked_value(self, value: str, visible_chars: int = 4) -> str:
        """Маскировка секретного значения"""
        if len(value) <= visible_chars:
            return '*' * len(value)
        return value[:visible_chars] + '*' * (len(value) - visible_chars)
    
    def get_env_safe_dict(self) -> Dict[str, str]:
        """Получение словаря без чувствительных данных"""
        safe_dict = {}
        for key, value in os.environ.items():
            if not self.is_sensitive(key):
                safe_dict[key] = value
            else:
                safe_dict[key] = self.get_masked_value(value, 4)
        return safe_dict
    
    def get_structure_only(self) -> list:
        """Получение только имён переменных без значений"""
        return list(os.environ.keys())

# Пример использования
config = SafeConfigManager()
masked_config = config.get_env_safe_dict()
structure = config.get_structure_only()
print(masked_config)
print(structure)
