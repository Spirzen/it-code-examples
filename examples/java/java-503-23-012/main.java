public class GCLifecycle {
    public static void main(String[] args) {
        // Этап 1: Создание
        Person person = new Person("Alice", 30);
        
        // Этап 2: Использование
        System.out.println(person.getName());
        person.setAge(31);
        
        // Этап 3: Объект становится недостижимым
        person = null;
        
        // Этап 4: Запрос сборки мусора (не гарантирует немедленное выполнение)
        System.gc();
        
        // Финализация (устаревший механизм)
        Person finalizable = new PersonWithFinalize("Bob", 25);
        finalizable = null;
        System.gc(); // вызовет finalize() перед удалением
    }
    
    static class Person {
        private String name;
        private int age;
        
        Person(String name, int age) {
            this.name = name;
            this.age = age;
        }
        
        String getName() { return name; }
        void setAge(int age) { this.age = age; }
    }
    
    static class PersonWithFinalize extends Person {
        PersonWithFinalize(String name, int age) {
            super(name, age);
        }
        
        @Override
        protected void finalize() throws Throwable {
            System.out.println("Финализация объекта " + getName());
            super.finalize();
        }
    }
}
