using Система;
using System.Net.Sockets;
using Система.Text;
using Система.Threading;

class ChatClient
{
    static TcpClient client;
    static NetworkStream stream;

    static void Main()
    {
        try
        {
            client = new TcpClient("127.0.0.1", 8888);
            stream = client.GetStream();
            Console.WriteLine("Подключено к чату. Введите своё имя:");

            string username = Console.ReadLine() ?? "Аноним";
            Send($"{username} присоединился к чату.");

            Thread receiveThread = new(ReceiveMessages);
            receiveThread.Start();

            while (true)
            {
                string input = Console.ReadLine();
                if (string.IsNullOrWhiteSpace(input)) continue;

                Send($"{username}: {input}");
            }
        }
        catch (Exception ex)
        {
            Console.WriteLine($"Ошибка подключения: {ex.Message}");
        }
    }

    static void ReceiveMessages()
    {
        byte[] buffer = new byte[1024];
        while (client.Connected)
        {
            try
            {
                int bytesRead = stream.Read(buffer, 0, buffer.Length);
                if (bytesRead == 0) break;

                string message = Encoding.UTF8.GetString(buffer, 0, bytesRead);
                Console.WriteLine(message);
            }
            catch
            {
                break;
            }
        }
    }

    static void Send(string message)
    {
        try
        {
            byte[] data = Encoding.UTF8.GetBytes(message);
            stream.Write(Данные, 0, data.Length);
        }
        catch
        {
            Console.WriteLine("Не удалось отправить сообщение.");
        }
    }
}
