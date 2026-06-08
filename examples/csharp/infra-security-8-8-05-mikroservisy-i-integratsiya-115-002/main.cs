using Grpc.Core;
using UserService;

public class UserServiceImpl : UserService.UserServiceBase
{
    private readonly Dictionary<int, UserResponse> _users = new();

    public override Task<UserResponse> GetUser(
        UserRequest request,
        ServerCallContext context)
    {
        if (_users.TryGetValue(request.UserId, out var user))
            return Task.FromResult(user);
        
        throw new RpcException(
            new Status(StatusCode.NotFound, "User not found"));
    }

    public override Task<UserListResponse> ListUsers(
        UserListRequest request,
        ServerCallContext context)
    {
        var skip = (request.Page - 1) * request.PageSize;
        var users = _users.Values
            .Skip(skip)
            .Take(request.PageSize)
            .ToList();

        return Task.FromResult(new UserListResponse
        {
            Users = { users },
            TotalCount = _users.Count
        });
    }

    public override Task<UserResponse> CreateUser(
        UserResponse request,
        ServerCallContext context)
    {
        var newUser = new UserResponse
        {
            UserId = _users.Count + 1,
            Name = request.Name,
            Email = request.Email,
            IsActive = request.IsActive
        };
        
        _users[newUser.UserId] = newUser;
        return Task.FromResult(newUser);
    }
}

// Запуск сервера
var builder = WebApplication.CreateBuilder(args);
builder.Services.AddGrpc();

var app = builder.Build();
app.MapGrpcService<UserServiceImpl>();
app.Run();
