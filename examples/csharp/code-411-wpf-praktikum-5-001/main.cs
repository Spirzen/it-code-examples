public class TasksApiTests : IClassFixture<WebApplicationFactory<Program>>
{
    private readonly HttpClient _client;

    public TasksApiTests(WebApplicationFactory<Program> factory) =>
        _client = factory.CreateClient();

    [Fact]
    public async Task PostTask_ReturnsCreated()
    {
        var response = await _client.PostAsJsonAsync(
            "/api/v1/tasks",
            new { title = "Test task", status = "Todo" });

        Assert.Equal(HttpStatusCode.Created, response.StatusCode);
        var dto = await response.Content.ReadFromJsonAsync<TaskDto>();
        Assert.NotEqual(Guid.Empty, dto!.Id);
    }

    [Fact]
    public async Task GetTasks_AfterPost_ContainsItem()
    {
        await _client.PostAsJsonAsync("/api/v1/tasks",
            new { title = "Listed", status = "Todo" });

        var list = await _client.GetFromJsonAsync<List<TaskDto>>("/api/v1/tasks");
        Assert.Contains(list!, t => t.Title == "Listed");
    }
}
