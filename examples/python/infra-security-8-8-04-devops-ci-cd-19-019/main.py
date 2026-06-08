
import asyncio

from dataclasses import dataclass
from typing import Dict, Optional
from enum import Enum

class ComponentStatus(Enum):
    HEALTHY = "healthy"
    DEGRADED = "degraded"
    UNHEALTHY = "unhealthy"

@dataclass
class ComponentHealth:
    status: ComponentStatus
    latency_ms: float
    details: Optional[str] = None

class HealthChecker:
    """Комплексная система проверки здоровья с таймаутами."""
    
    def __init__(self, db_pool, cache_client, queue_client, external_apis):
        self.db_pool = db_pool
        self.cache_client = cache_client
        self.queue_client = queue_client
        self.external_apis = external_apis
    
    async def check_component(self, name: str, coro, timeout: float = 2.0):
        """Проверка одного компонента с таймаутом."""
        start = asyncio.get_event_loop().time()
        try:
            result = await asyncio.wait_for(coro, timeout=timeout)
            elapsed = (asyncio.get_event_loop().time() - start) * 1000
            return ComponentHealth(
                status=ComponentStatus.HEALTHY,
                latency_ms=elapsed,
                details=str(result)
            )
        except asyncio.TimeoutError:
            elapsed = (asyncio.get_event_loop().time() - start) * 1000
            return ComponentHealth(
                status=ComponentStatus.UNHEALTHY,
                latency_ms=elapsed,
                details=f"Таймаут {timeout}с"
            )
        except Exception as e:
            elapsed = (asyncio.get_event_loop().time() - start) * 1000
            return ComponentHealth(
                status=ComponentStatus.UNHEALTHY,
                latency_ms=elapsed,
                details=str(e)
            )
    
    async def _check_database(self):
        async with self.db_pool.acquire() as conn:
            return await conn.fetchval("SELECT 1")
    
    async def _check_cache(self):
        return await self.cache_client.ping()
    
    async def _check_queue(self):
        return await self.queue_client.ping()
    
    async def full_check(self) -> Dict[str, ComponentHealth]:
        """Параллельная проверка всех компонентов."""
        checks = {
            "database": self.check_component("database", self._check_database(), 3.0),
            "cache": self.check_component("cache", self._check_cache(), 1.0),
            "queue": self.check_component("queue", self._check_queue(), 2.0),
        }
        
        results = {}
        for name, coro in checks.items():
            results[name] = await coro
        
        return results

@app.get("/health/ready")
async def readiness(checker: HealthChecker):
    """Проверка готовности к приёму трафика."""
    results = await checker.full_check()
    
    # Критические зависимости должны быть полностью здоровы
    critical_components = ["database"]
    critical_healthy = all(
        results[c].status == ComponentStatus.HEALTHY
        for c in critical_components
    )
    
    # Второстепенные могут быть деградированы
    overall_healthy = critical_healthy and all(
        r.status != ComponentStatus.UNHEALTHY
        for r in results.values()
    )
    
    status_code = 200 if overall_healthy else 503
    
    return JSONResponse(
        status_code=status_code,
        content={
            "status": "healthy" if overall_healthy else "unhealthy",
            "components": {
                name: {
                    "status": h.status.value,
                    "latency_ms": round(h.latency_ms, 2),
                    "details": h.details
                }
                for name, h in results.items()
            }
        }
    )
