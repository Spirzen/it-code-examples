class A {
    private Service service;
    
    A(Service service) {  // Зависимость через интерфейс
        this.service = service;
    }
}
