<?php
if ($user_logged_in) {
?>
  <p>Добро пожаловать, <?= htmlspecialchars($username) ?>!</p>
<?php
} else {
?>
  <form action="login.php" method="post">
    <input type="text" name="login">
    <input type="password" name="pass">
    <input type="submit">
  </form>
<?php
}
?>
