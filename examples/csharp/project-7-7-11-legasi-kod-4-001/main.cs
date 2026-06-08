// Новый домен не знает про LegacyCustomerRecord
public sealed class CustomerAdapter : ICustomerLookup
{
    private readonly ILegacySoapClient _legacy;

    public async Task<Customer> FindAsync(CustomerId id, CancellationToken ct)
    {
        var raw = await _legacy.GetCustomerAsync(id.Value, ct);
        return new Customer(
            id: new CustomerId(raw.CustNo),
            name: raw.FullName?.Trim() ?? "Unknown",
            tier: MapTier(raw.LoyaltyCode) // странные коды — только здесь
        );
    }

    private static Tier MapTier(string? code) => code switch
    {
        "V" => Tier.Vip,
        "G" => Tier.Gold,
        _ => Tier.Standard
    };
}
