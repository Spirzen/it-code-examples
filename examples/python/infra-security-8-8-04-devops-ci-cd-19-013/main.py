from dataclasses import dataclass
from typing import List, Optional
from enum import Enum

class MetricCategory(Enum):
    BUSINESS = "business"
    APPLICATION = "application"
    INFRASTRUCTURE = "infrastructure"
    DEPENDENCY = "dependency"

@dataclass
class MetricDefinition:
    name: str
    category: MetricCategory
    description: str
    unit: str
    alert_threshold: Optional[float]
    dashboard_panel: str
    owner_team: str

# Реестр метрик системы
metric_registry: List[MetricDefinition] = [
    # Бизнес-метрики
    MetricDefinition(
        name="orders_created_total",
        category=MetricCategory.BUSINESS,
        description="Количество созданных заказов",
        unit="count",
        alert_threshold=None,
        dashboard_panel="business/orders",
        owner_team="product"
    ),
    MetricDefinition(
        name="payment_success_rate",
        category=MetricCategory.BUSINESS,
        description="Доля успешных платежей",
        unit="ratio",
        alert_threshold=0.95,
        dashboard_panel="business/payments",
        owner_team="payments"
    ),
    
    # Метрики приложения
    MetricDefinition(
        name="http_request_duration_seconds",
        category=MetricCategory.APPLICATION,
        description="Время обработки HTTP-запросов",
        unit="seconds",
        alert_threshold=2.0,
        dashboard_panel="app/latency",
        owner_team="platform"
    ),
    
    # Метрики зависимостей
    MetricDefinition(
        name="database_connection_pool_active",
        category=MetricCategory.DEPENDENCY,
        description="Активные соединения в пуле БД",
        unit="count",
        alert_threshold=80,
        dashboard_panel="deps/database",
        owner_team="data"
    ),
]
