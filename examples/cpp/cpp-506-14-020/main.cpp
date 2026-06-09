#include <iostream>
#include <string>

class BankAccount {
private:
    std::string owner;
    int balance;

public:
    BankAccount(const std::string& owner) : owner(owner), balance(1000) {}

    void deposit(int amount) {
        balance += amount;
        std::cout << "Пополнение: +" << amount << " ₽. Баланс: " << balance << " ₽" << std::endl;
    }

    void withdraw(int amount) {
        if (amount > balance) {
            std::cout << "Ошибка: недостаточно средств" << std::endl;
            return;
        }
        balance -= amount;
        std::cout << "Снятие: -" << amount << " ₽. Баланс: " << balance << " ₽" << std::endl;
    }

    void show_balance() const {
        std::cout << "Текущий баланс: " << balance << " ₽" << std::endl;
    }
};

int main() {
    BankAccount account("Иван");
    account.deposit(500);
    account.withdraw(200);
    account.show_balance();
    std::cout << "Попытка прямого доступа к балансу..." << std::endl;
    // account.balance = 999999; // error: 'balance' is private
    std::cout << "Ошибка: прямой доступ к балансу запрещён" << std::endl;
    account.show_balance();
    return 0;
}
