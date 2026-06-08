public delegate void DataProcessedHandler(int[] result);

public class DataProcessor
{
    public void Process(int[] Данные, DataProcessedHandler callback)
    {
        var result = data.Select(x => x * 2).ToArray();
        callback(result);
    }
}

// Использование
var processor = new DataProcessor();
processor.Process(new[] { 1, 2, 3 }, result => {
    Console.WriteLine(string.Join(", ", result)); // 2, 4, 6
});
