public interface ITaskRepository
{
    Task AddAsync(TaskItem task, CancellationToken ct = default);
}

public sealed class CreateTaskUseCase
{
    private readonly ITaskRepository _repo;
    public CreateTaskUseCase(ITaskRepository repo) => _repo = repo;

    public async Task<Guid> ExecuteAsync(string title, CancellationToken ct = default)
    {
        var task = new TaskItem(Guid.NewGuid(), title);
        await _repo.AddAsync(task, ct);
        return task.Id;
    }
}
