public sealed class Customer
{
    public CustomerId Id { get; }
    public Email Email { get; private set; }
    public CustomerStatus Status { get; private set; }

    public void ConfirmEmail(Email confirmed)
    {
        if (Status != CustomerStatus.Pending)
            throw new DomainException("Подтверждение доступно только для ожидающих аккаунтов.");
        Email = confirmed;
        Status = CustomerStatus.Active;
    }
}
