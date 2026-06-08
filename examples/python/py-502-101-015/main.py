from dataclasses import dataclass
from typing import List

@dataclass(frozen=True)
class OrderItem:
    product_id: str
    quantity: int
    price: float

@dataclass(frozen=True)
class Order:
    id: str
    user_id: str
    items: List[OrderItem]
    status: str
    
    @property
    def total(self) -> float:
        return sum(item.quantity * item.price for item in self.items)
