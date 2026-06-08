# Плохо: фабрика стратегий для единственного способа оплаты
class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount): ...

class CardPayment(PaymentStrategy):
    def pay(self, amount):
        charge_card(amount)

class PaymentFactory:
    @staticmethod
    def create(kind: str) -> PaymentStrategy:
        if kind == "card":
            return CardPayment()
        raise ValueError(kind)

# Вызов: PaymentFactory.create("card").pay(100)
