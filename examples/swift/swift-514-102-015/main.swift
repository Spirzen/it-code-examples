class Product {
    let id: Int
    var name: String
    var price: Double
    var inStock: Bool
    
    init(id: Int, name: String, price: Double, inStock: Bool) {
        self.id = id
        self.name = name
        self.price = price
        self.inStock = inStock
    }
    
    convenience init(id: Int, name: String, price: Double) {
        self.init(id: id, name: name, price: price, inStock: true)
    }
}

let laptop = Product(id: 1, name: "Ноутбук", price: 50000.0, inStock: true)
let phone = Product(id: 2, name: "Смартфон", price: 30000.0)
