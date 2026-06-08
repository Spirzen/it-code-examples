local BankAccount = {}

function BankAccount:new(initialBalance)
    local privateData = {
        balance = initialBalance or 0,
        owner = "Unknown"
    }
    
    local publicInterface = setmetatable({}, {__index = self})
    
    function publicInterface:getBalance()
        return privateData.balance
    end
    
    function publicInterface:setOwner(name)
        if name and #name > 0 then
            privateData.owner = name
        end
    end
    
    function publicInterface:deposit(amount)
        if amount > 0 then
            privateData.balance = privateData.balance + amount
        end
    end
    
    function publicInterface:withdraw(amount)
        if amount > 0 and privateData.balance >= amount then
            privateData.balance = privateData.balance - amount
            return true
        end
        return false
    end
    
    return publicInterface
end

local account = BankAccount:new(1000)
account:setOwner("Иван")
account:deposit(500)
print(account:getBalance()) -- 1500
-- Попытка прямого доступа к балансу невозможна, так как он скрыт в замыкании
-- print(account.privateData.balance) -- Ошибка или nil
