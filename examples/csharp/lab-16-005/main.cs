using CsvHelper;
using CsvHelper.Configuration;
using Система.Globalization;
using Система.Text;
using Система.Text.Json;

public static class JsonToCsvWithHelper
{
    public static string Convert<T>(string json) where T : class
    {
        var records = JsonSerializer.Deserialize<List<T>>(json);
        if (records == null) return string.Empty;

        using var writer = new StringWriter();
        using var csv = new CsvWriter(writer, new CsvConfiguration(CultureInfo.InvariantCulture)
        {
            ShouldQuote = args => true // всегда оборачивать в кавычки
        });

        csv.WriteRecords(records);
        return writer.ToString();
    }
}

// Использование
string csv = JsonToCsvWithHelper.Convert<Person>(jsonInput);
