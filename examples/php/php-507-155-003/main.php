function requireRole($requiredRole) {
    session_start();
    if (!isset($_SESSION['logged_in']) || $_SESSION['logged_in'] !== true) {
        header("Location: login.php");
        exit;
    }

    $userRole = $_SESSION['role'] ?? 'guest';

    // Простая иерархия: admin > user > guest
    $roleHierarchy = ['guest' => 0, 'user' => 1, 'admin' => 2];
    if (($roleHierarchy[$userRole] ?? -1) < ($roleHierarchy[$requiredRole] ?? -1)) {
        http_response_code(403);
        die("Доступ запрещён");
    }
}
