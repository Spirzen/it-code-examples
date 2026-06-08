protocol JSONRepresentable {
    func toJSON() -> [String: Any]
}

extension Array: JSONRepresentable where Element: JSONRepresentable {
    func toJSON() -> [String: Any] {
        return ["items": self.map { $0.toJSON() }]
    }
}

extension Dictionary: JSONRepresentable where Value: JSONRepresentable {
    func toJSON() -> [String: Any] {
        return self.mapValues { $0.toJSON() }
    }
}

class Product: JSONRepresentable {
    var id: Int
    var name: String
    var price: Double
    
    init(id: Int, name: String, price: Double) {
        self.id = id
        self.name = name
        self.price = price
    }
    
    func toJSON() -> [String: Any] {
        return [
            "id": id,
            "name": name,
            "price": price
        ]
    }
}

let products = [
    Product(id: 1, name: "Ноутбук", price: 50000.0),
    Product(id: 2, name: "Мышь", price: 1500.0)
]

let json = products.toJSON()
print(json)
