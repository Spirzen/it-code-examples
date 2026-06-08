public interface ITaskStore
{
    IReadOnlyList<TaskItem> GetAll(string? statusFilter);
    TaskItem? GetById(Guid id);
    TaskItem Add(TaskItem item);
    bool Update(TaskItem item);
    bool Delete(Guid id);
}

public sealed class InMemoryTaskStore : ITaskStore
{
    private readonly List<TaskItem> _items = new();
    private readonly object _lock = new();

    public IReadOnlyList<TaskItem> GetAll(string? statusFilter)
    {
        lock (_lock)
        {
            var q = _items.AsEnumerable();
            if (!string.IsNullOrEmpty(statusFilter))
                q = q.Where(t => t.Status.ToString() == statusFilter);
            return q.OrderByDescending(t => t.CreatedAt).ToList();
        }
    }
    // Add, Update, Delete — с lock и Guid
}
