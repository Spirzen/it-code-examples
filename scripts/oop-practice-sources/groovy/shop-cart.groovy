class Product {
    String name
    int price

    Product(String name, int price) {
        this.name = name
        this.price = price
    }
}

class Cart {
    List<Product> items = []

    void add(Product product) {
        items << product
        println "В корзину добавлено: ${product.name} (${product.price} ₽)"
    }

    int total() {
        items.sum { it.price } ?: 0
    }
}

class Order {
    List<Product> items
    int total

    Order(Cart cart) {
        this.items = cart.items.toList()
        this.total = cart.total()
    }

    void checkout() {
        println 'Оформление заказа...'
        items.each { item ->
            println "  — ${item.name}: ${item.price} ₽"
        }
        println "Итого: ${total} ₽"
        println 'Заказ оформлен!'
    }
}

def cart = new Cart()
cart.add(new Product('Книга', 500))
cart.add(new Product('Ручка', 50))
def order = new Order(cart)
order.checkout()
