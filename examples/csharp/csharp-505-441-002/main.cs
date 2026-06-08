using BooksEf.Data;
using BooksEf.Models;

using var db = new AppDbContext();

// Create
db.Books.Add(new Book { Title = "Clean Code", Year = 2008 });
db.Books.Add(new Book { Title = "CLR via C#", Year = 2012 });
await db.SaveChangesAsync();

// Read
var recent = await db.Books
    .Where(b => b.Year >= 2010)
    .OrderBy(b => b.Title)
    .ToListAsync();

foreach (var b in recent)
    Console.WriteLine($"{b.Id}: {b.Title} ({b.Year})");

// Update
var first = await db.Books.OrderBy(b => b.Id).FirstAsync();
first.Year = 2009;
await db.SaveChangesAsync();

// Delete
var toRemove = await db.Books.FirstAsync(b => b.Title == "CLR via C#");
db.Books.Remove(toRemove);
await db.SaveChangesAsync();
