
import logging
import re

from typing import Set

class SecretFilter(logging.Filter):
    """Фильтр для предотвращения утечки секретов в логах."""
    
    # Паттерны для обнаружения секретов
    SECRET_PATTERNS = [
        # API-ключи
        re.compile(r'(?:api[_-]?key|apikey)["\s:=]+["\']?([a-zA-Z0-9]{32,})["\']?'),
        
        # Токены
        re.compile(r'(?:token|secret|password|passwd|pwd)["\s:=]+["\']?([^\s"\']{8,})["\']?'),
        
        # JWT
        re.compile(r'eyJ[a-zA-Z0-9_-]+\.eyJ[a-zA-Z0-9_-]+\.[a-zA-Z0-9_-]+'),
        
        # AWS ключи
        re.compile(r'AKIA[0-9A-Z]{16}'),
        
        # Приватные ключи
        re.compile(r'-----BEGIN [A-Z ]+ PRIVATE KEY-----'),
        
        # Строки подключения
        re.compile(r'(?:postgresql|mysql|redis|mongodb)://[^:]+:([^@]+)@'),
    ]
    
    # Имена полей, содержащих секреты
    SECRET_FIELD_NAMES: Set[str] = {
        'password', 'passwd', 'pwd', 'secret', 'token',
        'api_key', 'apikey', 'access_key', 'private_key',
        'auth', 'credentials', 'session_id', 'jwt',
        'database_url', 'connection_string'
    }
    
    def filter(self, record: logging.LogRecord) -> bool:
        """Фильтрация записи лога."""
        # Очистка сообщения
        if hasattr(record, 'msg') and isinstance(record.msg, str):
            record.msg = self._redact_secrets(record.msg)
        
        # Очистка аргументов
        if hasattr(record, 'args'):
            record.args = self._redact_args(record.args)
        
        return True
    
    def _redact_secrets(self, text: str) -> str:
        """Замена секретов в тексте на маскированные значения."""
        result = text
        
        for pattern in self.SECRET_PATTERNS:
            result = pattern.sub(
                lambda m: m.group(0)[:20] + '***REDACTED***',
                result
            )
        
        return result
    
    def _redact_args(self, args):
        """Очистка аргументов лог-записи."""
        if isinstance(args, dict):
            return {
                k: '***REDACTED***' if self._is_secret_field(k) else v
                for k, v in args.items()
            }
        elif isinstance(args, tuple):
            return tuple(
                '***REDACTED***' if self._might_be_secret(str(arg)) else arg
                for arg in args
            )
        return args
    
    def _is_secret_field(self, field_name: str) -> bool:
        """Проверка, является ли поле секретным."""
        field_lower = field_name.lower()
        return any(
            secret in field_lower 
            for secret in self.SECRET_FIELD_NAMES
        )
    
    def _might_be_secret(self, value: str) -> bool:
        """Эвристическая проверка значения на секретность."""
        if not isinstance(value, str):
            return False
        
        # Длинные случайные строки
        if len(value) > 32 and len(set(value)) > 20:
            return True
        
        # Соответствие паттернам
        return any(
            pattern.search(value) 
            for pattern in self.SECRET_PATTERNS
        )

# Применение фильтра
logger = logging.getLogger('myapp')
logger.addFilter(SecretFilter())
