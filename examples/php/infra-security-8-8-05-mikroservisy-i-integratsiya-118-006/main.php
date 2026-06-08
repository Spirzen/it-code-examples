require_once __DIR__ . '/vendor/autoload.php';
use PhpAmqpLib\Connection\AMQPStreamConnection;
use PhpAmqpLib\Message\AMQPMessage;
$connection = new AMQPStreamConnection('localhost', 5672, 'guest', 'guest');
$channel = $connection->channel();
// Создание очереди
$channel->queue_declare('my_queue', false, false, false, false);
// Отправка сообщения
$msg = new AMQPMessage('Hello, RabbitMQ!');
$channel->basic_publish($msg, '', 'my_queue');
echo "Message sent\n";
$channel->close();
$connection->close();

