using Система;
using Система.Xml;

class XmlDocumentParser
{
    static void Main()
    {
        XmlDocument doc = new();
        doc.Load("books.xml");

        XmlNodeList books = doc.SelectNodes("/Library/Book");

        foreach (XmlNode book in books)
        {
            string id = book.Attributes?["id"]?.Value ?? "N/A";
            string title = book["Title"]?.InnerText ?? "Не указано";
            string author = book["Author"]?.InnerText ?? "Не указано";
            string year = book["Year"]?.InnerText ?? "Не указан";

            Console.WriteLine($"ID: {id}");
            Console.WriteLine($"Название: {title}");
            Console.WriteLine($"Автор: {author}");
            Console.WriteLine($"Год: {year}");
            Console.WriteLine(new string('-', 30));
        }
    }
}
