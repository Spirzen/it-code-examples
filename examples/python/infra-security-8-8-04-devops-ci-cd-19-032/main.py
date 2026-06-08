
import asyncio
import requests

from datetime import datetime, timedelta

class ObservabilityIntegrationTest:
    """Сквозное тестирование наблюдаемости."""
    
    def __init__(self, app_url, prometheus_url, loki_url, tempo_url):
        self.app_url = app_url
        self.prometheus_url = prometheus_url
        self.loki_url = loki_url
        self.tempo_url = tempo_url
    
    async def run_full_test(self):
        """Полный тест всех трёх столпов наблюдаемости."""
        test_id = f"obs-test-{datetime.utcnow().isoformat()}"
        
        # Генерация тестового трафика с уникальным идентификатором
        await self._generate_test_traffic(test_id)
        
        # Ожидание обработки данных
        await asyncio.sleep(30)
        
        results = {
            "metrics": await self._verify_metrics(test_id),
            "logs": await self._verify_logs(test_id),
            "traces": await self._verify_traces(test_id),
        }
        
        overall_pass = all(r["passed"] for r in results.values())
        
        return {
            "test_id": test_id,
            "timestamp": datetime.utcnow().isoformat(),
            "overall_pass": overall_pass,
            "results": results
        }
    
    async def _generate_test_traffic(self, test_id: str):
        """Генерация запросов с тестовым идентификатором."""
        headers = {"X-Test-Id": test_id}
        
        # Успешный запрос
        requests.get(f"{self.app_url}/api/health", headers=headers)
        
        # Запрос с ошибкой
        requests.get(f"{self.app_url}/api/nonexistent", headers=headers)
        
        # Медленный запрос
        requests.get(
            f"{self.app_url}/api/slow-operation",
            headers=headers,
            timeout=10
        )
    
    async def _verify_metrics(self, test_id: str) -> dict:
        """Проверка наличия метрик от тестового трафика."""
        query = f'http_requests_total{{test_id="{test_id}"}}'
        response = requests.get(
            f"{self.prometheus_url}/api/v1/query",
            params={"query": query}
        )
        data = response.json()
        
        has_data = len(data.get("data", {}).get("result", [])) > 0
        
        return {
            "passed": has_data,
            "details": "Метрики обнаружены" if has_data else "Метрики отсутствуют"
        }
    
    async def _verify_logs(self, test_id: str) -> dict:
        """Проверка наличия логов с тестовым идентификатором."""
        query = f'{{app="myapp"}} |= "{test_id}"'
        end = datetime.utcnow()
        start = end - timedelta(minutes=5)
        
        response = requests.get(
            f"{self.loki_url}/loki/api/v1/query_range",
            params={
                "query": query,
                "start": start.timestamp(),
                "end": end.timestamp(),
                "limit": 10
            }
        )
        data = response.json()
        
        log_count = sum(
            len(stream["values"])
            for stream in data.get("data", {}).get("result", [])
        )
        
        return {
            "passed": log_count > 0,
            "details": f"Обнаружено {log_count} лог-записей"
        }
    
    async def _verify_traces(self, test_id: str) -> dict:
        """Проверка наличия трассировок с тестовым идентификатором."""
        response = requests.get(
            f"{self.tempo_url}/api/search",
            params={
                "tags": f"test.id={test_id}",
                "limit": 10
            }
        )
        data = response.json()
        
        trace_count = len(data.get("traces", []))
        
        return {
            "passed": trace_count > 0,
            "details": f"Обнаружено {trace_count} трассировок"
        }
