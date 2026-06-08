# core/request_router.py
class RequestRouter:
    """Маршрутизатор запросов между компонентами супераппа"""
    
    def __init__(self):
        self.handlers = {
            'payment.process': PaymentHandler(),
            'delivery.order': DeliveryHandler(),
            'profile.update': ProfileHandler(),
            'notification.send': NotificationHandler()
        }
    
    def route(self, operation: str, payload: dict, context: RequestContext) -> OperationResult:
        """Маршрутизация запроса к соответствующему обработчику"""
        if operation not in self.handlers:
            raise UnknownOperationException(f"Операция {operation} не поддерживается")
        
        # Проверка прав доступа перед передачей запроса
        if not self._validate_permissions(operation, context.user_permissions):
            raise PermissionDeniedError(f"Недостаточно прав для операции {operation}")
        
        # Логирование запроса для аудита
        self._log_operation(operation, context.user_id, payload.get('transaction_id'))
        
        # Передача запроса обработчику с контекстом безопасности
        handler = self.handlers[operation]
        return handler.process(payload, self._build_secure_context(context))
    
    def _validate_permissions(self, operation: str, user_permissions: list) -> bool:
        required_permissions = {
            'payment.process': ['payments.write'],
            'delivery.order': ['delivery.write'],
            'profile.update': ['profile.write'],
            'notification.send': ['notifications.write']
        }
        required = required_permissions.get(operation, [])
        return all(perm in user_permissions for perm in required)
    
    def _build_secure_context(self, context: RequestContext) -> dict:
        """Формирование контекста с минимально необходимыми правами"""
        return {
            'user_id': context.user_id,
            'session_id': context.session_id,
            'request_timestamp': context.timestamp,
            'device_fingerprint': context.device_fingerprint_hashed
        }
