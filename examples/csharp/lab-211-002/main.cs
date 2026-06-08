public class Loan
{
    public int Id { get; set; }
    public DateTime IssueDate { get; set; }
    public DateTime? ReturnDate { get; set; }
    public bool IsReturned => ReturnDate.HasValue;
    
    // Внешние ключи
    public int BookId { get; set; }
    public Book Book { get; set; } = null!;
    
    public int ReaderId { get; set; }
    public Reader Reader { get; set; } = null!;
}
