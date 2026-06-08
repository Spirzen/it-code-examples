# tests/unit/test_payment_service.py

import pytest

from unittest.mock import Mock
from src.my_package.core.services import PaymentService
from src.my_package.core.repositories import PaymentRepository
from src.my_package.core.models import Payment, PaymentStatus

class TestPaymentService:
    @pytest.fixture
    def payment_repository(self):
        return Mock(spec=PaymentRepository)
    
    @pytest.fixture
    def payment_service(self, payment_repository):
        return PaymentService(payment_repository)
    
    def test_process_payment_success(self, payment_service, payment_repository):
        payment_repository.save.return_value = Payment(
            id="pay_123",
            amount=1000.0,
            currency="RUB",
            status=PaymentStatus.SUCCEEDED
        )
        
        result = payment_service.process_payment(
            amount=1000.0,
            currency="RUB",
            payment_method="card_4242"
        )
        
        assert result.status == PaymentStatus.SUCCEEDED
        payment_repository.save.assert_called_once()
    
    def test_process_payment_failure(self, payment_service, payment_repository):
        payment_repository.save.side_effect = PaymentError("Insufficient funds")
        
        with pytest.raises(PaymentError):
            payment_service.process_payment(
                amount=1000.0,
                currency="RUB",
                payment_method="card_declined"
            )
