public abstract class BaseIntegrationService
{
    protected readonly IHttpClientFactory _httpClientFactory;
    protected readonly ILogger _logger;

    public BaseIntegrationService(IHttpClientFactory httpClientFactory, ILogger logger)
    {
        _httpClientFactory = httpClientFactory;
        _logger = logger;
    }

    public async Task<TResponse> ExecuteAsync<TRequest, TResponse>(
        TRequest request,
        CancellationToken ct = default)
    {
        // Шаг 1: Получить/обновить токен
        var token = await AcquireTokenAsync(ct);

        // Шаг 2: Создать клиент
        var client = _httpClientFactory.CreateClient();
        client.DefaultRequestHeaders.Authorization = new AuthenticationHeaderValue("Bearer", token);

        // Шаг 3: Подготовить запрос (абстрактный метод)
        var httpRequest = PrepareRequest(request);

        // Шаг 4: Отправить (можно обернуть в Polly retry policy)
        var response = await client.SendAsync(httpRequest, ct);

        // Шаг 5: Обработать ответ — делегируем специфическую логику
        return await HandleResponseAsync<TResponse>(response, ct);
    }

    // Защищённые абстрактные/виртуальные методы для кастомизации
    protected abstract Task<string> AcquireTokenAsync(CancellationToken ct);
    protected abstract HttpRequestMessage PrepareRequest<T>(T request);
    protected abstract Task<TResponse> HandleResponseAsync<TResponse>(
        HttpResponseMessage response, CancellationToken ct);
}
