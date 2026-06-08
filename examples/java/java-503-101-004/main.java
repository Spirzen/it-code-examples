// Плохо: нарушение инкапсуляции
public class User {
    public String email; // публичное поле
    private String password;
    
    public String getPassword() { // прямой доступ к чувствительному полю
        return password;
    }
}

// Хорошо: контролируемый доступ
public class User {
    private final String email;
    private String passwordHash;
    
    public User(String email, String password) {
        validateEmail(email);
        this.email = email.toLowerCase().trim();
        this.passwordHash = hashPassword(password);
    }
    
    public String getEmail() {
        return email;
    }
    
    public boolean verifyPassword(String password) {
        return checkPasswordHash(password, passwordHash);
    }
    
    // Нет сеттера для пароля — изменение происходит через отдельный метод
    public void changePassword(String oldPassword, String newPassword) {
        if (!verifyPassword(oldPassword)) {
            throw new SecurityException("Invalid current password");
        }
        this.passwordHash = hashPassword(newPassword);
    }
}
