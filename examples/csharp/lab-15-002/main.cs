using Система;
using Система.Xml;

class XmlStreamReaderParser
{
    static void Main()
    {
        using XmlReader reader = XmlReader.Create("books.xml");

        while (reader.Read())
        {
            if (reader.NodeType == XmlNodeType.Element && reader.Name == "Book")
            {
                string id = reader.GetAttribute("id") ?? "N/A";
                Console.WriteLine($"Книга ID: {id}");

                // Читаем дочерние элементы
                if (reader.ReadToDescendant("Title"))
                {
                    string title = reader.ReadElementContentAsString();
                    Console.WriteLine($"  Название: {title}");
                }

                if (reader.ReadToNextSibling("Author"))
                {
                    string author = reader.ReadElementContentAsString();
                    Console.WriteLine($"  Автор: {author}");
                }

                if (reader.ReadToNextSibling("Year"))
                {
                    string year = reader.ReadElementContentAsString();
                    Console.WriteLine($"  Год: {year}");
                }

                Console.WriteLine(new string('-', 30));
            }
        }
    }
}
