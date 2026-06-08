public class LoanService
{
    private readonly LibraryContext _context;

    public LoanService(LibraryContext context)
    {
        _context = context;
    }

    public async Task<Result> IssueBookAsync(int bookId, int readerId)
    {
        var activeLoan = await _context.Loans
            .FirstOrDefaultAsync(l => l.BookId == bookId && !l.IsReturned);
        
        if (activeLoan != null)
            return Result.Failure("Книга уже выдана");

        var loan = new Loan
        {
            BookId = bookId,
            ReaderId = readerId,
            IssueDate = DateTime.UtcNow
        };

        _context.Loans.Add(loan);
        await _context.SaveChangesAsync();
        return Result.Success();
    }

    public async Task<Result> ReturnBookAsync(int loanId)
    {
        var loan = await _context.Loans.FindAsync(loanId);
        if (loan == null || loan.IsReturned)
            return Result.Failure("Неверный ID выдачи или книга уже возвращена");

        loan.ReturnDate = DateTime.UtcNow;
        await _context.SaveChangesAsync();
        return Result.Success();
    }
}
