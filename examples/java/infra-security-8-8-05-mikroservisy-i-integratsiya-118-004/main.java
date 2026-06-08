
import com.rabbitmq.client.ConnectionFactory;
import com.rabbitmq.client.Connection;
import com.rabbitmq.client.Channel;

public class RabbitMQExample {
    public static void main(String[] args) throws Exception {
        ConnectionFactory factory = new ConnectionFactory();
        factory.setHost("localhost");
        try (Connection connection = factory.newConnection();
             Channel channel = connection.createChannel()) {
            // Создание очереди
            channel.queueDeclare("my_queue", false, false, false, null);
            // Отправка сообщения
            String message = "Hello, RabbitMQ!";
            channel.basicPublish("", "my_queue", null, message.getBytes());
            System.out.println("Message sent");
        }
    }
}

