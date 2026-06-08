public class InsufficientFundsException extends RuntimeException {
    private final String accountId;
    private final BigDecimal requiredAmount;
    private final BigDecimal availableBalance;

    public InsufficientFundsException(String accountId, BigDecimal required, BigDecimal available) {
        super("Недостаточно средств на счёте " + accountId +
              ". Требуется: " + required + ", доступно: " + available);
        this.accountId = accountId;
        this.requiredAmount = required;
        this.availableBalance = available;
    }

    // Геттеры для логирования, телеметрии, формирования UI-сообщений
    public String getAccountId() { return accountId; }
    public BigDecimal getRequiredAmount() { return requiredAmount; }
    public BigDecimal getAvailableBalance() { return availableBalance; }
}
