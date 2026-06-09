<?php

class User
{
    private bool $loggedIn = false;

    public function __construct(
        private string $username,
        private string $password
    ) {}

    public function login(string $password): void
    {
        if ($password === $this->password) {
            $this->loggedIn = true;
            echo "Добро пожаловать, {$this->username}!\n";
        } else {
            echo "Ошибка: неверный пароль\n";
        }
    }

    public function logout(): void
    {
        $this->loggedIn = false;
        echo "{$this->username} вышел из системы\n";
    }

    public function postMessage(string $text): void
    {
        if (!$this->loggedIn) {
            echo "Сначала войдите в систему\n";
            return;
        }
        echo "Сообщение опубликовано: {$text}\n";
    }
}

$user = new User('alex', 'secret123');
$user->postMessage('Привет!');
$user->login('wrong');
$user->login('secret123');
$user->postMessage('Привет, мир!');
$user->logout();
$user->postMessage('Ещё одно сообщение');
