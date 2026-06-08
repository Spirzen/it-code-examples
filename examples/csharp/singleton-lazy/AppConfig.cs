public sealed class AppConfig
{
    private static readonly Lazy<AppConfig> _instance =
        new(() => new AppConfig());

    public static AppConfig Instance => _instance.Value;

    public string EnvironmentName { get; private set; } = "Development";

    private AppConfig()
    {
    }

    public void SetEnvironment(string value)
    {
        EnvironmentName = value;
    }
}
