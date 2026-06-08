using System.Net.Http.Json;
using Microsoft.AspNetCore.Mvc.Testing;

namespace HelloApi.Tests;

public class NotesEndpointTests : IClassFixture<WebApplicationFactory<Program>>
{
    private readonly HttpClient _client;

    public NotesEndpointTests(WebApplicationFactory<Program> factory)
    {
        _client = factory.CreateClient();
    }

    [Fact]
    public async Task PostNote_ThenGetAll_ContainsNote()
    {
        var create = await _client.PostAsJsonAsync(
            "/api/notes",
            new { Text = "integration test" });

        create.EnsureSuccessStatusCode();

        var notes = await _client.GetFromJsonAsync<List<NoteDto>>("/api/notes");

        Assert.NotNull(notes);
        Assert.Contains(notes, n => n.Text == "integration test");
    }

    private record NoteDto(int Id, string Text);
}
