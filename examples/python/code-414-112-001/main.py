from functools import lru_cache
from cachetools import TTLCache

# LRU-кэш с ограничением на 1000 элементов
@lru_cache(maxsize=1000)
def compute_expensive_result(payload):
    return heavy_computation(payload)

# Кэш с ограничением по времени жизни (300 секунд)
_request_cache = TTLCache(maxsize=10000, ttl=300)

def process_request(request_id, payload):
    if request_id not in _request_cache:
        _request_cache[request_id] = compute_expensive_result(payload)
    return _request_cache[request_id]
