// Плохо: множественные мелкие записи
using (var writer = new StreamWriter("log.txt"))
{
    foreach (var item in items)
    {
        writer.WriteLine(item.ToString()); // Отдельная операция ввода-вывода
    }
}

// Хорошо: пакетная запись с буферизацией
using (var writer = new StreamWriter("log.txt", bufferSize: 8192))
{
    var batch = new StringBuilder();
    foreach (var item in items)
    {
        batch.AppendLine(item.ToString());
        if (batch.Length > 8192)
        {
            writer.Write(batch.ToString());
            batch.Clear();
        }
    }
    writer.Write(batch.ToString());
}
