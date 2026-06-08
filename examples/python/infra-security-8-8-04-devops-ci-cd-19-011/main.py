from prometheus_client import Counter, Histogram, Gauge

# Полноценный набор метрик для внешней зависимости
payment_requests_total = Counter(
    "payment_requests_total",
    "Общее количество запросов к платёжному шлюзу",
    ["gateway", "operation", "status"]
)

payment_duration_seconds = Histogram(
    "payment_duration_seconds",
    "Время выполнения операций платёжного шлюза",
    ["gateway", "operation"],
    buckets=[0.1, 0.25, 0.5, 1.0, 2.5, 5.0, 10.0, 30.0]
)

payment_circuit_state = Gauge(
    "payment_circuit_state",
    "Состояние circuit breaker для платёжного шлюза",
    ["gateway"]
)

payment_retry_total = Counter(
    "payment_retry_total",
    "Количество повторных попыток обращения к шлюзу",
    ["gateway", "reason"]
)

payment_fallback_total = Counter(
    "payment_fallback_total",
    "Количество переключений на резервный шлюз",
    ["primary_gateway", "fallback_gateway"]
)
