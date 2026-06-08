// Настройка пула потоков в ASP.NET Core
public void ConfigureServices(IServiceCollection services)
{
    // Явное ограничение параллелизма
    services.AddHttpClient("external-api")
        .ConfigurePrimaryHttpMessageHandler(() => new HttpClientHandler
        {
            MaxConnectionsPerServer = 100
        })
        .SetHandlerLifetime(TimeSpan.FromMinutes(5));
}

public void Configure(IApplicationBuilder app)
{
    // Ограничение параллельных запросов к приложению
    var threadPoolOptions = new ThreadPoolMinThreadsOptions
    {
        MinWorkerThreads = 50,
        MinCompletionPortThreads = 50
    };
}
