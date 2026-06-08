Account = { balance = 0 }
Account.__index = Account

function Account:new(initial_balance)
    local obj = { balance = initial_balance or 0 }
    setmetatable(obj, self)
    return obj
end

function Account:deposit(amount)
    self.balance = self.balance + amount
end

a = Account:new(100)
a:deposit(50)
print(a.balance)  --> 150
