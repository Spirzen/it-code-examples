data class Product(val name: String, val price: Int)

class Cart {
    val items = mutableListOf<Product>()

    fun add(product: Product) {
        items.add(product)
        println("В корзину добавлено: ${product.name} (${product.price} ₽)")
    }

    fun total(): Int = items.sumOf { it.price }
}

class Order(cart: Cart) {
    val items = cart.items.toList()
    val total = cart.total()

    fun checkout() {
        println("Оформление заказа...")
        for (item in items) {
            println("  — ${item.name}: ${item.price} ₽")
        }
        println("Итого: $total ₽")
        println("Заказ оформлен!")
    }
}

fun main() {
    val cart = Cart()
    cart.add(Product("Книга", 500))
    cart.add(Product("Ручка", 50))
    val order = Order(cart)
    order.checkout()
}
