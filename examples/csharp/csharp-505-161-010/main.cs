using System;
using System.Net.Http;

class UrlChecker
{
    static async Task Main()
    {
        string[] urls = { 
            "https://example.com", 
            "https://nonexistent-site-12345.com",
            "http://localhost:8080" 
        };

        using HttpClient client = new HttpClient();
        client.Timeout = TimeSpan.FromSeconds(5);

        foreach (string url in urls)
        {
            try
            {
                Uri uri = new Uri(url);
                Console.WriteLine($"\nURL: {url}");
                Console.WriteLine($"Хост: {uri.Host}");
                Console.WriteLine($"Порт: {uri.Port}");
                Console.WriteLine($"Схема: {uri.Scheme}");

                HttpResponseMessage response = await client.GetAsync(url);
                
                if (response.IsSuccessStatusCode)
                {
                    Console.WriteLine($"Статус: Доступен ({(int)response.StatusCode})");
                }
                else
                {
                    Console.WriteLine($"Статус: Недоступен ({(int)response.StatusCode})");
                }
            }
            catch (Exception ex)
            {
                Console.WriteLine($"Ошибка: {ex.Message}");
            }
        }
    }
}
