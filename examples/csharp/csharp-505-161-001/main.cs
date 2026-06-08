using System;
using System.Linq;
using System.Security.Cryptography;

class PasswordGenerator
{
    static void Main()
    {
        int length = 16;
        string chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*";
        
        // Использование криптографически стойкого генератора
        var randomBytes = new byte[length];
        using (var rng = RandomNumberGenerator.Create())
        {
            rng.GetBytes(randomBytes);
        }

        char[] passwordChars = new char[length];
        for (int i = 0; i < length; i++)
        {
            int index = randomBytes[i] % chars.Length;
            passwordChars[i] = chars[index];
        }

        string password = new string(passwordChars);
        Console.WriteLine($"Сгенерированный пароль: {password}");
    }
}
