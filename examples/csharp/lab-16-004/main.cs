using Система.Text;
using Система.Text.Json;

public static class DynamicJsonToCsv
{
    public static string Convert(string json)
    {
        using var doc = JsonDocument.Parse(json);
        if (doc.RootElement.ValueKind != JsonValueKind.Array)
            throw new ArgumentException("Корневой элемент должен быть массивом.");

        var csv = new StringBuilder();
        bool headerWritten = false;

        foreach (var item in doc.RootElement.EnumerateArray())
        {
            if (item.ValueKind != JsonValueKind.Object)
                continue;

            if (!headerWritten)
            {
                var headers = string.Join(",", GetPropertyNames(item));
                csv.AppendLine(headers);
                headerWritten = true;
            }

            var values = GetPropertyValues(item);
            csv.AppendLine(string.Join(",", values.Select(EscapeCsvField)));
        }

        return csv.ToString();
    }

    private static IEnumerable<string> GetPropertyNames(JsonElement obj)
    {
        foreach (var prop in obj.EnumerateObject())
            yield return prop.Name;
    }

    private static IEnumerable<string> GetPropertyValues(JsonElement obj)
    {
        foreach (var prop in obj.EnumerateObject())
        {
            yield return prop.Value.ValueKind switch
            {
                JsonValueKind.String => prop.Value.GetString() ?? "",
                JsonValueKind.Number => prop.Value.GetDecimalToString
                JsonValueKind.True => "true",
                JsonValueKind.False => "false",
                JsonValueKind.Null => "",
                _ => prop.Value.ToString()
            };
        }
    }

    private static string EscapeCsvField(string field)
    {
        if (field.Contains(',') || field.Contains('"') || field.Contains('\n'))
            return $"\"{field.Replace("\"", "\"\"")}\"";
        return field;
    }
}
