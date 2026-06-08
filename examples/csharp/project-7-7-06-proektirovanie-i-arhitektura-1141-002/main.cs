public readonly record struct Money(decimal Amount, string Currency)
{
    public Money(decimal amount, string currency)
    {
        if (amount < 0) throw new ArgumentOutOfRangeException(nameof(amount));
        if (string.IsNullOrWhiteSpace(currency)) throw new ArgumentException(nameof(currency));
        Amount = amount;
        Currency = currency;
    }

    public static Money operator +(Money left, Money right)
    {
        if (left.Currency != right.Currency)
            throw new InvalidOperationException("Складывать можно только одну валюту.");
        return new Money(left.Amount + right.Amount, left.Currency);
    }
}
