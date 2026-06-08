from opentelemetry import trace, context
from opentelemetry.trace.propagation import get_current_span
from celery import Celery

app = Celery('tasks')

@app.route("/orders")
async def create_order(request: Request):
    # Получение текущего span и его контекста
    current_span = get_current_span()
    trace_id = format_trace_id(current_span.get_span_context().trace_id)
    span_id = format_span_id(current_span.get_span_context().span_id)
    
    order = await process_order(request.json())
    
    # Передача контекста трассировки в фоновую задачу
    send_confirmation_email.apply_async(
        args=[order.id],
        headers={
            "trace_id": trace_id,
            "span_id": span_id,
            "traceparent": f"00-{trace_id}-{span_id}-01"
        }
    )
    
    return {"order_id": order.id}

@app.task(bind=True)
def send_confirmation_email(self, order_id: int):
    # Восстановление контекста трассировки
    traceparent = self.request.headers.get("traceparent")
    
    if traceparent:
        ctx = TraceContextTextMapPropagator().extract(
            carrier={"traceparent": traceparent}
        )
        context.attach(ctx)
    
    # Создание дочернего span
    with tracer.start_as_current_span(
        "send_confirmation_email",
        attributes={
            "order.id": order_id,
            "task.id": self.request.id
        }
    ) as span:
        order = get_order(order_id)
        email_service.send(order.customer_email, "Подтверждение заказа", ...)
        span.set_attribute("email.sent", True)
