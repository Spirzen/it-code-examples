# Python (плохой пример)
def calculate_total(items, discount_type):
    total = sum(item.price for item in items)
    if discount_type == "seasonal":
        return total * 0.9
    elif discount_type == "vip":
        return total * 0.8
    elif discount_type == "promo":
        return total * 0.85
    return total
