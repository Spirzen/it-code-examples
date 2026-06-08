class NotificationService
{
    protected $mailer;

    public function __construct(Mailer $mailer)
    {
        $this->mailer = $mailer;
    }

    public function send($user, $message)
    {
        $this->mailer->send($user->email, $message);
    }
}
