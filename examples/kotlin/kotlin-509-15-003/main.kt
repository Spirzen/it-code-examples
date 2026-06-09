class BankAccount(private val owner: String) {
    private var balance: Int = 1000

    fun deposit(amount: Int) {
        balance += amount
        println("Пополнение: +$amount ₽. Баланс: $balance ₽")
    }

    fun withdraw(amount: Int) {
        if (amount > balance) {
            println("Ошибка: недостаточно средств")
            return
        }
        balance -= amount
        println("Снятие: -$amount ₽. Баланс: $balance ₽")
    }

    fun showBalance() {
        println("Текущий баланс: $balance ₽")
    }
}

fun main() {
    val account = BankAccount("Иван")
    account.deposit(500)
    account.withdraw(200)
    account.showBalance()
    println("Попытка прямого доступа к балансу...")
    // account.balance = 999999 // Cannot access 'balance': it is private
    println("Ошибка: прямой доступ к балансу запрещён")
    account.showBalance()
}
