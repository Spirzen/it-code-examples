using Система;
using Система.Text;

public class SimplePasswordGenerator
{
    private static readonly string DefaultCharset = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()";

    public static string Generate(int length = 12)
    {
        if (length <= 0) throw new ArgumentException("Длина пароля должна быть положительной.");

        Random random = new();
        StringBuilder password = new(length);

        for (int i = 0; i < length; i++)
        {
            int index = random.Next(DefaultCharset.Length);
            password.Append(DefaultCharset[index]);
        }

        return password.ToString();
    }
}

// Пример использования
class Program
{
    static void Main()
    {
        string password = SimplePasswordGenerator.Generate(16);
        Console.WriteLine($"Сгенерированный пароль: {password}");
    }
}
