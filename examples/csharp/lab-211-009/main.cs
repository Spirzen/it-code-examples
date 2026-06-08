[HttpGet]
public async Task<ActionResult<IEnumerable<Book>>> GetBooks()
{
    var cacheKey = "all-books";
    if (_cache.TryGetValue(cacheKey, out List<Book>? cachedBooks))
    {
        return cachedBooks;
    }

    var books = await _context.Books
        .Include(b => b.Author)
        .Include(b => b.Genre)
        .ToListAsync();

    var cacheEntryOptions = new MemoryCacheEntryOptionsSetAbsoluteExpiration(TimeSpan.FromMinutes(10));

    _cache.Set(cacheKey, books, cacheEntryOptions);
    return books;
}
