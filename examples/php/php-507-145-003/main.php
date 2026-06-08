use PHPUnit\Framework\TestCase;

final class MailerTest extends TestCase
{
    public function test_sends_welcome_email(): void
    {
        $mailer = $this->createMock(MailerInterface::class);
        $mailer->expects($this->once())
            ->method('send')
            ->with($this->stringContains('welcome'));

        (new UserService($mailer))->register('a@b.c');
    }
}
