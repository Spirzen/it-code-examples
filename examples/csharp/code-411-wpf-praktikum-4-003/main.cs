public sealed class ApiTaskRepository : ITaskRepository
{
    private readonly HttpClient _http;

    public ApiTaskRepository(HttpClient http) => _http = http;

    public async Task<IReadOnlyList<TaskItem>> GetAllAsync(CancellationToken ct = default)
    {
        var dtos = await _http.GetFromJsonAsync<List<TaskDto>>("api/v1/tasks", ct)
                   ?? new List<TaskDto>();
        return dtos.Select(Map).ToList();
    }

    public async Task<TaskItem> CreateAsync(TaskItem task, CancellationToken ct = default)
    {
        var response = await _http.PostAsJsonAsync(
            "api/v1/tasks",
            new CreateTaskRequest(task.Title, task.Status.ToString()),
            ct);
        response.EnsureSuccessStatusCode();
        var dto = await response.Content.ReadFromJsonAsync<TaskDto>(cancellationToken: ct)
                  ?? throw new InvalidOperationException("Empty body");
        return Map(dto);
    }

    private static TaskItem Map(TaskDto dto) => new()
    {
        Id = dto.Id,
        Title = dto.Title,
        Status = Enum.Parse<TaskStatus>(dto.Status),
        CreatedAt = dto.CreatedAt
    };
}
