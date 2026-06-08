public class Author
{
    [Key]
    public int Id { get; set; }
    public List<Book> Books { get; set; }  // Навигационное свойство
}

public class Book
{
    [Key]
    public int Id { get; set; }
    public int AuthorId { get; set; }      // Внешний ключ

    [ForeignKey("AuthorId")]
    public Author Author { get; set; }      // Навигационное свойство
}
