public class BankAccount
{
    private decimal _balance;

    public decimal Balance
    {
        get => _balance;
        private set
        {
            if (value < 0)
                throw new InvalidOperationException("Баланс не может быть отрицательным.");
            _balance = value;
        }
    }

    public void Deposit(decimal amount)
    {
        if (amount <= 0) throw new ArgumentException("Сумма должна быть положительной.");
        Balance += amount;
    }
}
