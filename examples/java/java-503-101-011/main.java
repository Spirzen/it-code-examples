// Проверяемое исключение: вызывающий код может обработать недостаток средств
public void transferMoney(Account from, Account to, BigDecimal amount) 
        throws InsufficientFundsException {
    if (from.getBalance().compareTo(amount) < 0) {
        throw new InsufficientFundsException(from.getId(), amount);
    }
    // выполнение перевода
}

// Непроверяемое исключение: программная ошибка, которую нельзя обработать
public void processPayment(Payment payment) {
    if (payment == null) {
        throw new IllegalArgumentException("Payment cannot be null");
    }
    // обработка платежа
}
