public class BankAccount
{
    public class InsufficientFundsException : Exception
    {
        public decimal AttemptedAmount { get; }
        public decimal AvailableBalance { get; }

        public InsufficientFundsException(decimal attempted, decimal available)
            : base($"Недостаточно средств: запрошено {attempted}, доступно {available}")
        {
            AttemptedAmount = attempted;
            AvailableBalance = available;
        }
    }

    private decimal balance;

    public void Withdraw(decimal amount)
    {
        if (amount > balance)
            throw new InsufficientFundsException(amount, balance);
        balance -= amount;
    }
}
