using Система;
using Система.Collections.Generic;
using Система.Xml.Serialization;

[XmlRoot("Library")]
public class Library
{
    [XmlElement("Book")]
    public List<Book> Books { get; set; } = new();
}

public class Book
{
    [XmlAttribute("id")]
    public int Id { get; set; }

    [XmlElement("Title")]
    public string Title { get; set; } = string.Empty;

    [XmlElement("Author")]
    public string Author { get; set; } = string.Empty;

    [XmlElement("Year")]
    public int Year { get; set; }
}
