class BankAccount {
    #balance = 0;           // приватное поле (# — обязательный символ)
    
    deposit(amount) {
        if (amount > 0) this.#balance += amount;
    }
    
    getBalance() {
        return this.#balance;
    }
}

const acc = new BankAccount();
acc.deposit(100);
// console.log(acc.#balance); // Ошибка! Private field
console.log(acc.getBalance());  // 100
