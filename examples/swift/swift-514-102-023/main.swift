class PaymentMethod {
    func processPayment(amount: Double) {
        print("Обработка платежа: \(amount)")
    }
}

class CreditCardPayment: PaymentMethod {
    override func processPayment(amount: Double) {
        print("Обработка платежа кредитной картой: \(amount)")
    }
}

class PayPalPayment: PaymentMethod {
    override func processPayment(amount: Double) {
        print("Обработка платежа через PayPal: \(amount)")
    }
}

class CryptoPayment: PaymentMethod {
    override func processPayment(amount: Double) {
        print("Обработка платежа криптовалютой: \(amount)")
    }
}

class PaymentProcessor {
    var paymentMethod: PaymentMethod
    
    init(paymentMethod: PaymentMethod) {
        self.paymentMethod = paymentMethod
    }
    
    func executePayment(amount: Double) {
        paymentMethod.processPayment(amount: amount)
    }
}

let processor = PaymentProcessor(paymentMethod: CreditCardPayment())
processor.executePayment(amount: 1000.0)

processor.paymentMethod = PayPalPayment()
processor.executePayment(amount: 1000.0)

processor.paymentMethod = CryptoPayment()
processor.executePayment(amount: 1000.0)
