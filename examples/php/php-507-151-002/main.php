try {
    $pdo = new PDO("mysql:host=localhost;dbname=mydb", $user, $pass);
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

    $stmt = $pdo->prepare("INSERT INTO users (email, password) VALUES (?, ?)");
    $stmt->execute([
        $_POST['email'],
        password_hash($_POST['password'], PASSWORD_DEFAULT)
    ]);

    echo "Регистрация успешна!";
} catch (PDOException $e) {
    // Логирование ошибки, но не показ пользователю
    error_log($e->getMessage());
    echo "Произошла ошибка. Попробуйте позже.";
}
