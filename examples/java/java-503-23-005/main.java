public class HeapExample {
    public static void main(String[] args) {
        // Объект String размещается в куче
        String name = new String("Java");
        
        // Массив объектов размещается в куче
        Person[] people = new Person[10];
        for (int i = 0; i < people.length; i++) {
            people[i] = new Person("Person " + i);
        }
        
        // После выхода из метода объекты становятся кандидатами на GC
    }
    
    static class Person {
        String name;
        int age;
        
        Person(String name) {
            this.name = name;
            this.age = 30;
        }
    }
}
