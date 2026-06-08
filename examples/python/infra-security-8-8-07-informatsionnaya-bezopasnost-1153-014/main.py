from dataclasses import dataclass
from typing import Any, Dict, Optional, Callable
from enum import Enum

import hashlib

class FlagType(Enum):
    BOOLEAN = "boolean"
    VARIANT = "variant"
    PERCENTAGE = "percentage"

@dataclass
class FeatureFlag:
    """Определение флага функциональности."""
    name: str
    flag_type: FlagType
    default_value: Any
    description: str
    owner: str
    created_at: str
    variants: Optional[Dict[str, Any]] = None
    targeting_rules: Optional[list] = None

class FeatureFlagService:
    """Сервис управления флагами функциональности."""
    
    def __init__(self, config_source):
        self.config_source = config_source
        self.flags: Dict[str, FeatureFlag] = {}
        self._load_flags()
    
    def _load_flags(self):
        """Загрузка определений флагов из источника конфигурации."""
        raw_flags = self.config_source.get_all_flags()
        for flag_data in raw_flags:
            flag = FeatureFlag(
                name=flag_data['name'],
                flag_type=FlagType(flag_data['type']),
                default_value=flag_data['default'],
                description=flag_data['description'],
                owner=flag_data['owner'],
                created_at=flag_data['created_at'],
                variants=flag_data.get('variants'),
                targeting_rules=flag_data.get('targeting_rules'),
            )
            self.flags[flag.name] = flag
    
    def is_enabled(self, flag_name: str, context: Dict[str, Any] = None) -> bool:
        """Проверка включённости булевого флага."""
        flag = self.flags.get(flag_name)
        if not flag:
            return False
        
        if flag.flag_type != FlagType.BOOLEAN:
            raise ValueError(f"Флаг {flag_name} не является булевым")
        
        # Проверка targeting-правил
        if flag.targeting_rules and context:
            for rule in flag.targeting_rules:
                if self._evaluate_rule(rule, context):
                    return rule['value']
        
        return flag.default_value
    
    def get_variant(
        self, 
        flag_name: str, 
        context: Dict[str, Any] = None
    ) -> Any:
        """Получение варианта для мульти-вариантного флага."""
        flag = self.flags.get(flag_name)
        if not flag:
            return None
        
        if flag.flag_type != FlagType.VARIANT:
            raise ValueError(f"Флаг {flag_name} не является мульти-вариантным")
        
        # Детерминированный выбор варианта на основе контекста
        if context and 'user_id' in context:
            hash_input = f"{flag_name}:{context['user_id']}"
            hash_value = int(hashlib.md5(hash_input.encode()).hexdigest(), 16)
            percentage = (hash_value % 10000) / 100.0
            
            # Распределение по процентам
            cumulative = 0
            for variant, config in flag.variants.items():
                cumulative += config.get('percentage', 0)
                if percentage < cumulative:
                    return config['value']
        
        return flag.default_value
    
    def _evaluate_rule(self, rule: Dict, context: Dict[str, Any]) -> bool:
        """Вычисление targeting-правила."""
        condition = rule.get('condition', {})
        
        if 'user_segment' in condition:
            user_segment = context.get('user_segment')
            return user_segment in condition['user_segment']
        
        if 'environment' in condition:
            current_env = os.environ.get('ENVIRONMENT')
            return current_env in condition['environment']
        
        if 'percentage' in condition:
            user_id = context.get('user_id', '')
            hash_value = int(hashlib.md5(user_id.encode()).hexdigest(), 16)
            return (hash_value % 100) < condition['percentage']
        
        return False
