// Плохо: все поля доступны напрямую
public class User {
    private String email;
    private String phoneNumber;
    private LocalDate birthDate;
    private String address;
    
    public String getEmail() { return email; }
    public String getPhoneNumber() { return phoneNumber; }
    public LocalDate getBirthDate() { return birthDate; }
    public String getAddress() { return address; }
}

// Хорошо: контролируемый доступ
public class User {
    private final String email;
    private final String phoneNumberHash; // хеш для поиска
    private final LocalDate birthDate;
    private final String address;
    
    // Публичный метод для отображения
    public String getObfuscatedEmail() {
        int atIndex = email.indexOf('@');
        if (atIndex <= 1) return email;
        String prefix = email.substring(0, 2) + "***";
        return prefix + email.substring(atIndex);
    }
    
    // Метод только для аутентифицированных пользователей
    public String getEmailForOwner() {
        return email;
    }
    
    // Возраст вместо даты рождения для внешних сервисов
    public int getAge() {
        return Period.between(birthDate, LocalDate.now()).getYears();
    }
    
    // Полная дата рождения только для внутренних операций
    String getBirthDateInternal() {
        return birthDate.toString();
    }
}
