# Python (хороший пример)
from abc import ABC, abstractmethod

class NotificationService(ABC):
    @abstractmethod
    def send(self, message):
        pass

class EmailNotificationService(NotificationService):
    def send(self, message):
        print(f"Sending email: {message}")

class SmsNotificationService(NotificationService):
    def send(self, message):
        print(f"Sending SMS: {message}")

class OrderService:
    def __init__(self, notifier: NotificationService):
        self.notifier = notifier  # Зависимость от абстракции

    def place_order(self, order):
        # Логика оформления заказа
        self.notifier.send("Order placed!")
