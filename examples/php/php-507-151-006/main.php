$errors = [];
$data = [
    'email' => '',
    'message' => ''
];

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $data['email'] = $_POST['email'] ?? '';
    $data['message'] = $_POST['message'] ?? '';

    if (empty($data['email'])) {
        $errors[] = 'Email обязателен';
    } elseif (!filter_var($data['email'], FILTER_VALIDATE_EMAIL)) {
        $errors[] = 'Некорректный email';
    }

    if (empty($data['message'])) {
        $errors[] = 'Сообщение не может быть пустым';
    }

    if (empty($errors)) {
        // Обработка успешной отправки
        echo "Спасибо! Ваше сообщение отправлено.";
        exit;
    }
}
