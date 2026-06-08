// Асинхронный вызов с таймаутом
public async Task<UserData> GetUserAsync(int userId, CancellationToken ct)
{
    using var timeoutCts = new CancellationTokenSource(TimeSpan.FromSeconds(3));
    using var linkedCts = CancellationTokenSource.CreateLinkedTokenSource(ct, timeoutCts.Token);
    
    try
    {
        return await _httpClient.GetFromJsonAsync<UserData>(
            $"/api/users/{userId}", 
            linkedCts.Token);
    }
    catch (OperationCanceledException) when (timeoutCts.IsCancellationRequested)
    {
        throw new TimeoutException("Превышено время ожидания внешнего сервиса");
    }
}
