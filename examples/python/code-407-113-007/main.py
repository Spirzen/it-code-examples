# Python (хороший пример)
from abc import ABC, abstractmethod

class Discount(ABC):
    @abstractmethod
    def apply(self, amount):
        pass

class SeasonalDiscount(Discount):
    def apply(self, amount):
        return amount * 0.9

class VipDiscount(Discount):
    def apply(self, amount):
        return amount * 0.8

class PromoDiscount(Discount):
    def apply(self, amount):
        return amount * 0.85

def calculate_total(items, discount: Discount):
    total = sum(item.price for item in items)
    return discount.apply(total)
