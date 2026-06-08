
import yaml

from typing import Dict, Any, List
from dataclasses import dataclass

@dataclass
class ConfigDiff:
    path: str
    env_a_value: Any
    env_b_value: Any
    diff_type: str  # "added", "removed", "changed"

def compare_configs(
    config_a: Dict[str, Any],
    config_b: Dict[str, Any],
    path: str = ""
) -> List[ConfigDiff]:
    """Рекурсивное сравнение двух конфигураций."""
    diffs = []
    
    all_keys = set(config_a.keys()) | set(config_b.keys())
    
    for key in all_keys:
        current_path = f"{path}.{key}" if path else key
        
        if key not in config_a:
            diffs.append(ConfigDiff(
                path=current_path,
                env_a_value=None,
                env_b_value=config_b[key],
                diff_type="added"
            ))
        elif key not in config_b:
            diffs.append(ConfigDiff(
                path=current_path,
                env_a_value=config_a[key],
                env_b_value=None,
                diff_type="removed"
            ))
        elif isinstance(config_a[key], dict) and isinstance(config_b[key], dict):
            diffs.extend(compare_configs(config_a[key], config_b[key], current_path))
        elif config_a[key] != config_b[key]:
            diffs.append(ConfigDiff(
                path=current_path,
                env_a_value=config_a[key],
                env_b_value=config_b[key],
                diff_type="changed"
            ))
    
    return diffs

# Использование — сравнение staging и production
with open("config/staging.yaml") as f:
    staging_config = yaml.safe_load(f)

with open("config/production.yaml") as f:
    production_config = yaml.safe_load(f)

diffs = compare_configs(staging_config, production_config)

# Ожидаемые различия (разные значения для разных сред)
expected_differences = {
    "database.url",
    "cache.url",
    "log_level",
    "instance_count"
}

unexpected_diffs = [d for d in diffs if d.path not in expected_differences]

if unexpected_diffs:
    print("Обнаружены неожиданные расхождения:")
    for diff in unexpected_diffs:
        print(f"  {diff.path}: {diff.env_a_value} -> {diff.env_b_value}")
