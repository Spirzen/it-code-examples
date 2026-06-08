def place_order(customer_id: str, items: list):
    validate_customer(customer_id)
    validate_inventory(items)
    charge_payment(customer_id, items)
    confirm_shipment(items)

def validate_customer(customer_id: str):
    # проверка
    pass

def validate_inventory(items: list):
    # проверка
    pass

def charge_payment(customer_id: str, items: list):
    # оплата
    pass

def confirm_shipment(items: list):
    # отправка
    pass
