class Person {
    String name;
    
    void greet() {
        System.out.println("Привет, я " + this.name);
        // this указывает на КОНКРЕТНЫЙ объект, который вызвал метод
    }
}

Person p1 = new Person();
p1.name = "Анна";
Person p2 = new Person();
p2.name = "Борис";

p1.greet(); // Выведет: Привет, я Анна (this ссылается на p1)
p2.greet(); // Выведет: Привет, я Борис (this ссылается на p2)
