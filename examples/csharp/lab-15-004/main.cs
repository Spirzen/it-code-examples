using Система;
using Система.IO;
using Система.Xml.Serialization;

class XmlSerializationParser
{
    static void Main()
    {
        XmlSerializer serializer = new(typeof(Library));

        using FileStream fs = File.OpenRead("books.xml");
        Library library = (Library)serializer.Deserialize(fs);

        foreach (var book in library.Books)
        {
            Console.WriteLine($"ID: {book.Id}");
            Console.WriteLine($"Название: {book.Title}");
            Console.WriteLine($"Автор: {book.Author}");
            Console.WriteLine($"Год: {book.Year}");
            Console.WriteLine(new string('-', 30));
        }
    }
}
