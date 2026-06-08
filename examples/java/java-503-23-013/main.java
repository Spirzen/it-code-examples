public class ObjectLifecycle {
    public static void main(String[] args) {
        // Этап 1: Загрузка класса Person (происходит при первом использовании)
        
        // Этап 2: Создание объекта
        Person p = new Person("John", 25);
        // - выделение памяти в Eden
        // - заполнение полей значениями по умолчанию
        // - вызов конструктора родительского класса (Object)
        // - выполнение инициализаторов полей
        // - выполнение тела конструктора
        
        // Этап 3: Использование
        p.setName("Jonathan");
        System.out.println(p.getName());
        
        // Создание второй ссылки на тот же объект
        Person p2 = p;
        
        // Этап 4: Объект остаётся достижимым через p2
        p = null;
        
        // Объект становится недостижимым только после обнуления всех ссылок
        p2 = null;
        
        // Этап 5: Сборка мусора (время не определено)
        System.gc(); // рекомендация JVM, не команда
        
        // Объект с финализацией проходит дополнительный этап
        Resource resource = new Resource();
        resource = null;
        // finalize() вызывается в отдельном потоке перед удалением
    }
    
    static class Resource {
        private byte[] data = new byte[1024 * 1024];
        
        @Override
        protected void finalize() throws Throwable {
            System.out.println("Ресурс освобождён");
            super.finalize();
        }
    }
}
