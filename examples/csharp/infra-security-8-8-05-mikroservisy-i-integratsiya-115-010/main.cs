public class Query
{
    private readonly List<User> _users = new();
    private readonly List<Post> _posts = new();

    public User GetUser(int id) => _users.FirstOrDefault(u => u.Id == id);

    public List<User> GetUsers(int page = 1, int pageSize = 10)
    {
        int skip = (page - 1) * pageSize;
        return _users.Skip(skip).Take(pageSize).ToList();
    }

    public Post GetPost(int id) => _posts.FirstOrDefault(p => p.Id == id);

    public List<Post> GetPosts(int page = 1, int pageSize = 10)
    {
        int skip = (page - 1) * pageSize;
        return _posts.Skip(skip).Take(pageSize).ToList();
    }
}

public class Mutation
{
    private readonly List<User> _users = new();
    private readonly List<Post> _posts = new();

    public User CreateUser(string name, string email, bool isActive = true)
    {
        var user = new User
        {
            Id = _users.Count + 1,
            Name = name,
            Email = email,
            IsActive = isActive,
            CreatedAt = DateTime.UtcNow
        };
        _users.Add(user);
        return user;
    }

    public User UpdateUser(int id, string? name = null, string? email = null, bool? isActive = null)
    {
        var user = _users.FirstOrDefault(u => u.Id == id);
        if (user == null) throw new Exception("User not found");
        
        if (name != null) user.Name = name;
        if (email != null) user.Email = email;
        if (isActive != null) user.IsActive = isActive.Value;
        
        return user;
    }

    public bool DeleteUser(int id)
    {
        var user = _users.FirstOrDefault(u => u.Id == id);
        if (user == null) return false;
        return _users.Remove(user);
    }

    public Post CreatePost(string title, string content, int authorId)
    {
        var author = _users.FirstOrDefault(u => u.Id == authorId);
        if (author == null) throw new Exception("Author not found");
        
        var post = new Post
        {
            Id = _posts.Count + 1,
            Title = title,
            Content = content,
            AuthorId = authorId,
            PublishedAt = DateTime.UtcNow,
            Author = author
        };
        _posts.Add(post);
        return post;
    }
}
