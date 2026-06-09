class Student
{
    public const int PassingScore = 60;
    public string Name { get; }
    public List<int> Grades { get; } = new();

    public Student(string name)
    {
        Name = name;
    }

    public void AddGrade(int grade)
    {
        Grades.Add(grade);
        Console.WriteLine($"Оценка {grade} добавлена для {Name}");
    }

    public double AverageScore()
    {
        return Grades.Count == 0 ? 0 : Grades.Average();
    }

    public bool IsPassing()
    {
        return AverageScore() >= PassingScore;
    }

    public void Info()
    {
        Console.WriteLine($"Студент: {Name}");
        Console.WriteLine($"Оценки: [{string.Join(", ", Grades)}]");
        Console.WriteLine($"Средний балл: {AverageScore():F1}");
        Console.WriteLine(IsPassing() ? "Зачёт получен" : "Зачёт не получен");
    }
}

class Program
{
    static void Main()
    {
        var student = new Student("Анна");
        student.AddGrade(70);
        student.AddGrade(85);
        student.AddGrade(55);
        student.Info();
    }
}
