// Определяем язык из URL, cookie или Accept-Language
$lang = $_COOKIE['lang'] ?? 'ru';

// Загружаем переводы
$translations = [
    'ru' => [
        'email_label' => 'Электронная почта',
        'submit' => 'Отправить',
        'email_required' => 'Поле email обязательно'
    ],
    'en' => [
        'email_label' => 'Email',
        'submit' => 'Submit',
        'email_required' => 'Email is required'
    ]
];

$t = $translations[$lang] ?? $translations['ru'];
