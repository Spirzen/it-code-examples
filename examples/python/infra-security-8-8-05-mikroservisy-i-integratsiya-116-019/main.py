
import faust

from datetime import datetime

app = faust.App(
    'order-processing',
    broker='kafka://localhost:9092',
    store='memory://',
    version=1
)

class OrderEvent(faust.Record, serializer='json'):
    type: str
    order_id: str
    customer_id: str
    items: list
    timestamp: str

orders_topic = app.topic('orders', value_type=OrderEvent)

# Таблица для агрегации по клиентам
customer_orders = app.Table(
    'customer_orders',
    default=int
)

@app.agent(orders_topic)
async def process_orders(stream):
    async for event in stream:
        if event.type == 'OrderCreated':
            print(f"Обработка заказа {event.order_id}")
            
            # Инкремент счётчика заказов клиента
            customer_orders[event.customer_id] += 1
            
            # Логика обработки...
            await process_order(event)

async def process_order(event):
    # Бизнес-логика
    pass

# Периодическая задача для отчётов
@app.timer(interval=60.0)
async def report_stats():
    total = sum(customer_orders.values())
    print(f"Статистика: всего заказов = {total}")
    for customer, count in customer_orders.items():
        print(f"  Клиент {customer}: {count} заказов")

if __name__ == '__main__':
    app.main()
