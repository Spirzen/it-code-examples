enum Priority: string
{
    case Low = 'low';
    case Normal = 'normal';
    case High = 'high';
}

// Из строки (например, из БД)
$p = Priority::from('high');

// Безопасный разбор
$p = Priority::tryFrom('unknown'); // null, если нет такого значения

echo $p->value; // 'high'
echo $p->name;  // 'High'
