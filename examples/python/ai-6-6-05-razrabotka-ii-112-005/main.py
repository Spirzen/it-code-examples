
import hashlib

from typing import Optional

class CachedModelClient:
    def __init__(self, adapter: AIModelAdapter, redis_client: aioredis.Redis):
        self.adapter = adapter
        self.redis = redis_client
        self.cache_ttl = 86400  # 24 часа

    def _prompt_hash(self, prompt: str, params: Dict[str, Any]) -> str:
        # Сериализация параметров для воспроизводимости хэша
        param_str = "|".join(f"{k}={v}" for k, v in sorted(params.items()))
        combined = f"{prompt}|{param_str}"
        return hashlib.sha256(combined.encode()).hexdigest()

    async def generate(self, prompt: str, **kwargs) -> ModelResponse:
        cache_key = f"model:cache:{self._prompt_hash(prompt, kwargs)}"
        cached = await self.redis.get(cache_key)
        
        if cached:
            return ModelResponse.parse_raw(cached)
        
        response = await self.adapter.generate(prompt, **kwargs)
        await self.redis.setex(cache_key, self.cache_ttl, response.json())
        return response
