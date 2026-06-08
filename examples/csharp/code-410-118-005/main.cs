// Пример проблемы N+1
var authors = context.Authors.ToList(); // 1 запрос

foreach (var author in authors)
{
    var books = author.Books.ToList(); // N дополнительных запросов
    foreach (var book in books)
    {
        Console.WriteLine(book.Title);
    }
}

// Решение с предварительной загрузкой
var authors = context.Authors
    .Include(a => a.Books)
    .ThenInclude(b => b.Genres)
    .ToList(); // 1 запрос с JOIN

foreach (var author in authors)
{
    foreach (var book in author.Books)
    {
        Console.WriteLine(book.Title);
    }
}
