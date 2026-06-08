# OpenTelemetry — настройка трассировки
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.exporter.jaeger.thrift import JaegerExporter

# Инициализация провайдера
provider = TracerProvider()
trace.set_tracer_provider(provider)

# Настройка экспорта в Jaeger
jaeger_exporter = JaegerExporter(
    agent_host_name="localhost",
    agent_port=6831,
)
provider.add_span_processor(BatchSpanProcessor(jaeger_exporter))

# Создание трассировщика
tracer = trace.get_tracer(__name__)

# Трассировка операций
@tracer.start_as_current_span("process_order")
def process_order(order_id: str):
    with tracer.start_as_current_span("validate_order"):
        validate_order(order_id)
    
    with tracer.start_as_current_span("charge_payment"):
        charge_payment(order_id)
    
    with tracer.start_as_current_span("update_inventory"):
        update_inventory(order_id)
    
    with tracer.start_as_current_span("send_notification"):
        send_notification(order_id)
