class Account {
    BigDecimal balance = 0
    
    void deposit(BigDecimal amount) {
        if (amount <= 0) throw new IllegalArgumentException("Сумма должна быть положительной")
        balance += amount
    }
    
    boolean withdraw(BigDecimal amount) {
        if (amount > balance) return false
        balance -= amount
        true
    }
}
