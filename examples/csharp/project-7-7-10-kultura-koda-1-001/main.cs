/// <summary>
/// Модель пользователя в системе.
/// </summary>
public class User
{
    /// <summary>
    /// Создаёт пользователя с указанным именем и возрастом.
    /// </summary>
    /// <param name="name">Отображаемое имя.</param>
    /// <param name="age">Возраст в полных годах.</param>
    public User(string name, int age)
    {
        Name = name;
        Age = age;
    }

    /// <summary>
    /// Проверяет, достиг ли пользователь 18 лет.
    /// </summary>
    /// <returns><c>true</c>, если возраст ≥ 18.</returns>
    public bool IsAdult() => Age >= 18;

    public string Name { get; set; }
    public int Age { get; private set; }
}
