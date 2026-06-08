"""Модуль обработки платежей

Содержит компоненты для взаимодействия с платежными шлюзами,
валидации платежных данных и обработки результатов транзакций.
"""

def calculate_discount(amount: float, user_tier: str) -> float:
    """Рассчитывает размер скидки для пользователя на основе суммы заказа и уровня лояльности.

    Скидка применяется по следующим правилам:
    - Для сумм до 1000 рублей скидка не предоставляется
    - Для сумм от 1000 до 5000 рублей предоставляется скидка 5%
    - Для сумм свыше 5000 рублей:
        * Бронзовый уровень: 7%
        * Серебряный уровень: 10%
        * Золотой уровень: 15%

    Args:
        amount: Сумма заказа в рублях.
        user_tier: Уровень лояльности пользователя (bronze, silver, gold).

    Returns:
        Размер скидки в рублях.

    Raises:
        ValueError: Если сумма отрицательная или уровень лояльности некорректный.
    """
    if amount < 0:
        raise ValueError("Amount cannot be negative")
    
    if amount < 1000:
        return 0.0
    
    if amount < 5000:
        return amount * 0.05
    
    tier_discounts = {
        "bronze": 0.07,
        "silver": 0.10,
        "gold": 0.15
    }
    
    if user_tier not in tier_discounts:
        raise ValueError(f"Invalid user tier: {user_tier}")
    
    return amount * tier_discounts[user_tier]
