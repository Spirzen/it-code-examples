class BankAccount 
{
public:
    explicit BankAccount(double initial_balance)
        : balance_(initial_balance) 
    {
        if (initial_balance < 0.0) {
            throw std::invalid_argument("Initial balance cannot be negative");
        }
    }

    void deposit(double amount) 
    {
        if (amount <= 0.0) {
            throw std::invalid_argument("Deposit amount must be positive");
        }
        balance_ += amount;
    }

    void withdraw(double amount) 
    {
        if (amount <= 0.0) {
            throw std::invalid_argument("Withdrawal amount must be positive");
        }
        if (amount > balance_) {
            throw std::runtime_error("Insufficient funds");
        }
        balance_ -= amount;
    }

    double get_balance() const { return balance_; }

private:
    double balance_;
};
