public class UserService
{
    private IEmailService _emailService;

    public void SetEmailService(IEmailService emailService) // DI через сеттер
    {
        _emailService = emailService;
    }
}
