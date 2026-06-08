interface MessageSender {
    void send(String message, String recipient);
}

class EmailSender implements MessageSender {
    @Override
    public void send(String message, String recipient) {
        System.out.println("Email -> " + recipient + ": " + message);
    }
}

class SmsSender implements MessageSender {
    @Override
    public void send(String message, String recipient) {
        System.out.println("SMS -> " + recipient + ": " + message);
    }
}

abstract class Notification {
    protected final MessageSender sender;

    protected Notification(MessageSender sender) {
        this.sender = sender;
    }

    abstract void notify(String recipient, String message);
}

class UrgentNotification extends Notification {
    UrgentNotification(MessageSender sender) {
        super(sender);
    }

    @Override
    void notify(String recipient, String message) {
        sender.send("[СРОЧНО] " + message, recipient);
        sender.send("[СРОЧНО] Повтор: " + message, recipient);
    }
}

class RegularNotification extends Notification {
    RegularNotification(MessageSender sender) {
        super(sender);
    }

    @Override
    void notify(String recipient, String message) {
        sender.send(message, recipient);
    }
}
