using Система.Text.Json;

public static class CsvToJsonConverter
{
    public static string Convert(string csv)
    {
        var lines = csv.Split(new[] { '\r', '\n' }, StringSplitOptions.RemoveEmptyEntries);
        if (lines.Length < 2) return "[]";

        var headers = ParseCsvLine(lines[0]);
        var people = new List<Person>();

        for (int i = 1; i < lines.Length; i++)
        {
            var values = ParseCsvLine(lines[i]);
            if (values.Length != headers.Length) continue;

            var person = new Person
            {
                Name = UnescapeCsvField(values[0]),
                Age = int.TryParse(values[1], out int age) ? age : 0,
                Email = UnescapeCsvField(values[2])
            };
            people.Add(person);
        }

        var options = new JsonSerializerOptions { WriteIndented = true };
        return JsonSerializer.Serialize(people, options);
    }

    private static string[] ParseCsvLine(string line)
    {
        var fields = new List<string>();
        bool inQuotes = false;
        var current = new StringBuilder();

        for (int i = 0; i < line.Length; i++)
        {
            char c = line[i];

            if (c == '"' && (i == 0 || line[i - 1] != '\\'))
            {
                inQuotes = !inQuotes;
            }
            else if (c == ',' && !inQuotes)
            {
                fields.Add(current.ToString());
                current.Clear();
            }
            else
            {
                current.Append(c);
            }
        }
        fields.Add(current.ToString());
        return fields.ToArray();
    }

    private static string UnescapeCsvField(string field)
    {
        if (field.StartsWith("\"") && field.EndsWith("\""))
        {
            return field.Substring(1, field.Length - 2).Replace("\"\"", "\"");
        }
        return field;
    }
}
