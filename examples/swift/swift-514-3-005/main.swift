actor BankAccount {
    private var balance: Double = 0

    init(initialBalance: Double) {
        balance = initialBalance
    }

    func deposit(_ amount: Double) {
        balance += amount
    }

    func withdraw(_ amount: Double) throws {
        guard amount <= balance else {
            throw BankError.insufficientFunds
        }
        balance -= amount
    }

    nonisolated func description() -> String {
        return "BankAccount"
    }
}
