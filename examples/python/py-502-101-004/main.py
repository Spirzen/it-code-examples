# До декомпозиции
def process_order(order_data):
    # Валидация данных
    if not order_data.get("user_id"):
        raise ValueError("User ID required")
    if not order_data.get("items"):
        raise ValueError("Items required")
    if len(order_data["items"]) == 0:
        raise ValueError("At least one item required")
    
    # Расчёт суммы
    total = 0
    for item in order_data["items"]:
        if item["quantity"] <= 0:
            raise ValueError("Quantity must be positive")
        total += item["price"] * item["quantity"]
    
    # Применение скидки
    if total > 1000:
        discount = total * 0.1
        total -= discount
    else:
        discount = 0
    
    # Сохранение заказа
    order = {
        "user_id": order_data["user_id"],
        "items": order_data["items"],
        "total": total,
        "discount": discount,
        "status": "pending",
        "created_at": datetime.now()
    }
    database.save_order(order)
    
    # Отправка уведомления
    send_email(order_data["user_id"], f"Order created: {order['id']}")
    
    return order

# После декомпозиции
def process_order(order_data):
    validate_order_data(order_data)
    total, discount = calculate_order_total(order_data["items"])
    order = create_order_record(order_data, total, discount)
    save_order_to_database(order)
    notify_user_about_order(order)
    return order

def validate_order_data(order_data):
    if not order_data.get("user_id"):
        raise ValueError("User ID required")
    if not order_data.get("items"):
        raise ValueError("Items required")
    if len(order_data["items"]) == 0:
        raise ValueError("At least one item required")
    for item in order_data["items"]:
        if item["quantity"] <= 0:
            raise ValueError("Quantity must be positive")

def calculate_order_total(items):
    total = sum(item["price"] * item["quantity"] for item in items)
    discount = total * 0.1 if total > 1000 else 0
    return total - discount, discount

def create_order_record(order_data, total, discount):
    return {
        "user_id": order_data["user_id"],
        "items": order_data["items"],
        "total": total,
        "discount": discount,
        "status": "pending",
        "created_at": datetime.now()
    }
