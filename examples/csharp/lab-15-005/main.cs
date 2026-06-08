try
{
    XmlDocument doc = new();
    doc.Load("books.xml");
    // .. обработка
}
catch (XmlException ex)
{
    Console.WriteLine($"Ошибка XML: {ex.Message}");
}
catch (FileNotFoundException)
{
    Console.WriteLine("Файл не найден.");
}
catch (Exception ex)
{
    Console.WriteLine($"Неожиданная ошибка: {ex.Message}");
}
