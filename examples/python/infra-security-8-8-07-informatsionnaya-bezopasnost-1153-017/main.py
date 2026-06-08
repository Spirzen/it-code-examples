
import ldclient

from ldclient.config import Config
from ldclient import Context

class LaunchDarklyFeatureService:
    """Интеграция с LaunchDarkly."""
    
    def __init__(self, sdk_key: str):
        config = Config(sdk_key=sdk_key)
        ldclient.set_config(config)
        self.client = ldclient.get()
    
    def is_enabled(
        self, 
        flag_key: str, 
        user_id: str,
        attributes: dict = None
    ) -> bool:
        """Проверка флага через LaunchDarkly."""
        context = Context.builder(user_id)
        
        if attributes:
            for key, value in attributes.items():
                context.set(key, value)
        
        return self.client.variation(
            flag_key,
            context.build(),
            False  # значение по умолчанию
        )
    
    def get_variation(
        self,
        flag_key: str,
        user_id: str,
        default: str,
        attributes: dict = None
    ) -> str:
        """Получение варианта через LaunchDarkly."""
        context = Context.builder(user_id)
        
        if attributes:
            for key, value in attributes.items():
                context.set(key, value)
        
        return self.client.variation(
            flag_key,
            context.build(),
            default
        )
    
    def track(self, event_name: str, user_id: str, data: dict = None):
        """Отправка события для аналитики."""
        context = Context.builder(user_id).build()
        self.client.track(event_name, context, data)
    
    def shutdown(self):
        """Корректное завершение работы клиента."""
        self.client.close()
