// Конкретный тип
services.AddSingleton<ILoggerProvider, FileLoggerProvider>();

// Интерфейс → реализация
services.AddScoped<IRepository, EfRepository>();

// Фабрика
services.AddTransient<IService>(sp => {
    var config = sp.GetRequiredService<IConfiguration>();
    return new MyService(config["ApiKey"]);
});

// Декоратор (ручная реализация)
services.AddScoped<ICacheService, RedisCacheService>();
services.Decorate<ICacheService, LoggingCacheDecorator>();
// (требует Microsoft.Extensions.DependencyInjection.Decorator или аналога)
