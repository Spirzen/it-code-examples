struct BankAccount {
    owner: String,
    balance: i32,
}

impl BankAccount {
    fn new(owner: &str) -> Self {
        Self {
            owner: owner.to_string(),
            balance: 1000,
        }
    }

    fn deposit(&mut self, amount: i32) {
        self.balance += amount;
        println!("Пополнение: +{} ₽. Баланс: {} ₽", amount, self.balance);
    }

    fn withdraw(&mut self, amount: i32) {
        if amount > self.balance {
            println!("Ошибка: недостаточно средств");
            return;
        }
        self.balance -= amount;
        println!("Снятие: -{} ₽. Баланс: {} ₽", amount, self.balance);
    }

    fn show_balance(&self) {
        println!("Текущий баланс: {} ₽", self.balance);
    }
}

fn main() {
    let mut account = BankAccount::new("Иван");
    account.deposit(500);
    account.withdraw(200);
    account.show_balance();
    println!("Попытка прямого доступа к балансу...");
    // account.balance = 999999; // error[E0616]: field `balance` is private
    println!("Ошибка: прямой доступ к балансу запрещён");
    account.show_balance();
}
