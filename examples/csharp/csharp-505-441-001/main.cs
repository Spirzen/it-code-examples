using BooksEf.Models;
using Microsoft.EntityFrameworkCore;

namespace BooksEf.Data;

public class AppDbContext : DbContext
{
    public DbSet<Book> Books => Set<Book>();

    protected override void OnConfiguring(DbContextOptionsBuilder options)
    {
        // Файл books.db появится рядом с exe после миграции
        options.UseSqlite("Data Source=books.db");
    }
}
