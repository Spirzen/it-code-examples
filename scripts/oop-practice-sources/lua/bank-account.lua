local BankAccount = {}

function BankAccount:new(owner)
    local obj = setmetatable({owner = owner, _balance = 1000}, {__index = self})
    return obj
end

function BankAccount:deposit(amount)
    self._balance = self._balance + amount
    print("Пополнение: +" .. amount .. " ₽. Баланс: " .. self._balance .. " ₽")
end

function BankAccount:withdraw(amount)
    if amount > self._balance then
        print("Ошибка: недостаточно средств")
        return
    end
    self._balance = self._balance - amount
    print("Снятие: -" .. amount .. " ₽. Баланс: " .. self._balance .. " ₽")
end

function BankAccount:show_balance()
    print("Текущий баланс: " .. self._balance .. " ₽")
end

local account = BankAccount:new("Иван")
account:deposit(500)
account:withdraw(200)
account:show_balance()
print("Попытка прямого доступа к балансу...")
if account.balance ~= nil then
    account.balance = 999999
    print("Взлом удался!")
else
    print("Ошибка: прямой доступ к балансу запрещён")
end
account:show_balance()
