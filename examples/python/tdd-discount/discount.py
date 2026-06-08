def get_discount_percent(amount: int) -> int:
    if amount >= 5000:
        return 10
    if amount >= 1000:
        return 5
    return 0
