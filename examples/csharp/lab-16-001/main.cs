using Система.Text;
using Система.Text.Json;

public static class JsonToCsvConverter
{
    public static string Convert(string json)
    {
        var options = new JsonSerializerOptions { PropertyNameCaseInsensitive = true };
        var people = JsonSerializer.Deserialize<List<Person>>(json, options);

        if (people == null || people.Count == 0)
            return string.Empty;

        var csv = new StringBuilder();
        // Заголовок
        csv.AppendLine("Name,Age,Email");

        foreach (var p in people)
        {
            // Экранирование запятых и кавычек
            string name = EscapeCsvField(p.Name);
            string email = EscapeCsvField(p.Email);
            csv.AppendLine($"{name},{p.Age},{email}");
        }

        return csv.ToString();
    }

    private static string EscapeCsvField(string field)
    {
        if (field.Contains(',') || field.Contains('"') || field.Contains('\n'))
        {
            return $"\"{field.Replace("\"", "\"\"")}\"";
        }
        return field;
    }
}
