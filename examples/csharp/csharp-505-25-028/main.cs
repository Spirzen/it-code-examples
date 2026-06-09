class User
{
    private readonly string username;
    private readonly string password;
    private bool loggedIn;

    public User(string username, string password)
    {
        this.username = username;
        this.password = password;
        loggedIn = false;
    }

    public void Login(string password)
    {
        if (password == this.password)
        {
            loggedIn = true;
            Console.WriteLine($"Добро пожаловать, {username}!");
        }
        else
        {
            Console.WriteLine("Ошибка: неверный пароль");
        }
    }

    public void Logout()
    {
        loggedIn = false;
        Console.WriteLine($"{username} вышел из системы");
    }

    public void PostMessage(string text)
    {
        if (!loggedIn)
        {
            Console.WriteLine("Сначала войдите в систему");
            return;
        }
        Console.WriteLine($"Сообщение опубликовано: {text}");
    }
}

class Program
{
    static void Main()
    {
        var user = new User("alex", "secret123");
        user.PostMessage("Привет!");
        user.Login("wrong");
        user.Login("secret123");
        user.PostMessage("Привет, мир!");
        user.Logout();
        user.PostMessage("Ещё одно сообщение");
    }
}
