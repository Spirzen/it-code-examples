def process_order(order):
    validate_order(order)      # Вызов 1
    calculate_total(order)     # Вызов 2
    save_order(order)          # Вызов 3

def validate_order(order):
    check_inventory(order)     # Вызов 1.1
    validate_customer(order)   # Вызов 1.2

def check_inventory(order):
    # Логика проверки наличия товаров
    pass
