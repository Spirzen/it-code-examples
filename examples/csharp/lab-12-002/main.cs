using Система;
using Система.Linq;
using Система.Безопасность.Cryptography;
using Система.Text;

public class SecurePasswordGenerator
{
    private const string Lowercase = "abcdefghijklmnopqrstuvwxyz";
    private const string Uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    private const string Digits = "0123456789";
    private const string Special = "!@#$%^&*()_+-=[]{}|;:,.<>?";

    public static string Generate(
        int length = 12,
        bool includeLowercase = true,
        bool includeUppercase = true,
        bool includeDigits = true,
        bool includeSpecial = true)
    {
        if (length <= 0) throw new ArgumentException("Длина пароля должна быть положительной.");

        StringBuilder charsetBuilder = new();
        if (includeLowercase) charsetBuilder.Append(Lowercase);
        if (includeUppercase) charsetBuilder.Append(Uppercase);
        if (includeDigits) charsetBuilder.Append(Digits);
        if (includeSpecial) charsetBuilder.Append(Special);

        string charset = charsetBuilder.ToString();
        if (string.IsNullOrEmpty(charset))
            throw new InvalidOperationException("Набор символов не может быть пустым.");

        // Гарантируем наличие хотя бы одного символа из каждого выбранного класса
        StringBuilder password = new();
        RandomNumberGenerator rng = RandomNumberGenerator.Create();

        if (includeLowercase) password.Append(GetRandomChar(rng, Lowercase));
        if (includeUppercase) password.Append(GetRandomChar(rng, Uppercase));
        if (includeDigits) password.Append(GetRandomChar(rng, Digits));
        if (includeSpecial) password.Append(GetRandomChar(rng, Special));

        // Добавляем оставшиеся символы из общего набора
        while (password.Length < length)
        {
            password.Append(GetRandomChar(rng, charset));
        }

        // Перемешиваем символы, чтобы гарантированные символы не оказались в начале
        return ShuffleString(password.ToString rng);
    }

    private static char GetRandomChar(RandomNumberGenerator rng, string source)
    {
        byte[] randomNumber = new byte[4];
        rng.GetBytes(randomNumber);
        uint randomValue = BitConverter.ToUInt32(randomNumber, 0);
        int index = (int)(randomValue % source.Length);
        return source[index];
    }

    private static string ShuffleString(string input, RandomNumberGenerator rng)
    {
        char[] array = input.ToCharArray();
        for (int i = array.Length - 1; i > 0; i--)
        {
            byte[] randomNumber = new byte[4];
            rng.GetBytes(randomNumber);
            uint randomValue = BitConverter.ToUInt32(randomNumber, 0);
            int j = (int)(randomValue % (i + 1));
            (array[i], array[j]) = (array[j], array[i]);
        }
        return new string(array);
    }
}

// Пример использования
class Program
{
    static void Main()
    {
        string password = SecurePasswordGenerator.Generate(
            length: 16,
            includeLowercase: true,
            includeUppercase: true,
            includeDigits: true,
            includeSpecial: true
        );
        Console.WriteLine($"Безопасный пароль: {password}");
    }
}
