class Car {
    // Поля (состояние)
    string brand;
    string model;
    int year;

    // Методы (поведение)
    public void StartEngine() {
        Console.WriteLine("Двигатель запущен");
    }

    public void ShowInfo() {
        Console.WriteLine($"Марка: {brand}, Модель: {model}, Год: {year}");
    }
}
