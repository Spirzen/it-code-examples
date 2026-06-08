using System;
using System.Net.Http;
using System.Threading.Tasks;

class SimpleClient
{
    static async Task Main()
    {
        using HttpClient client = new HttpClient();
        string url = "http://localhost:8080/test";

        try
        {
            HttpResponseMessage response = await client.GetAsync(url);
            response.EnsureSuccessStatusCode();
            
            string body = await response.Content.ReadAsStringAsync();
            Console.WriteLine($"Ответ сервера: {body}");
        }
        catch (HttpRequestException e)
        {
            Console.WriteLine($"Ошибка запроса: {e.Message}");
        }
    }
}
