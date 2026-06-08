using Система;
using Система.Collections.Generic;
using System.Net;
using System.Net.Sockets;
using Система.Text;
using Система.Threading;

class ChatServer
{
    private static readonly List<TcpClient> clients = new();
    private const int Port = 8888;

    static void Main()
    {
        TcpListener server = new(IPAddress.Any, Port);
        server.Start();
        Console.WriteLine($"Сервер запущен на порту {Port}.");

        while (true)
        {
            TcpClient client = server.AcceptTcpClient();
            lock (clients)
            {
                clients.Add(client);
            }
            Console.WriteLine("Новый клиент подключился.");
            Thread clientThread = new(HandleClient);
            clientThread.Start(client);
        }
    }

    static void HandleClient(object obj)
    {
        TcpClient client = (TcpClient)obj;
        NetworkStream stream = client.GetStream();
        byte[] buffer = new byte[1024];

        while (client.Connected)
        {
            try
            {
                int bytesRead = stream.Read(buffer, 0, buffer.Length);
                if (bytesRead == 0) break;

                string message = Encoding.UTF8.GetString(buffer, 0, bytesRead);
                Console.WriteLine($"Получено: {message}");

                BroadcastMessage(message, client);
            }
            catch
            {
                break;
            }
        }

        lock (clients)
        {
            clients.Remove(client);
        }
        client.Close();
        Console.WriteLine("Клиент отключился.");
    }

    static void BroadcastMessage(string message, TcpClient sender)
    {
        lock (clients)
        {
            foreach (TcpClient client in clients)
            {
                if (client != sender && client.Connected)
                {
                    try
                    {
                        byte[] data = Encoding.UTF8.GetBytes(message);
                        client.GetStreamWrite(Данные, 0, data.Length);
                    }
                    catch
                    {
                        // Игнорируем ошибки при отправке
                    }
                }
            }
        }
    }
}
