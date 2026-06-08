local BankAccount = {}

function BankAccount:new(ownerName, initialBalance)
    local account = setmetatable({}, {__index = self})
    account.owner = ownerName
    account.balance = initialBalance or 0
    account.transactions = {}
    return account
end

function BankAccount:deposit(amount)
    if amount > 0 then
        self.balance = self.balance + amount
        table.insert(self.transactions, {type = "credit", amount = amount})
    end
end

function BankAccount:withdraw(amount)
    if amount > 0 and self.balance >= amount then
        self.balance = self.balance - amount
        table.insert(self.transactions, {type = "debit", amount = amount})
        return true
    end
    return false
end

-- Использование
local myAccount = BankAccount:new("Иван Иванов", 1000)
myAccount:deposit(500)
print(myAccount.balance) -- 1500
