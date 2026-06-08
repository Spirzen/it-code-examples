class BankAccount {
    var balance: Double = 0.0
    
    func deposit(amount: Double) {
        balance += amount
        print("Пополнение на \(amount). Баланс: \(balance)")
    }
    
    func withdraw(amount: Double) -> Bool {
        if balance >= amount {
            balance -= amount
            print("Снятие \(amount). Баланс: \(balance)")
            return true
        } else {
            print("Недостаточно средств")
            return false
        }
    }
}
