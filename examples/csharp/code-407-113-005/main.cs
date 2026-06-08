// C# (хороший пример)
public class UserRepository
{
    public void Save(string userData)
    {
        File.AppendAllText("users.txt", userData + Environment.NewLine);
    }
}

public class EmailService
{
    public void Send(string email, string message)
    {
        Console.WriteLine($"Sending email to {email}: {message}");
    }
}

public class UserManager
{
    private readonly UserRepository _repo;
    private readonly EmailService _mailer;

    public UserManager(UserRepository repo, EmailService mailer)
    {
        _repo = repo;
        _mailer = mailer;
    }

    public void RegisterUser(string userData, string email)
    {
        _repo.Save(userData);
        _mailer.Send(email, "Welcome!");
    }
}
