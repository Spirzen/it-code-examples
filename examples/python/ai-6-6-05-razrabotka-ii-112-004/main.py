
import asyncio
import aioredis

from pydantic import BaseModel

class InferenceRequest(BaseModel):
    request_id: str
    prompt: str
    user_id: str
    priority: int = 5  # 1-10

class AsyncInferenceQueue:
    def __init__(self, redis_url: str):
        self.redis = aioredis.from_url(redis_url)
        self.queue_key = "model:inference:queue"

    async def enqueue(self, request: InferenceRequest):
        payload = request.json()
        # Приоритет через sorted set: score = priority
        await self.redis.zadd(self.queue_key, {payload: request.priority})

    async def worker(self, model_adapter: AIModelAdapter):
        while True:
            # Извлечение задачи с наивысшим приоритетом (минимальный score)
            task = await self.redis.zpopmin(self.queue_key)
            if task:
                request = InferenceRequest.parse_raw(task[0][0])
                try:
                    response = await model_adapter.generate(request.prompt)
                    await self._publish_result(request.request_id, response)
                except Exception as e:
                    await self._publish_error(request.request_id, str(e))
            await asyncio.sleep(0.01)  # Предотвращение busy-wait

    async def _publish_result(self, request_id: str, response: ModelResponse):
        await self.redis.setex(
            f"result:{request_id}",
            3600,  # TTL 1 час
            response.json()
        )
