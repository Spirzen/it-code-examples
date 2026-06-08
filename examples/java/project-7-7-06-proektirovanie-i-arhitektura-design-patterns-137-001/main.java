interface NotificationService {
    void send(String userId, String text);
}

class LegacySmsGateway {
    void sendSms(String phone, String body) {
        System.out.println("Legacy SMS -> " + phone + ": " + body);
    }
}

class SmsGatewayAdapter implements NotificationService {
    private final LegacySmsGateway gateway;
    private final UserPhoneResolver resolver;

    SmsGatewayAdapter(LegacySmsGateway gateway, UserPhoneResolver resolver) {
        this.gateway = gateway;
        this.resolver = resolver;
    }

    @Override
    public void send(String userId, String text) {
        String phone = resolver.resolve(userId);
        gateway.sendSms(phone, text);
    }
}

interface UserPhoneResolver {
    String resolve(String userId);
}
