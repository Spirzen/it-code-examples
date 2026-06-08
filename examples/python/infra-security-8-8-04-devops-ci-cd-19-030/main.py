from dataclasses import dataclass
from typing import List, Set

import requests

@dataclass
class ComponentCoverage:
    component_name: str
    component_type: str  # "service", "database", "queue", "cache"
    has_metrics: bool
    has_logs: bool
    has_traces: bool
    has_alerts: bool
    missing_capabilities: List[str]

def audit_observability_coverage(
    prometheus_url: str,
    service_registry: List[dict]
) -> List[ComponentCoverage]:
    """Аудит покрытия наблюдаемостью всех компонентов."""
    
    # Получение списка активных метрик
    response = requests.get(f"{prometheus_url}/api/v1/label/__name__/values")
    available_metrics: Set[str] = set(response.json()["data"])
    
    results = []
    
    for service in service_registry:
        name = service["name"]
        service_type = service["type"]
        
        # Проверка наличия стандартных метрик
        expected_metrics = [
            f"{name}_requests_total",
            f"{name}_errors_total",
            f"{name}_duration_seconds",
            f"{name}_up",
        ]
        
        found_metrics = [m for m in expected_metrics if m in available_metrics]
        has_metrics = len(found_metrics) >= len(expected_metrics) * 0.75
        
        # Проверка алертов
        alerts_response = requests.get(f"{prometheus_url}/api/v1/rules")
        rules = alerts_response.json()["data"]["groups"]
        has_alerts = any(
            name in str(rule) 
            for group in rules 
            for rule in group["rules"]
        )
        
        missing = []
        if not has_metrics:
            missing.append("метрики")
        if not has_alerts:
            missing.append("алерты")
        
        results.append(ComponentCoverage(
            component_name=name,
            component_type=service_type,
            has_metrics=has_metrics,
            has_logs=True,  # Предполагается наличие централизованных логов
            has_traces=False,  # Требует отдельной проверки
            has_alerts=has_alerts,
            missing_capabilities=missing
        ))
    
    return results
