
import random
import time

from typing import Callable, TypeVar

T = TypeVar('T')

def execute_with_backoff(
    operation: Callable[[], T],
    max_retries: int = 5,
    base_delay: float = 1.0,
    max_delay: float = 60.0
) -> T:
    """Выполнение операции с экспоненциальной задержкой и джиттером."""
    last_exception = None
    
    for attempt in range(max_retries + 1):
        try:
            return operation()
        except Exception as e:
            last_exception = e
            if attempt == max_retries:
                break
            
            # Экспоненциальный рост базовой задержки
            exponential_delay = base_delay * (2 ** attempt)
            
            # Ограничение максимальной задержки
            capped_delay = min(exponential_delay, max_delay)
            
            # Добавление случайного джиттера (±25%)
            jitter = capped_delay * random.uniform(-0.25, 0.25)
            actual_delay = capped_delay + jitter
            
            time.sleep(actual_delay)
    
    raise last_exception
