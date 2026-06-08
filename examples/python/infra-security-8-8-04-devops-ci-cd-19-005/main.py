
import structlog

from datetime import datetime

# Настройка структурированного логгера
structlog.configure(
    processors=[
        structlog.contextvars.merge_contextvars,
        structlog.processors.add_log_level,
        structlog.processors.TimeStamper(fmt="iso"),
        structlog.processors.StackInfoRenderer(),
        structlog.processors.format_exc_info,
        structlog.processors.JSONRenderer()
    ],
    wrapper_class=structlog.make_filtering_bound_logger(logging.INFO),
    context_class=dict,
    logger_factory=structlog.PrintLoggerFactory()
)

logger = structlog.get_logger()

# Структурированный лог с контекстом
logger.info(
    "order_processed",
    order_id="ORD-12345",
    customer_id="CUST-67890",
    item_count=3,
    total_amount=1599.99,
    currency="RUB",
    duration_ms=245,
    payment_method="card",
    warehouse="MSK-01"
)
