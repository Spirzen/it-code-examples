<?php
namespace App\Http\Controller;

use App\Service\Mailer;
use App\Model\User;
use DateTimeImmutable;

class RegisterController
{
    public function __construct(
        private Mailer $mailer,
    ) {}

    public function complete(User $user): void
    {
        $this->mailer->send($user->email, 'Добро пожаловать');
        $at = new DateTimeImmutable();
    }
}
