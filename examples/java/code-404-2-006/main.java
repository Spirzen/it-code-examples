// logger/src/main/java/com/example/logger/Logger.java
package com.example.logger;
public interface Logger {
    void info(String msg);
}
public class ConsoleLogger implements Logger {
    public void info(String msg) {
        System.out.println("[INFO] " + java.time.Instant.now() + " " + msg);
    }
}

// core/src/main/java/com/example/core/Order.java
package com.example.core;
public record Order(int id, String[] items) {}

// core/src/main/java/com/example/core/OrderService.java
package com.example.core;

import com.example.logger.Logger;

public class OrderService {
    private final Logger logger;
    public OrderService(Logger logger) { this.logger = logger; }
    public Order placeOrder(String[] items) {
        var order = new Order(1, items);
        logger.info("Order %d placed with %d items".formatted(order.id(), items.length));
        return order;
    }
}

// notification/src/main/java/com/example/notification/EmailService.java
package com.example.notification;

import com.example.logger.Logger;

public interface EmailService {
    void send(String to, String subject, String body);
}
public class SmtpEmailService implements EmailService {
    private final Logger logger;
    public SmtpEmailService(Logger logger) { this.logger = logger; }
    public void send(String to, String subject, String body) {
        logger.info("Sending email to " + to);
        // ...
    }
}

// app/src/main/java/com/example/app/Main.java
package com.example.app;

import com.example.core.*;
import com.example.logger.*;
import com.example.notification.*;

public class Main {
    public static void main(String[] args) {
        Logger logger = new ConsoleLogger();
        OrderService orderService = new OrderService(logger);
        EmailService emailService = new SmtpEmailService(logger);
        Order order = orderService.placeOrder(new String[]{"book", "pen"});
        emailService.send("user@example.com", "Order confirmed", "ID: " + order.id());
    }
}
