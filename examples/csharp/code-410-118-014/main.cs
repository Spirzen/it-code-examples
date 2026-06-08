// Пример оптимизации запросов
public async Task GetPopularProductsAsync()
{
    // Неоптимизированный запрос
    var products = await _context.Products
        .Include(p => p.Reviews)
        .ThenInclude(r => r.User)
        .Where(p => p.SalesCount > 100)
        .OrderByDescending(p => p.SalesCount)
        .Take(10)
        .ToListAsync();
    
    // Оптимизированный запрос с проекцией
    var productIds = await _context.Products
        .Where(p => p.SalesCount > 100)
        .Select(p => p.Id)
        .Take(10)
        .ToListAsync();
        
    var products = await _context.Products
        .Where(p => productIds.Contains(p.Id))
        .Include(p => p.Reviews)
        .ToListAsync();
}

// Добавление индекса в модель
[Index(nameof(SalesCount))]
public class Product
{
    public int Id { get; set; }
    public string Name { get; set; }
    public int SalesCount { get; set; }
}
