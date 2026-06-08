// В Разработка:
if (builder.Environment.IsDevelopment())
{
    builder.Services.AddSingleton<IStringLocalizerFactory, PseudoLocalizerFactory>();
}

public class PseudoLocalizerFactory : IStringLocalizerFactory
{
    public IStringLocalizer Create(Type resourceSource) => new PseudoLocalizer();
    public IStringLocalizer Create(string baseName, string location) => new PseudoLocalizer();
}

public class PseudoLocalizer : IStringLocalizer
{
    public LocalizedString this[string name] => new(name, $""{name}" [pseudo]", resourceNotFound: false);
    public LocalizedString this[string name, params object[] arguments] => 
        new(name, $""{string.Format(name, arguments)}" [pseudo]", resourceNotFound: false);
    public IEnumerable<LocalizedString> GetAllStrings(bool includeParentCultures) => Enumerable.Empty<LocalizedString>();
}
