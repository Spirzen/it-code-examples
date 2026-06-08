class PaymentMethod
  def process_payment(amount)
    "Обработка платежа #{amount} рублей"
  end
  
  def refund(amount)
    "Возврат #{amount} рублей"
  end
end

class CreditCard < PaymentMethod
  def initialize(card_number)
    @card_number = card_number
  end
  
  def process_payment(amount)
    "Обработка платежа #{amount} рублей с карты #{@card_number}"
  end
  
  def refund(amount)
    "Возврат #{amount} рублей на карту #{@card_number}"
  end
end

class PayPal < PaymentMethod
  def initialize(email)
    @email = email
  end
  
  def process_payment(amount)
    "Обработка платежа #{amount} рублей через PayPal аккаунт #{@email}"
  end
  
  def refund(amount)
    "Возврат #{amount} рублей на аккаунт #{@email}"
  end
end

class Cash < PaymentMethod
  def process_payment(amount)
    "Принят наличный платеж #{amount} рублей"
  end
  
  def refund(amount)
    "Выдан наличный возврат #{amount} рублей"
  end
end

def complete_purchase(payment_method, amount)
  puts payment_method.process_payment(amount)
  puts payment_method.refund(amount * 0.1)
end

credit_card = CreditCard.new("4111-1111-1111-1111")
paypal = PayPal.new("user@example.com")
cash = Cash.new

complete_purchase(credit_card, 1000)
# Обработка платежа 1000 рублей с карты 4111-1111-1111-1111
# Возврат 100.0 рублей на карту 4111-1111-1111-1111

complete_purchase(paypal, 1500)
# Обработка платежа 1500 рублей через PayPal аккаунт user@example.com
# Возврат 150.0 рублей на аккаунт user@example.com

complete_purchase(cash, 500)
# Принят наличный платеж 500 рублей
# Выдан наличный возврат 50.0 рублей
