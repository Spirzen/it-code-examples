<?php
declare(strict_types=1);
?>
<!DOCTYPE html>
<html lang="ru">
<head><meta charset="utf-8"><title>Подписка</title></head>
<body>
  <h1>Подписка на рассылку</h1>
  <?php if (!empty($_GET['error'])): ?>
    <p role="alert">Проверьте поля и попробуйте снова.</p>
  <?php endif; ?>
  <form action="register_submit.php" method="post">
    <label>Имя <input name="name" required maxlength="100"></label>
    <label>Email <input name="email" type="email" required maxlength="255"></label>
    <button type="submit">Подписаться</button>
  </form>
</body>
</html>
