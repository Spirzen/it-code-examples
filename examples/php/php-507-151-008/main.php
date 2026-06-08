session_start();

$errors = [];
$data = $_SESSION['form_data'] ?? [];

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Обновляем данные текущего шага
    $data['step2'] = [
        'phone' => $_POST['phone'] ?? '',
        'address' => $_POST['address'] ?? ''
    ];

    // Валидируем только текущий шаг
    if (empty($data['step2']['phone'])) {
        $errors[] = 'Телефон обязателен';
    }

    if (empty($errors)) {
        $_SESSION['form_data'] = $data;
        header('Location: /step3.php');
        exit;
    }
}
