struct Product {
    let name: String
    let price: Int
}

class Cart {
    var items: [Product] = []

    func add(_ product: Product) {
        items.append(product)
        print("В корзину добавлено: \(product.name) (\(product.price) ₽)")
    }

    func total() -> Int {
        items.reduce(0) { $0 + $1.price }
    }
}

class Order {
    let items: [Product]
    let total: Int

    init(cart: Cart) {
        self.items = cart.items
        self.total = cart.total()
    }

    func checkout() {
        print("Оформление заказа...")
        for item in items {
            print("  — \(item.name): \(item.price) ₽")
        }
        print("Итого: \(total) ₽")
        print("Заказ оформлен!")
    }
}

let cart = Cart()
cart.add(Product(name: "Книга", price: 500))
cart.add(Product(name: "Ручка", price: 50))
let order = Order(cart: cart)
order.checkout()
