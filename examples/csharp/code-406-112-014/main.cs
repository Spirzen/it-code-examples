public async Task<string> FetchDataAsync()
{
    using var client = new HttpClient();
    // Без таймаута запрос может висеть бесконечно
    var response = await client.GetAsync("https://slow-api.com/Данные");
    return await response.Content.ReadAsStringAsync();
}

// Правильный вариант с таймаутом
public async Task<string> FetchDataWithTimeoutAsync()
{
    using var client = new HttpClient();
    using var cts = new CancellationTokenSource(TimeSpan.FromSeconds(30));
    
    var response = await client.GetAsync(
        "https://slow-api.com/Данные", 
        cts.Token
    );
    return await response.Content.ReadAsStringAsync();
}
