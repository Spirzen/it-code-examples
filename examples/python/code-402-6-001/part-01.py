# Импорты

import os

from typing import Dict

# Основная функция
def process_order(order_id: str) -> Dict[str, any]:
    validate_order(order_id)
    return _calculate_and_save(order_id)

# Вспомогательная функция
def _calculate_and_save(order_id: str) -> Dict[str, any]:
    # реализация
    return {"status": "processed"}
