public class UserService {
    private EmailService emailService;

    // Сеттер для внедрения зависимости
    public void setEmailService(EmailService emailService) {
        this.emailService = emailService;
    }

    public void register(User user) {
        emailService.send("Welcome!"); // используем
    }
}
