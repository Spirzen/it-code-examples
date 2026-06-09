class BankAccount:
    def __init__(self, owner, initial_balance=0):
        self.owner = owner
        self.__balance = initial_balance  # __balance скрытое поле (два подчеркивания)

    def deposit(self, amount):     # Положить деньги
        if amount > 0:
            self.__balance += amount
            print(f"Внесено {amount}. Баланс: {self.__balance}")

    def withdraw(self, amount):    # Снять деньги
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Снято {amount}. Баланс: {self.__balance}")
        else:
            print("Недостаточно средств!")

    def show_balance(self):
        print(f"Владелец: {self.owner}, Баланс: {self.__balance}")


# Использование
my_money = BankAccount("Иван", 1000)
my_money.show_balance()   # Владелец: Иван, Баланс: 1000
my_money.withdraw(200)    # Снято 200. Баланс: 800
my_money.__balance = 9999999  # Попытка взлома (не сработает, т.к. поле скрыто)
my_money.show_balance()   # Владелец: Иван, Баланс: 800 (защита сработала)
