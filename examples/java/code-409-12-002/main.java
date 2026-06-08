@Service
public class UserService {
    private final EmailService emailService;

    public UserService(EmailService emailService) { // DI через конструктор
        this.emailService = emailService;
    }
}
