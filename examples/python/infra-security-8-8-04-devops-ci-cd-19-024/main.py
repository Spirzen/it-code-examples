# Проблема — потеря trace_id в фоновой задаче
from celery import Celery

app = Celery('tasks')

@app.route("/orders")
async def create_order(request: Request):
    trace_id = request.headers.get("X-Trace-Id")
    order = await process_order(request.json())
    
    # Фоновая задача теряет trace_id
    send_confirmation_email.delay(order.id)
    
    return {"order_id": order.id}

@app.task
def send_confirmation_email(order_id: int):
    # trace_id недоступен - задача не связана с исходным запросом
    order = get_order(order_id)
    email_service.send(order.customer_email, "Подтверждение заказа", ...)
