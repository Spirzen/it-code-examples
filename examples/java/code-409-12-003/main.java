interface EmailService {
    void send(String msg);
}

class SmtpEmailService implements EmailService { ... }
class MockEmailService implements EmailService { ... } // для тестов

class UserService {
    private EmailService emailService;

    public UserService(EmailService emailService) { // DI
        this.emailService = emailService;
    }

    public void register(User user) {
        // ... логика
        emailService.send("Welcome!");
    }
}
