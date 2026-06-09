class BankAccount
{
    private readonly string owner;
    private int balance;

    public BankAccount(string owner)
    {
        this.owner = owner;
        balance = 1000;
    }

    public void Deposit(int amount)
    {
        balance += amount;
        Console.WriteLine($"Пополнение: +{amount} ₽. Баланс: {balance} ₽");
    }

    public void Withdraw(int amount)
    {
        if (amount > balance)
        {
            Console.WriteLine("Ошибка: недостаточно средств");
            return;
        }
        balance -= amount;
        Console.WriteLine($"Снятие: -{amount} ₽. Баланс: {balance} ₽");
    }

    public void ShowBalance()
    {
        Console.WriteLine($"Текущий баланс: {balance} ₽");
    }
}

class Program
{
    static void Main()
    {
        var account = new BankAccount("Иван");
        account.Deposit(500);
        account.Withdraw(200);
        account.ShowBalance();
        Console.WriteLine("Попытка прямого доступа к балансу...");
        // account.balance = 999999; // CS0122: balance is inaccessible
        Console.WriteLine("Ошибка: прямой доступ к балансу запрещён");
        account.ShowBalance();
    }
}
