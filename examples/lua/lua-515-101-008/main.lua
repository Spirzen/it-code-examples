local function create_bank_account(initial_balance)
  local balance = initial_balance or 0
  
  return {
    deposit = function(amount)
      if amount > 0 then
        balance = balance + amount
      end
    end,
    
    withdraw = function(amount)
      if amount > 0 and balance >= amount then
        balance = balance - amount
        return true
      end
      return false
    end,
    
    get_balance = function()
      return balance
    end
  }
end

local account = create_bank_account(100)
account.deposit(50)
account.withdraw(30)
print(account.get_balance())  -- 120
-- поле `balance` недоступно напрямую извне
