from fastapi import FastAPI, Depends, HTTPException, BackgroundTasks
from sqlalchemy.orm import Session
from typing import List
from database import get_db, Base, engine
from models import Order
from schemas import OrderCreate, OrderResponse

import json
import pika

app = FastAPI(title="Order Ingestion Service")

# Создание таблиц
Base.metadata.create_all(bind=engine)

# Конфигурация RabbitMQ
rabbit_url = "amqp://admin:secret_password@rabbitmq/"
connection = pika.BlockingConnection(pika.URLParameters(rabbit_url))
channel = connection.channel()
channel.queue_declare(queue='order_events', durable=True)

def send_order_event(order_id: int, event_type: str):
    message = json.dumps({
        "order_id": order_id,
        "event_type": event_type,
        "timestamp": datetime.utcnow().isoformat()
    })
    channel.basic_publish(
        exchange='',
        routing_key='order_events',
        body=message,
        properties=pika.BasicProperties(delivery_mode=2)
    )

@app.post("/orders", response_model=OrderResponse)
async def create_order(order: OrderCreate, background_tasks: BackgroundTasks, db: Session = Depends(get_db)):
    existing_order = db.query(Order).filter(Order.order_number == order.order_number).first()
    if existing_order:
        raise HTTPException(status_code=400, detail="Order number already exists")
    
    new_order = Order(
        order_number=order.order_number,
        amount=order.amount,
        status="pending"
    )
    db.add(new_order)
    db.commit()
    db.refresh(new_order)
    
    background_tasks.add_task(send_order_event, new_order.id, "order.created")
    
    return new_order

@app.get("/orders/{order_id}", response_model=OrderResponse)
async def get_order(order_id: int, db: Session = Depends(get_db)):
    order = db.query(Order).filter(Order.id == order_id).first()
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    return order
