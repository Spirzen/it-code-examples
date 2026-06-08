class Customer {
    let name: String
    var card: CreditCard?
    
    init(name: String) {
        self.name = name
    }
    
    deinit {
        print("\(name) удалён из системы")
    }
}

class CreditCard {
    let number: String
    unowned let customer: Customer
    
    init(number: String, customer: Customer) {
        self.number = number
        self.customer = customer
    }
    
    deinit {
        print("Карта \(number) деактивирована")
    }
}

var customer: Customer? = Customer(name: "Алексей")
customer?.card = CreditCard(number: "1234-5678-9012-3456", customer: customer!)

customer = nil
// Вывод:
// Карта 1234-5678-9012-3456 деактивирована
// Алексей удалён из системы
