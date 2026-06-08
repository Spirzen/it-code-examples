class Outer {
    private String outerField = "Я из внешнего класса";
    
    class Inner {  // Нестатический вложенный класс
        void show() {
            // Inner автоматически имеет доступ к outerField
            // Он хранит ссылку на конкретный объект Outer
            System.out.println(outerField); 
            // или явно: Outer.this.outerField
        }
    }
}

// Создание:
Outer outer = new Outer();           // Создаём ВНЕШНИЙ объект
Outer.Inner inner = outer.new Inner(); // Создаём ВНУТРЕННИЙ через ВНЕШНИЙ
inner.show(); // Работает, потому что inner знает, какой outer его создал
