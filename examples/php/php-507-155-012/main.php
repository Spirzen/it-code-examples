// test_session_login.php
require_once 'auth.php';

class SessionLoginTest extends \PHPUnit\Framework\TestCase
{
    private $pdo;

    protected function setUp(): void {
        // Используем in-memory SQLite для тестов
        $this->pdo = new PDO('sqlite::memory:');
        // Создание таблиц и тестовых данных
    }

    public function testSuccessfulLoginSetsSession()
    {
        session_start();
        $_POST = ['username' => 'testuser', 'password' => 'correctpass'];

        // Вызов login.php логики (обёрнутой в функцию)
        handleLogin($this->pdo);

        $this->assertTrue($_SESSION['logged_in']);
        $this->assertEquals('testuser', $_SESSION['username']);
    }

    protected function tearDown(): void {
        session_destroy();
    }
}
