// Не нужно
public interface IOrderRepository { Task<Order> GetByIdAsync(int id); }

// Вместо этого — DbContext как Unit of Work, DbSet как Repository
public class OrderService
{
    private readonly AppDbContext _db;
    public OrderService(AppDbContext db) => _db = db;

    public async Task<Order> GetOrderWithItemsAsync(int id)
    {
        return await _db.Orders
            .Include(o => o.Items)
            .FirstOrDefaultAsync(o => o.Id == id);
    }
}
