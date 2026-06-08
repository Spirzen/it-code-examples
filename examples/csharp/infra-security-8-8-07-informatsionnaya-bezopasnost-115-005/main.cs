using System;
using System.Security.Cryptography;
using System.Text;

class HashExample
{
    static void Main()
    {
        string text = "Привет, мир!";
        Console.WriteLine($"Исходный текст: {text}");
        
        // Хеширование SHA-256
        using (SHA256 sha256 = SHA256.Create())
        {
            byte[] bytes = Encoding.UTF8.GetBytes(text);
            byte[] hash = sha256.ComputeHash(bytes);
            
            string hashString = BitConverter.ToString(hash).Replace("-", "").ToLower();
            Console.WriteLine($"SHA-256: {hashString}");
        }
        
        // Хеширование MD5
        using (MD5 md5 = MD5.Create())
        {
            byte[] bytes = Encoding.UTF8.GetBytes(text);
            byte[] hash = md5.ComputeHash(bytes);
            
            string hashString = BitConverter.ToString(hash).Replace("-", "").ToLower();
            Console.WriteLine($"MD5: {hashString}");
        }
    }
}
