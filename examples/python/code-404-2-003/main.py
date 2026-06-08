# logger/logger.py

import sys

from datetime import datetime

def info(msg: str):
    ts = datetime.now().isoformat()
    print(f"[INFO] {ts} {msg}", file=sys.stderr)

# notification/email.py
from logger.logger import info  # ← прямой импорт модуля

def send_email(to: str, subject: str, body: str):
    info(f"Sending email to {to}")
    # ... SMTP logic

# core/order.py
from dataclasses import dataclass
from logger.logger import info

@dataclass
class Order:
    id: int
    items: list[str]

class OrderService:
    def place_order(self, items: list[str]) -> Order:
        order = Order(id=1, items=items)
        info(f"Order {order.id} placed with {len(items)} items")
        return order

# app/main.py
from core.order import OrderService
from notification.email import send_email

if __name__ == "__main__":
    service = OrderService()
    order = service.place_order(["book", "pen"])
    send_email("user@example.com", "Order confirmed", f"ID: {order.id}")
