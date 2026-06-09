class BankAccount {
    private String owner;
    private int balance;

    BankAccount(String owner) {
        this.owner = owner;
        this.balance = 1000;
    }

    void deposit(int amount) {
        balance += amount;
        System.out.println("Пополнение: +" + amount + " ₽. Баланс: " + balance + " ₽");
    }

    void withdraw(int amount) {
        if (amount > balance) {
            System.out.println("Ошибка: недостаточно средств");
            return;
        }
        balance -= amount;
        System.out.println("Снятие: -" + amount + " ₽. Баланс: " + balance + " ₽");
    }

    void showBalance() {
        System.out.println("Текущий баланс: " + balance + " ₽");
    }
}

public class Main {
    public static void main(String[] args) {
        BankAccount account = new BankAccount("Иван");
        account.deposit(500);
        account.withdraw(200);
        account.showBalance();
        System.out.println("Попытка прямого доступа к балансу...");
        // account.balance = 999999; // ошибка компиляции: balance has private access
        System.out.println("Ошибка: прямой доступ к балансу запрещён");
        account.showBalance();
    }
}
