using Grpc.Net.Client;
using UserService;

var channel = GrpcChannel.ForAddress("https://localhost:5001");
var client = new UserService.UserServiceClient(channel);

// Получение пользователя
var user = await client.GetUserAsync(new UserRequest { UserId = 1 });
Console.WriteLine($"User: {user.Name}, Email: {user.Email}");

// Создание пользователя
var newUser = await client.CreateUserAsync(new UserResponse
{
    Name = "Тимур",
    Email = "timur@example.com",
    IsActive = true
});
Console.WriteLine($"Created user ID: {newUser.UserId}");
