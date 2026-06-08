interface PaymentStrategy
{
    public function pay($amount);
}

class StripeStrategy implements PaymentStrategy
{
    public function pay($amount)
    {
        // Логика оплаты через Stripe
        return true;
    }
}

class PayPalStrategy implements PaymentStrategy
{
    public function pay($amount)
    {
        // Логика оплаты через PayPal
        return true;
    }
}
