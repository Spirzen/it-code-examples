# lib/billing/invoice.rb
module Billing
  class Invoice
    # реализация
  end
end

# lib/billing/payment_processor.rb
module Billing
  class PaymentProcessor
    # реализация
  end
end

# Использование
invoice = Billing::Invoice.new(order)
Billing::PaymentProcessor.charge(invoice)
