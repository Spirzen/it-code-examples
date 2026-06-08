public sealed class TaskItem
{
    public Guid Id { get; }
    public string Title { get; private set; }
    public bool IsCompleted { get; private set; }

    public TaskItem(Guid id, string title)
    {
        if (string.IsNullOrWhiteSpace(title))
            throw new DomainException("Заголовок задачи обязателен.");
        Id = id;
        Title = title.Trim();
    }

    public void Complete()
    {
        if (IsCompleted) return;
        IsCompleted = true;
    }
}
