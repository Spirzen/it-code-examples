#include <iostream>
#include <string>

class BankAccount {
private:
    std::string owner;
    double balance;

public:
    BankAccount(const std::string& name, double initialBalance)
        : owner(name), balance(initialBalance) {}

    void deposit(double amount) {
        if (amount > 0) balance += amount;
    }

    bool withdraw(double amount) {
        if (amount > 0 && amount <= balance) {
            balance -= amount;
            return true;
        }
        return false;
    }

    double getBalance() const {
        return balance;
    }

    std::string getOwner() const {
        return owner;
    }
};

int main() {
    BankAccount acc("Иван", 1000.0);
    acc.deposit(500.0);
    acc.withdraw(200.0);

    std::cout << acc.getOwner() << " — баланс: " << acc.getBalance() << std::endl;
    return 0;
}
