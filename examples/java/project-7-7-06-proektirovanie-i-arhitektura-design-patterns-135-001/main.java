interface EmailSender {
    void send(String to, String message);
}

interface SmsSender {
    void send(String phone, String message);
}

interface NotificationFactory {
    EmailSender createEmailSender();
    SmsSender createSmsSender();
}

class AwsEmailSender implements EmailSender {
    @Override
    public void send(String to, String message) {
        System.out.println("AWS SES -> " + to);
    }
}

class AwsSmsSender implements SmsSender {
    @Override
    public void send(String phone, String message) {
        System.out.println("AWS SNS -> " + phone);
    }
}

class AwsNotificationFactory implements NotificationFactory {
    @Override
    public EmailSender createEmailSender() {
        return new AwsEmailSender();
    }

    @Override
    public SmsSender createSmsSender() {
        return new AwsSmsSender();
    }
}
