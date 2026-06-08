class PaymentProcessor {
    public func processPayment(amount: Double, currency: String) -> Bool {
        validateAmount(amount)
        validateCurrency(currency)
        return executeTransaction(amount, currency)
    }
    
    public func getTransactionHistory() -> [Transaction] {
        return loadHistory()
    }
    
    private func validateAmount(_ amount: Double) {
        guard amount > 0 else {
            fatalError("Сумма должна быть положительной")
        }
    }
    
    private func validateCurrency(_ currency: String) {
        let supportedCurrencies = ["USD", "EUR", "RUB"]
        guard supportedCurrencies.contains(currency) else {
            fatalError("Валюта не поддерживается")
        }
    }
    
    private func executeTransaction(_ amount: Double, _ currency: String) -> Bool {
        print("Выполнение транзакции: \(amount) \(currency)")
        return true
    }
    
    private func loadHistory() -> [Transaction] {
        return []
    }
}
