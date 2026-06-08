class SecureAccount
  attr_reader :account_number
  
  def initialize(account_number, initial_balance, pin)
    @account_number = account_number
    @balance = initial_balance
    @pin = pin
    @transaction_history = []
  end
  
  def deposit(amount)
    if amount > 0
      @balance += amount
      log_transaction(:deposit, amount)
      true
    else
      false
    end
  end
  
  def withdraw(amount, pin)
    if verify_pin(pin) && amount > 0 && @balance >= amount
      @balance -= amount
      log_transaction(:withdrawal, amount)
      true
    else
      false
    end
  end
  
  def balance(pin)
    verify_pin(pin) ? @balance : nil
  end
  
  def transaction_history(pin)
    verify_pin(pin) ? @transaction_history.dup : []
  end
  
  private
  
  attr_reader :balance
  
  def verify_pin(pin)
    @pin == pin
  end
  
  def log_transaction(type, amount)
    @transaction_history << {
      type: type,
      amount: amount,
      timestamp: Time.now
    }
  end
end

account = SecureAccount.new("ACC123", 1000, "1234")
account.deposit(500)

puts account.withdraw(200, "1234")  # true
puts account.withdraw(100, "0000")  # false (неверный PIN)

puts account.balance("1234")  # 1300
puts account.balance("0000")  # nil

history = account.transaction_history("1234")
puts history.size  # 2

# account.balance  # Ошибка — метод приватный
