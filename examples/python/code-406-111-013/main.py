def create_order(order, force=False):
    if not force:
        validate_order(order)
    # Принудительное создание
    save_order(order)

def validate_order(order):
    if order.amount <= 0:
        raise ValueError("Сумма заказа должна быть положительной")
    if not order.customer_name:
        raise ValueError("Имя клиента обязательно")
