[Fact]
public async Task GetUser_ReturnsUser()
{
  var builder = WebApplication.CreateBuilder();
  builder.Services.AddGrpc();
  var app = builder.Build();
  app.MapGrpcService<UserServiceImpl>();
  using var server = app.Services.GetRequiredService<IServer>();
  var channel = GrpcChannel.ForAddress("http://localhost", new GrpcChannelOptions
  {
    HttpClient = new HttpClient(new TestHttpMessageHandler(app))
  });
  var client = new UserService.UserServiceClient(channel);
  var resp = await client.GetUserAsync(new GetUserRequest { UserId = "u1" });
  Assert.Equal("u1", resp.User.Id);
}
