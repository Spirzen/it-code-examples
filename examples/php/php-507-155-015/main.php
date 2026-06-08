<?php
declare(strict_types=1);

final class SessionGuard
{
    public static function start(): void
    {
        if (session_status() === PHP_SESSION_NONE) {
            session_start();
        }
    }

    public static function requireAuth(): void
    {
        self::start();
        if (($_SESSION["logged_in"] ?? false) !== true) {
            header("Location: /auth/login.php");
            exit;
        }
    }
}
