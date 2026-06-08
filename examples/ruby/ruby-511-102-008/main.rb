class BankAccount
  attr_reader :account_number
  
  def initialize(account_number, initial_balance)
    @account_number = account_number
    @balance = initial_balance
    @pin_code = generate_pin
  end
  
  public
  
  def deposit(amount)
    @balance += amount
    record_transaction(:deposit, amount)
  end
  
  def withdraw(amount, pin)
    if verify_pin(pin) && @balance >= amount
      @balance -= amount
      record_transaction(:withdrawal, amount)
      true
    else
      false
    end
  end
  
  protected
  
  def verify_pin(pin)
    @pin_code == pin
  end
  
  private
  
  def generate_pin
    rand(1000..9999)
  end
  
  def record_transaction(type, amount)
    puts "#{type.capitalize} of #{amount} at #{Time.now}"
  end
end

account = BankAccount.new("ACC123", 1000)
account.deposit(500)           # Работает
account.withdraw(200, 1234)    # Работает
# account.verify_pin(1234)     # Ошибка — метод защищенный
# account.generate_pin         # Ошибка — метод приватный
