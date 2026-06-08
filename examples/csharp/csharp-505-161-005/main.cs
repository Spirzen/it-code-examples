using System;
using System.Net;
using System.Threading.Tasks;

class SimpleServer
{
    static async Task Main()
    {
        string prefix = "http://localhost:8080/";
        HttpListener listener = new HttpListener();
        listener.Prefixes.Add(prefix);
        listener.Start();

        Console.WriteLine("Сервер запущен. Нажмите Ctrl+C для остановки.");

        try
        {
            while (true)
            {
                HttpListenerContext context = await listener.GetContextAsync();
                HttpListenerRequest request = context.Request;
                HttpListenerResponse response = context.Response;

                string responseBody = $"Получен запрос: {request.Url.PathAndQuery}";
                byte[] buffer = System.Text.Encoding.UTF8.GetBytes(responseBody);
                
                response.ContentLength64 = buffer.Length;
                System.IO.Stream output = response.OutputStream;
                await output.WriteAsync(buffer, 0, buffer.Length);
                output.Close();
            }
        }
        finally
        {
            listener.Stop();
        }
    }
}
