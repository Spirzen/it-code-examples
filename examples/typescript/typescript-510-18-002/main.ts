class Account {
  protected balance = 0;

  deposit(amount: number): void {
    if (amount <= 0) throw new Error("amount > 0");
    this.balance += amount;
  }

  getBalance(): number {
    return this.balance;
  }
}

class SavingsAccount extends Account {
  addInterest(rate: number): void {
    this.balance *= 1 + rate;
  }
}
