[HttpGet("search")]
public async Task<ActionResult<IEnumerable<Book>>> SearchBooks(
    [FromQuery] string? title = null,
    [FromQuery] string? author = null,
    [FromQuery] string? isbn = null)
{
    var query = _context.Books.AsQueryable();

    if (!string.IsNullOrEmpty(title))
        query = query.Where(b => b.Title.Contains(title));

    if (!string.IsNullOrEmpty(author))
        query = query.Where(b => b.Author.FirstName.Contains(author) || b.Author.LastName.Contains(author));

    if (!string.IsNullOrEmpty(isbn))
        query = query.Where(b => b.ISBN == isbn);

    return await query
        .Include(b => b.Author)
        .Include(b => b.Genre)
        .ToListAsync();
}
