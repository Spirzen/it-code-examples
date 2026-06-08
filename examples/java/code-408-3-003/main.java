public class Класс1 {
    public string имя = "Анна";
}

public class Класс2 {
    public void использоватьКласс1() {
        Класс1 объект = new Класс1();
        вывод(объект.имя); // Выведет: Анна
    }
}
