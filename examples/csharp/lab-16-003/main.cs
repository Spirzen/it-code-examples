class Program
{
    static void Main()
    {
        string jsonInput = @"[
            {""Name"": ""Алиса"", ""Age"": 28, ""Email"": ""alice@example.com""},
            {""Name"": ""Боб"", ""Age"": 34, ""Email"": ""bob@test.org""}
        ]";

        string csv = JsonToCsvConverter.Convert(jsonInput);
        Console.WriteLine("JSON → CSV:");
        Console.WriteLine(csv);

        string jsonOutput = CsvToJsonConverter.Convert(csv);
        Console.WriteLine("\nCSV → JSON:");
        Console.WriteLine(jsonOutput);
    }
}
