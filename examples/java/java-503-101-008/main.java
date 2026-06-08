// Плохо: метод с большим количеством параметров
public User createUser(String email, String password, String firstName, 
                      String lastName, String phone, String address, 
                      LocalDate birthDate, String nationality) {
    // реализация
}

// Хорошо: объект-параметр
public class UserRegistrationRequest {
    private final String email;
    private final String password;
    private final String firstName;
    private final String lastName;
    private final String phone;
    private final String address;
    private final LocalDate birthDate;
    private final String nationality;
    
    // конструктор, геттеры
}

public User createUser(UserRegistrationRequest request) {
    // реализация
}

// Альтернатива: строитель
public User createUser(UserBuilder builder) {
    // реализация
}

// Использование
User user = createUser(new UserBuilder()
    .withEmail("user@example.com")
    .withPassword("secure123")
    .withFirstName("John")
    // ... остальные параметры
    .build());
