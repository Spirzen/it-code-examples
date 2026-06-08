
import consul
import threading
import time

from typing import Dict, Any, Callable, Optional

class ConsulConfigWatcher:
    """Наблюдатель за изменениями конфигурации в Consul."""
    
    def __init__(
        self, 
        host: str = "localhost",
        port: int = 8500,
        prefix: str = "myapp/config/"
    ):
        self.client = consul.Consul(host=host, port=port)
        self.prefix = prefix
        self.config: Dict[str, Any] = {}
        self.watchers: Dict[str, list] = {}
        self._running = False
        self._watch_thread: Optional[threading.Thread] = None
    
    def start(self):
        """Запуск наблюдения за конфигурацией."""
        self._running = True
        self._load_initial_config()
        
        self._watch_thread = threading.Thread(
            target=self._watch_loop,
            daemon=True
        )
        self._watch_thread.start()
    
    def stop(self):
        """Остановка наблюдения."""
        self._running = False
        if self._watch_thread:
            self._watch_thread.join(timeout=5)
    
    def get(self, key: str, default: Any = None) -> Any:
        """Получение значения параметра."""
        return self.config.get(key, default)
    
    def watch(
        self, 
        key: str, 
        callback: Callable[[str, Any, Any], None]
    ):
        """Регистрация наблюдателя за изменением параметра."""
        if key not in self.watchers:
            self.watchers[key] = []
        self.watchers[key].append(callback)
    
    def _load_initial_config(self):
        """Загрузка начальной конфигурации."""
        index, data = self.client.kv.get(
            self.prefix, 
            recurse=True
        )
        
        if data:
            for item in data:
                key = item['Key'][len(self.prefix):]
                value = item['Value'].decode('utf-8') if item['Value'] else None
                self.config[key] = self._parse_value(value)
    
    def _watch_loop(self):
        """Цикл наблюдения за изменениями."""
        index = None
        
        while self._running:
            try:
                index, data = self.client.kv.get(
                    self.prefix,
                    recurse=True,
                    index=index,
                    wait='5m'
                )
                
                if data:
                    self._process_updates(data)
                    
            except Exception as e:
                print(f"Ошибка наблюдения Consul: {e}")
                time.sleep(5)
    
    def _process_updates(self, data: list):
        """Обработка обновлений конфигурации."""
        new_config = {}
        
        for item in data:
            key = item['Key'][len(self.prefix):]
            value = item['Value'].decode('utf-8') if item['Value'] else None
            new_config[key] = self._parse_value(value)
        
        # Обнаружение изменений
        for key, new_value in new_config.items():
            old_value = self.config.get(key)
            
            if old_value != new_value:
                self._notify_watchers(key, old_value, new_value)
        
        # Обнаружение удалений
        for key in set(self.config.keys()) - set(new_config.keys()):
            old_value = self.config[key]
            self._notify_watchers(key, old_value, None)
        
        self.config = new_config
    
    def _notify_watchers(
        self, 
        key: str, 
        old_value: Any, 
        new_value: Any
    ):
        """Уведомление наблюдателей об изменении."""
        if key in self.watchers:
            for callback in self.watchers[key]:
                try:
                    callback(key, old_value, new_value)
                except Exception as e:
                    print(f"Ошибка в наблюдателе {key}: {e}")
    
    def _parse_value(self, value: str) -> Any:
        """Парсинг строкового значения в Python-объект."""
        if value is None:
            return None
        
        # Попытка парсинга как JSON
        try:
            import json
            return json.loads(value)
        except (json.JSONDecodeError, TypeError):
            pass
        
        # Булевы значения
        if value.lower() in ('true', 'yes', '1'):
            return True
        if value.lower() in ('false', 'no', '0'):
            return False
        
        # Числовые значения
        try:
            if '.' in value:
                return float(value)
            return int(value)
        except ValueError:
            pass
        
        return value
