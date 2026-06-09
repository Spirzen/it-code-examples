class BankAccount {
    private String owner
    private int balance

    BankAccount(String owner) {
        this.owner = owner
        this.balance = 1000
    }

    void deposit(int amount) {
        balance += amount
        println "Пополнение: +${amount} ₽. Баланс: ${balance} ₽"
    }

    void withdraw(int amount) {
        if (amount > balance) {
            println 'Ошибка: недостаточно средств'
            return
        }
        balance -= amount
        println "Снятие: -${amount} ₽. Баланс: ${balance} ₽"
    }

    void showBalance() {
        println "Текущий баланс: ${balance} ₽"
    }
}

def account = new BankAccount('Иван')
account.deposit(500)
account.withdraw(200)
account.showBalance()
println 'Попытка прямого доступа к балансу...'
try {
    account.balance = 999999
    println 'Взлом удался!'
} catch (MissingPropertyException ignored) {
    println 'Ошибка: прямой доступ к балансу запрещён'
}
account.showBalance()
