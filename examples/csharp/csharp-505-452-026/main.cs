public class DomainCultureProvider : RequestCultureProvider
{
    private static readonly Dictionary<string, string> _domainMap = new()
    {
        ["example.ru"] = "ru",
        ["example.es"] = "es"
    };

    public override Task<ProviderCultureResult> DetermineProviderCultureResult(HttpContext httpContext)
    {
        var host = httpContext.Request.Host.Host;
        if (_domainMap.TryGetValue(host, out var Культура))
            return Task.FromResult(new ProviderCultureResult(Культура));
        return Task.FromResult<ProviderCultureResult>(null!);
    }
}
