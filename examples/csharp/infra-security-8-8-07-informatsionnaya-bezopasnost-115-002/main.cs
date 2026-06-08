using System;
using System.IO;
using System.Security.Cryptography;
using System.Text;

class AesExample
{
    static void Main()
    {
        using Aes aes = Aes.Create();
        byte[] plaintext = Encoding.UTF8.GetBytes("Secret message");
        
        // Шифрование
        ICryptoTransform encryptor = aes.CreateEncryptor(aes.Key, aes.IV);
        byte[] ciphertext;
        using (MemoryStream ms = new MemoryStream())
        {
            using (CryptoStream cs = new CryptoStream(ms, encryptor, CryptoStreamMode.Write))
            {
                cs.Write(plaintext, 0, plaintext.Length);
            }
            ciphertext = ms.ToArray();
        }
        
        Console.WriteLine($"Открытый текст: {Encoding.UTF8.GetString(plaintext)}");
        Console.WriteLine($"Шифротекст (байты): {BitConverter.ToString(ciphertext)}");
    }
}
