from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Optional, List, Dict, Any

import httpx
import backoff

@dataclass
class ModelResponse:
    text: str
    tokens_used: int
    generation_time_ms: float
    model_version: str

class AIModelAdapter(ABC):
    @abstractmethod
    async def generate(self, prompt: str, **kwargs) -> ModelResponse:
        pass

class OpenAICompatibleAdapter(AIModelAdapter):
    def __init__(
        self,
        base_url: str,
        api_key: str,
        model_name: str,
        timeout: float = 30.0
    ):
        self.client = httpx.AsyncClient(
            base_url=base_url,
            headers={"Authorization": f"Bearer {api_key}"},
            timeout=timeout
        )
        self.model_name = model_name

    @backoff.on_exception(
        backoff.expo,
        (httpx.TimeoutException, httpx.HTTPStatusError),
        max_tries=3
    )
    async def generate(self, prompt: str, **kwargs) -> ModelResponse:
        payload = {
            "model": self.model_name,
            "messages": [{"role": "user", "content": prompt}],
            "max_tokens": kwargs.get("max_tokens", 512),
            "temperature": kwargs.get("temperature", 0.7),
            "stream": False
        }
        
        response = await self.client.post("/v1/chat/completions", json=payload)
        response.raise_for_status()
        data = response.json()
        
        choice = data["choices"][0]
        usage = data["usage"]
        
        return ModelResponse(
            text=choice["message"]["content"],
            tokens_used=usage["total_tokens"],
            generation_time_ms=response.elapsed.total_seconds() * 1000,
            model_version=data.get("model", self.model_name)
        )

    async def close(self):
        await self.client.aclose()
