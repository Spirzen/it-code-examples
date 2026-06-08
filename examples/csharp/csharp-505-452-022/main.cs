[Fact]
public async Task TimingMiddleware_AddsHeader()
{
    // Arrange
    var builder = WebApplication.CreateBuilder();
    var app = builder.Build();
    app.UseMiddleware<TimingMiddleware>();
    app.Run(ctx => ctx.Response.WriteAsync("OK"));

    using var server = new TestServer(app);
    var client = server.CreateClient();

    // Act
    var response = await client.GetAsync("/");

    // Assert
    Assert.True(response.Headers.Contains("X-Elapsed"));
}
