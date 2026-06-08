// Core/AppKernel.cs
public class SuperAppKernel
{
    private readonly IAuthService _authService;
    private readonly IPaymentGateway _paymentGateway;
    private readonly IProfileManager _profileManager;
    private readonly IModuleRegistry _moduleRegistry;

    public SuperAppKernel(
        IAuthService authService,
        IPaymentGateway paymentGateway,
        IProfileManager profileManager,
        IModuleRegistry moduleRegistry)
    {
        _authService = authService;
        _paymentGateway = paymentGateway;
        _profileManager = profileManager;
        _moduleRegistry = moduleRegistry;
    }

    public async Task InitializeAsync()
    {
        await _authService.InitializeAsync();
        await _paymentGateway.ConnectAsync();
        await _profileManager.LoadUserProfileAsync();
    }

    public async Task<IModuleResult> LaunchModuleAsync(string moduleName, ModuleContext context)
    {
        var module = _moduleRegistry.GetModule(moduleName);
        if (module == null)
            throw new ModuleNotFoundException($"Модуль {moduleName} не зарегистрирован");

        var safeContext = new SafeModuleContext
        {
            UserId = _authService.CurrentUserId,
            AuthToken = await _authService.GetShortLivedTokenAsync(),
            PaymentMethods = await _paymentGateway.ListAvailableMethodsAsync(),
            Permissions = _authService.GetUserPermissions()
        };

        return await module.ExecuteAsync(context, safeContext);
    }
}
