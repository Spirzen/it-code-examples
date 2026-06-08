from fastapi import FastAPI, HTTPException, Response
from fastapi.responses import JSONResponse

app = FastAPI()

class HealthChecker:
    def __init__(self, db_pool, cache_client, queue_client):
        self.db_pool = db_pool
        self.cache_client = cache_client
        self.queue_client = queue_client
    
    async def check_database(self):
        """Проверка соединения с базой данных."""
        try:
            async with self.db_pool.acquire() as conn:
                await conn.fetchval("SELECT 1")
            return {"status": "healthy", "latency_ms": 0}
        except Exception as e:
            return {"status": "unhealthy", "error": str(e)}
    
    async def check_cache(self):
        """Проверка доступности кэша."""
        try:
            await self.cache_client.ping()
            return {"status": "healthy"}
        except Exception as e:
            return {"status": "degraded", "error": str(e)}
    
    async def check_queue(self):
        """Проверка брокера сообщений."""
        try:
            await self.queue_client.ping()
            return {"status": "healthy"}
        except Exception as e:
            return {"status": "degraded", "error": str(e)}
    
    async def full_check(self):
        """Комплексная проверка всех зависимостей."""
        checks = {
            "database": await self.check_database(),
            "cache": await self.check_cache(),
            "queue": await self.check_queue()
        }
        
        all_healthy = all(c["status"] == "healthy" for c in checks.values())
        
        return {
            "status": "healthy" if all_healthy else "degraded",
            "components": checks,
            "timestamp": datetime.utcnow().isoformat()
        }

@app.get("/health/live")
async def liveness():
    """Базовая проверка: приложение отвечает."""
    return {"status": "alive"}

@app.get("/health/ready")
async def readiness(checker: HealthChecker):
    """Глубокая проверка готовности."""
    result = await checker.full_check()
    
    if result["status"] == "unhealthy":
        raise HTTPException(status_code=503, detail=result)
    
    return JSONResponse(
        content=result,
        status_code=200 if result["status"] == "healthy" else 207
    )
