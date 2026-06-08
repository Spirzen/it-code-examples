# core/app_kernel.py
class SuperAppKernel:
    """Центральное ядро супераппа"""
    
    def __init__(self):
        self.auth_service = AuthService()
        self.payment_gateway = PaymentGateway()
        self.profile_manager = ProfileManager()
        self.module_registry = ModuleRegistry()
    
    def bootstrap(self):
        """Инициализация базовых сервисов при старте приложения"""
        self.auth_service.initialize()
        self.payment_gateway.connect()
        self.profile_manager.load_user_profile()
    
    def launch_module(self, module_name: str, context: dict):
        """Запуск мини-приложения с передачей контекста"""
        module = self.module_registry.get(module_name)
        if module:
            return module.execute(context, self._build_module_context())
        raise ModuleNotFoundError(f"Модуль {module_name} не зарегистрирован")
    
    def _build_module_context(self) -> dict:
        """Формирование безопасного контекста для модуля"""
        return {
            "user_id": self.auth_service.current_user_id,
            "auth_token": self.auth_service.get_short_lived_token(),
            "payment_methods": self.payment_gateway.list_available_methods(),
            "permissions": self.auth_service.get_user_permissions()
        }
