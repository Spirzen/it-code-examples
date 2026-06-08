# Python (плохой пример)
class EmailNotificationService:
    def send(self, message):
        # Реализация отправки через SMTP
        print(f"Sending email via SMTP: {message}")

class OrderService:
    def __init__(self):
        self.notifier = EmailNotificationService()  # Жёсткая зависимость

    def place_order(self, order):
        # Логика оформления заказа
        self.notifier.send("Order placed!")
