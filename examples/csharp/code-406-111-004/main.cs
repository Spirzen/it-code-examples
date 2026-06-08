public string ReadFile(string path)
{
    try
    {
        return File.ReadAllText(path);
    }
    catch (FileNotFoundException)
    {
        // Обработка конкретной ошибки
        return "Файл не найден";
    }
    catch (IOException ex)
    {
        // Обработка других ошибок ввода-вывода
        throw new ApplicationException("Ошибка чтения файла", ex);
    }
}
