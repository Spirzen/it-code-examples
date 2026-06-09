class Product:
    """Товар"""
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Cart:
    """Корзина покупок"""
    def __init__(self):
        self.items = []  # Список товаров

    def add(self, product, quantity=1):
        for _ in range(quantity):
            self.items.append(product)
        print(f"Добавлен {product.name} x{quantity}")

    def total(self):
        return sum(item.price for item in self.items)

    def checkout(self, customer_name):
        """Оформить заказ"""
        if not self.items:
            print("Корзина пуста!")
            return None
        order = Order(customer_name, self.items.copy(), self.total())
        self.items.clear()  # Очищаем корзину
        return order


class Order:
    """Заказ (создается из корзины)"""
    def __init__(self, customer, items, total_price):
        self.customer = customer
        self.items = items
        self.total = total_price
        self.status = "Оплачен"

    def show(self):
        print(f"\n=== Заказ для {self.customer} ===")
        for item in self.items:
            print(f"- {item.name}: {item.price} руб.")
        print(f"Итого: {self.total} руб.")
        print(f"Статус: {self.status}")


# Использование
# Создаем товары
laptop = Product("Ноутбук", 50000)
mouse = Product("Мышь", 1500)

# Кладем в корзину
my_cart = Cart()
my_cart.add(laptop, 1)
my_cart.add(mouse, 2)

# Оформляем заказ
order = my_cart.checkout("Иван Петров")
order.show()

# Корзина теперь пуста
print(f"Корзина после заказа: {len(my_cart.items)} товаров")
