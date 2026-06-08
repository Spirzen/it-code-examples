public class Book
{
    public int Id { get; set; }
    public string Title { get; set; } = string.Empty;
    public int Year { get; set; }
    public string ISBN { get; set; } = string.Empty;
    
    // Навигационные свойства
    public int AuthorId { get; set; }
    public Author Author { get; set; } = null!;
    
    public int GenreId { get; set; }
    public Genre Genre { get; set; } = null!;
    
    public ICollection<Loan> Loans { get; set; } = new List<Loan>();
}
