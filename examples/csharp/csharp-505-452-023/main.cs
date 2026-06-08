[Fact]
public void AllServicesAreRegistered()
{
    var services = new ServiceCollection();
    var startup = new Startup(new ConfigurationBuilder().Build());
    startup.ConfigureServices(services);

    var provider = services.BuildServiceProvider();
    var scope = provider.CreateScope();

    // Попытка разрешить все transient-сервисы
    foreach (var descriptor in services.Where(d => d.Lifetime == ServiceLifetime.Transient))
    {
        if (descriptor.ServiceType.IsInterface || descriptor.ImplementationType != null)
        {
            var instance = scope.ServiceProvider.GetService(descriptor.ServiceType);
            Assert.NotNull(instance);
        }
    }
}
