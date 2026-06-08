
import yaml

from typing import Dict, Any
from pathlib import Path

class ConfigGenerator:
    """Генератор конфигураций для всех окружений."""
    
    def __init__(self, matrix_path: str = "config_matrix.yaml"):
        with open(matrix_path) as f:
            self.matrix = yaml.safe_load(f)
        
        self.environments = ["development", "staging", "production"]
    
    def generate_all(self, output_dir: str = "config"):
        """Генерация конфигураций для всех окружений."""
        output_path = Path(output_dir)
        output_path.mkdir(exist_ok=True)
        
        for env in self.environments:
            config = self._build_config(env)
            
            config_file = output_path / f"{env}.yaml"
            with open(config_file, 'w') as f:
                yaml.dump(config, f, default_flow_style=False, sort_keys=False)
            
            print(f"✓ Сгенерирована конфигурация: {config_file}")
    
    def _build_config(self, environment: str) -> Dict[str, Any]:
        """Построение конфигурации для конкретного окружения."""
        config = {}
        
        # Общие параметры
        config.update(self.matrix['parameters']['common'])
        
        # Специфичные для окружения параметры
        for section_name, section_data in self.matrix['parameters'].items():
            if section_name == 'common':
                continue
            
            if isinstance(section_data, dict) and environment in section_data:
                config[section_name] = section_data[environment]
        
        # Добавление метаданных
        config['_metadata'] = {
            'environment': environment,
            'generated_at': datetime.utcnow().isoformat(),
            'generator_version': '1.0.0'
        }
        
        return config
    
    def compare_environments(
        self, 
        env_a: str, 
        env_b: str
    ) -> Dict[str, Any]:
        """Сравнение конфигураций двух окружений."""
        config_a = self._build_config(env_a)
        config_b = self._build_config(env_b)
        
        return self._deep_diff(config_a, config_b)
    
    def _deep_diff(
        self, 
        obj_a: Any, 
        obj_b: Any, 
        path: str = ""
    ) -> Dict[str, Any]:
        """Рекурсивное сравнение двух объектов."""
        differences = {
            'added': {},
            'removed': {},
            'changed': {},
            'expected_differences': {}
        }
        
        if type(obj_a) != type(obj_b):
            differences['changed'][path] = {
                'from': obj_a,
                'to': obj_b,
                'type_change': True
            }
            return differences
        
        if isinstance(obj_a, dict):
            all_keys = set(obj_a.keys()) | set(obj_b.keys())
            
            for key in all_keys:
                current_path = f"{path}.{key}" if path else key
                
                if key not in obj_a:
                    differences['added'][current_path] = obj_b[key]
                elif key not in obj_b:
                    differences['removed'][current_path] = obj_a[key]
                else:
                    sub_diff = self._deep_diff(
                        obj_a[key], 
                        obj_b[key], 
                        current_path
                    )
                    for category, items in sub_diff.items():
                        differences[category].update(items)
        
        elif obj_a != obj_b:
            # Определение ожидааемых различий
            expected_diff_paths = {
                'scaling.replicas',
                'database.host',
                'database.name',
                'database.pool_size',
                'logging.level',
                'logging.sample_rate',
                'feature_flags'
            }
            
            if any(path.startswith(p) for p in expected_diff_paths):
                differences['expected_differences'][path] = {
                    'from': obj_a,
                    'to': obj_b
                }
            else:
                differences['changed'][path] = {
                    'from': obj_a,
                    'to': obj_b
                }
        
        return differences
