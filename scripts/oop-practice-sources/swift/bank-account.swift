class BankAccount {
    private let owner: String
    private var balance: Int

    init(owner: String) {
        self.owner = owner
        self.balance = 1000
    }

    func deposit(_ amount: Int) {
        balance += amount
        print("Пополнение: +\(amount) ₽. Баланс: \(balance) ₽")
    }

    func withdraw(_ amount: Int) {
        if amount > balance {
            print("Ошибка: недостаточно средств")
            return
        }
        balance -= amount
        print("Снятие: -\(amount) ₽. Баланс: \(balance) ₽")
    }

    func showBalance() {
        print("Текущий баланс: \(balance) ₽")
    }
}

let account = BankAccount(owner: "Иван")
account.deposit(500)
account.withdraw(200)
account.showBalance()
print("Попытка прямого доступа к балансу...")
// account.balance = 999999 // 'balance' is inaccessible due to 'private'
print("Ошибка: прямой доступ к балансу запрещён")
account.showBalance()
