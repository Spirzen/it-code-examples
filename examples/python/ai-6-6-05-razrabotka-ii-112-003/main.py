
import pybreaker

class ResilientModelClient:
    def __init__(self, base_url: str, api_key: str):
        self.breaker = pybreaker.CircuitBreaker(
            fail_max=5,
            reset_timeout=60000  # 60 секунд
        )
        self.adapter = OpenAICompatibleAdapter(base_url, api_key, "my-model")

    @pybreaker.CircuitBreakerError
    def _call_model(self, prompt: str) -> ModelResponse:
        return await self.adapter.generate(prompt)

    async def generate_with_fallback(self, prompt: str) -> ModelResponse:
        try:
            return await self._call_model(prompt)
        except pybreaker.CircuitBreakerError:
            # Переключение на резервную модель меньшего размера
            fallback = OpenAICompatibleAdapter(
                base_url="https://backup.example.com",
                api_key="backup-key",
                model_name="my-model-small"
            )
            return await fallback.generate(prompt)
