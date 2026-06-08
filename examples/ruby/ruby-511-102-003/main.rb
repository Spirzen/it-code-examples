class BankAccount
  def initialize(account_number, balance)
    @account_number = account_number
    @balance = balance
    @transactions = []
  end
  
  def deposit(amount)
    @balance += amount
    @transactions << { type: :deposit, amount: amount, date: Time.now }
  end
  
  def withdraw(amount)
    if @balance >= amount
      @balance -= amount
      @transactions << { type: :withdrawal, amount: amount, date: Time.now }
      true
    else
      false
    end
  end
end

account = BankAccount.new("12345", 1000)
account.deposit(500)
account.withdraw(200)
