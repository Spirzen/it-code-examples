class BankAccount {
    #balance = 0;
    #pinCode;
    
    constructor(owner, pinCode) {
        this.owner = owner;
        this.#pinCode = pinCode;
    }
    
    #validatePin(pin) {
        return pin === this.#pinCode;
    }
    
    deposit(amount) {
        if (amount > 0) {
            this.#balance += amount;
            return true;
        }
        return false;
    }
    
    withdraw(amount, pin) {
        if (this.#validatePin(pin) && amount <= this.#balance) {
            this.#balance -= amount;
            return true;
        }
        return false;
    }
    
    getBalance(pin) {
        if (this.#validatePin(pin)) {
            return this.#balance;
        }
        return "Неверный пин-код";
    }
}

const account = new BankAccount("Иван", "1234");
account.deposit(1000);
console.log(account.getBalance("1234")); // 1000
console.log(account.getBalance("0000")); // "Неверный пин-код"
// console.log(account.#balance); // Ошибка
