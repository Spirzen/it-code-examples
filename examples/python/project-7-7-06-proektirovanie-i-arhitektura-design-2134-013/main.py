from dataclasses import dataclass
from typing import List, Optional

import jsonschema

PAYMENT_RESPONSE_SCHEMA = {
    "type": "object",
    "required": ["transaction_id", "status"],
    "properties": {
        "transaction_id": {"type": "string", "pattern": "^[a-zA-Z0-9-]{36}$"},
        "status": {"type": "string", "enum": ["success", "pending", "failed"]},
        "amount": {"type": "number", "minimum": 0},
        "currency": {"type": "string", "pattern": "^[A-Z]{3}$"}
    }
}

@dataclass
class PaymentResponse:
    transaction_id: str
    status: str
    amount: float
    currency: str
    
    @classmethod
    def from_dict(cls, data: dict) -> 'PaymentResponse':
        # Валидация схемы
        jsonschema.validate(data, PAYMENT_RESPONSE_SCHEMA)
        
        return cls(
            transaction_id=data['transaction_id'],
            status=data['status'],
            amount=data.get('amount', 0.0),
            currency=data.get('currency', 'USD')
        )
