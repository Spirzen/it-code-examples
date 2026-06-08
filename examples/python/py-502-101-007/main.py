class ApplicationError(Exception):
    """Базовый класс для всех ошибок приложения"""
    pass

class ValidationError(ApplicationError):
    """Ошибка валидации входных данных"""
    def __init__(self, field, message):
        self.field = field
        self.message = message
        super().__init__(f"Validation error in field '{field}': {message}")

class PaymentError(ApplicationError):
    """Ошибка обработки платежа"""
    def __init__(self, transaction_id, reason):
        self.transaction_id = transaction_id
        self.reason = reason
        super().__init__(f"Payment failed for transaction {transaction_id}: {reason}")

class ResourceNotFoundError(ApplicationError):
    """Запрашиваемый ресурс не найден"""
    def __init__(self, resource_type, resource_id):
        self.resource_type = resource_type
        self.resource_id = resource_id
        super().__init__(f"{resource_type} with ID {resource_id} not found")
