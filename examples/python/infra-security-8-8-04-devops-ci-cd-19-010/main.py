from collections import defaultdict
from datetime import datetime, timedelta

import threading

class LogAggregator:
    """Агрегатор повторяющихся лог-событий."""
    
    def __init__(self, logger, window_seconds: int = 60):
        self.logger = logger
        self.window = timedelta(seconds=window_seconds)
        self.counters = defaultdict(int)
        self.first_seen = {}
        self.lock = threading.Lock()
        self._start_flusher()
    
    def log(self, event_key: str, level: str = "INFO", **context):
        """Регистрация события с агрегацией."""
        with self.lock:
            now = datetime.utcnow()
            
            if event_key not in self.first_seen:
                self.first_seen[event_key] = now
            
            self.counters[event_key] += 1
            self._last_context[event_key] = context
    
    def _flush(self):
        """Периодическая запись агрегированных событий."""
        with self.lock:
            for event_key, count in self.counters.items():
                if count == 1:
                    # Единичное событие логируется как есть
                    self.logger.info(event_key, **self._last_context[event_key])
                else:
                    # Множественные события агрегируются
                    self.logger.info(
                        f"{event_key}_aggregated",
                        event=event_key,
                        count=count,
                        window_seconds=self.window.total_seconds(),
                        rate_per_second=count / self.window.total_seconds(),
                        last_context=self._last_context[event_key]
                    )
            
            self.counters.clear()
            self.first_seen.clear()
