$lang = $_COOKIE['lang'] ?? 'ru';
$labels = [
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
$t = $labels[$lang] ?? $labels['ru'];
