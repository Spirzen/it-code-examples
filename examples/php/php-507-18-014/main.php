<?php

class BankAccount
{
    public function __construct(
        private string $owner,
        private int $balance = 1000
    ) {}

    public function deposit(int $amount): void
    {
        $this->balance += $amount;
        echo "Пополнение: +{$amount} ₽. Баланс: {$this->balance} ₽\n";
    }

    public function withdraw(int $amount): void
    {
        if ($amount > $this->balance) {
            echo "Ошибка: недостаточно средств\n";
            return;
        }
        $this->balance -= $amount;
        echo "Снятие: -{$amount} ₽. Баланс: {$this->balance} ₽\n";
    }

    public function showBalance(): void
    {
        echo "Текущий баланс: {$this->balance} ₽\n";
    }
}

$account = new BankAccount('Иван');
$account->deposit(500);
$account->withdraw(200);
$account->showBalance();
echo "Попытка прямого доступа к балансу...\n";
try {
    echo $account->balance;
} catch (Error $e) {
    echo "Ошибка: прямой доступ к балансу запрещён\n";
}
$account->showBalance();
