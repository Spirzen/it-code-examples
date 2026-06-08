public record ValidationResult(bool IsValid, string? ErrorMessage = null);

public static class EmailValidator
{
    public static ValidationResult Validate(string? email)
    {
        if (string.IsNullOrWhiteSpace(email))
            return new ValidationResult(false, "Email не может быть пустым");

        var parts = email.Split('@');
        if (parts.Length != 2)
            return new ValidationResult(false, "Email должен содержать ровно один символ '@'");

        var (local, domain) = (parts[0], parts[1]);

        if (string.IsNullOrEmpty(local))
            return new ValidationResult(false, "Локальная часть email не может быть пустой");

        if (string.IsNullOrEmpty(domain) || !domain.Contains('.') ||
            domain.StartsWith('.') || domain.EndsWith('.'))
            return new ValidationResult(false, "Некорректный домен: должен содержать точку и не начинаться/заканчиваться ею");

        return new ValidationResult(true);
    }
}
