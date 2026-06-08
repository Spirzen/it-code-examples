// Пример различных типов отношений
public class Author
{
    public int Id { get; set; }
    public string Name { get; set; }
    
    // Один-ко-многим: автор имеет много книг
    public virtual ICollection<Book> Books { get; set; }
}

public class Book
{
    public int Id { get; set; }
    public string Title { get; set; }
    public int AuthorId { get; set; }
    
    // Обратная связь один-ко-многим
    public virtual Author Author { get; set; }
    
    // Многие-ко-многим: книга имеет много жанров
    public virtual ICollection<Genre> Genres { get; set; }
}

public class Genre
{
    public int Id { get; set; }
    public string Name { get; set; }
    
    // Многие-ко-многим: жанр имеет много книг
    public virtual ICollection<Book> Books { get; set; }
}
