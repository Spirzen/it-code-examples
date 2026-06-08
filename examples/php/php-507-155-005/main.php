<?php
function isLoggedIn(): bool {
    return isset($_SESSION['logged_in']) && $_SESSION['logged_in'] === true;
}

function requireLogin() {
    if (!isLoggedIn()) {
        header("Location: /auth/login.php");
        exit;
    }
}

function getUserRole(): string {
    return $_SESSION['role'] ?? 'guest';
}

function hasRole(string $requiredRole): bool {
    $userRole = getUserRole();
    $roles = ['guest' => 0, 'user' => 1, 'moderator' => 2, 'admin' => 3];
    return ($roles[$userRole] ?? -1) >= ($roles[$requiredRole] ?? -1);
}

function requireRole(string $role) {
    if (!hasRole($role)) {
        http_response_code(403);
        die("Доступ запрещён");
    }
}
?>
