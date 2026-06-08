from abc import ABC, abstractmethod

class PaymentProcessor(ABC):
    @abstractmethod
    def authorize(self, amount: float) -> bool:
        pass
    
    @abstractmethod
    def capture(self, transaction_id: str) -> bool:
        pass
    
    def refund(self, transaction_id: str, amount: float) -> bool:
        """Неабстрактный метод с реализацией по умолчанию"""
        raise NotImplementedError("Возврат не поддерживается этим процессором")

class StripeProcessor(PaymentProcessor):
    def authorize(self, amount: float) -> bool:
        print(f"Авторизуем {amount} через Stripe")
        return True
    
    def capture(self, transaction_id: str) -> bool:
        print(f"Захватываем транзакцию {transaction_id}")
        return True

# processor = PaymentProcessor()  # TypeError — Can't instantiate abstract class
processor = StripeProcessor()
processor.authorize(100.0)
