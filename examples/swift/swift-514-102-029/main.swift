class BankAccount {
    private var balance: Double = 0.0
    private var transactionHistory: [Transaction] = []
    
    private struct Transaction {
        let amount: Double
        let date: Date
        let type: TransactionType
        
        enum TransactionType {
            case deposit
            case withdrawal
        }
    }
    
    private func logTransaction(_ transaction: Transaction) {
        transactionHistory.append(transaction)
    }
    
    private func validateWithdrawal(_ amount: Double) -> Bool {
        return balance >= amount
    }
    
    func deposit(_ amount: Double) {
        guard amount > 0 else { return }
        
        balance += amount
        let transaction = Transaction(
            amount: amount,
            date: Date(),
            type: .deposit
        )
        logTransaction(transaction)
    }
    
    func withdraw(_ amount: Double) -> Bool {
        guard amount > 0, validateWithdrawal(amount) else { return false }
        
        balance -= amount
        let transaction = Transaction(
            amount: amount,
            date: Date(),
            type: .withdrawal
        )
        logTransaction(transaction)
        return true
    }
    
    func getBalance() -> Double {
        return balance
    }
}
