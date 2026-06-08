<?php
$q = trim($_GET['q'] ?? '');
if (empty($q)) {
    die('Введите поисковый запрос.');
}

// Пример простого поиска по массиву (в реальности — по БД)
$pages = [
    ['title' => 'Главная', 'content' => 'Добро пожаловать на сайт'],
    ['title' => 'О нас', 'content' => 'Мы занимаемся разработкой'],
    ['title' => 'Контакты', 'content' => 'Напишите нам']
];

$results = array_filter($pages, fn($page) =>
    stripos($page['title'], $q) !== false ||
    stripos($page['content'], $q) !== false
);
?>

<h2>Результаты поиска по запросу: "<?= htmlspecialchars($q) ?>"</h2>
<?php if (count($results)): ?>
  <ul>
    <?php foreach ($results as $page): ?>
      <li><strong><?= htmlspecialchars($page['title']) ?></strong>: <?= htmlspecialchars($page['content']) ?></li>
    <?php endforeach; ?>
  </ul>
<?php else: ?>
  <p>Ничего не найдено.</p>
<?php endif; ?>
