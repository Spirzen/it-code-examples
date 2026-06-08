public class PasswordOptions
{
    public int Length { get; set; } = 12;
    public bool IncludeLowercase { get; set; } = true;
    public bool IncludeUppercase { get; set; } = true;
    public bool IncludeDigits { get; set; } = true;
    public bool IncludeSpecial { get; set; } = true;
    public string CustomSpecialChars { get; set; } = "!@#$%^&*()_+-=[]{}|;:,.<>?";
}

public class AdvancedPasswordGenerator
{
    public static string Generate(PasswordOptions options)
    {
        if (options.Length <= 0)
            throw new ArgumentException("Длина пароля должна быть положительной.");

        string lowercase = "abcdefghijklmnopqrstuvwxyz";
        string uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
        string digits = "0123456789";
        string special = options.CustomSpecialChars;

        StringBuilder charsetBuilder = new();
        if (options.IncludeLowercase) charsetBuilder.Append(lowercase);
        if (options.IncludeUppercase) charsetBuilder.Append(uppercase);
        if (options.IncludeDigits) charsetBuilder.Append(digits);
        if (options.IncludeSpecial && !string.IsNullOrEmpty(special))
            charsetBuilder.Append(special);

        string charset = charsetBuilder.ToString();
        if (string.IsNullOrEmpty(charset))
            throw new InvalidOperationException("Набор символов не может быть пустым.");

        StringBuilder password = new();
        RandomNumberGenerator rng = RandomNumberGenerator.Create();

        if (options.IncludeLowercase) password.Append(GetRandomChar(rng, lowercase));
        if (options.IncludeUppercase) password.Append(GetRandomChar(rng, uppercase));
        if (options.IncludeDigits) password.Append(GetRandomChar(rng, digits));
        if (options.IncludeSpecial && !string.IsNullOrEmpty(special))
            password.Append(GetRandomChar(rng, special));

        while (password.Length < options.Length)
        {
            password.Append(GetRandomChar(rng, charset));
        }

        return ShuffleString(password.ToString rng);
    }

    // Методы GetRandomChar и ShuffleString — как в предыдущем примере
}
