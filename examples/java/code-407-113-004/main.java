// Java (хороший пример)
public class UserRepository {
    public void save(String userData) {
        // запись в файл
    }
}

public class EmailService {
    public void send(String email, String message) {
        // отправка email
    }
}

public class UserManager {
    private UserRepository repo;
    private EmailService mailer;

    public UserManager(UserRepository repo, EmailService mailer) {
        this.repo = repo;
        this.mailer = mailer;
    }

    public void registerUser(String userData, String email) {
        repo.save(userData);
        mailer.send(email, "Welcome!");
    }
}
