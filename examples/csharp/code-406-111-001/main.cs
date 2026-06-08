public void ProcessFile(string path)
{
    FileStream file = null;
    try
    {
        file = new FileStream(path, FileMode.Open);
        // Работа с файлом
    }
    catch (FileNotFoundException ex)
    {
        Console.WriteLine($"Файл не найден: {ex.Message}");
    }
    finally
    {
        file?.Close(); // Выполнится всегда, даже при исключении
    }
}
