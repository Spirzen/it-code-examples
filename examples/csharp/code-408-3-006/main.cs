internal class Класс1 { // C#
    public string имя = "Анна";
}

public class Класс2 { // В другой сборке
    public void использоватьКласс1() {
        Класс1 объект = new Класс1(); // Ошибка: недоступно
    }
}
