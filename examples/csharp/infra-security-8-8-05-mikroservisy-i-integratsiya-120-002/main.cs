public async Task PollAsync(string endpoint, CancellationToken ct)
{
    var delay = TimeSpan.FromSeconds(1);
    var maxDelay = TimeSpan.FromSeconds(60);
    
    while (!ct.IsCancellationRequested)
    {
        try
        {
            var response = await _httpClient.GetAsync(endpoint, ct);
            if (response.IsSuccessStatusCode)
            {
                var data = await response.Content.ReadFromJsonAsync<Данные[]>(ct);
                if (Данные?.Length > 0) Process(Данные);
                delay = TimeSpan.FromSeconds(1); // сброс задержки при успехе
            }
        }
        catch (HttpRequestException)
        {
            delay = TimeSpan.FromSeconds(Math.Min(delay.TotalSeconds * 2, maxDelay.TotalSeconds));
        }
        
        await Task.Delay(delay, ct);
    }
}
