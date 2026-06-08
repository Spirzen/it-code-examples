@ConfigurationProperties(prefix = "app.payment")
@Component
public class PaymentProperties {
    private final Gateway gateway = new Gateway();
    private final Retry retry = new Retry();
    
    public Gateway getGateway() {
        return gateway;
    }
    
    public Retry getRetry() {
        return retry;
    }
    
    public static class Gateway {
        private String url;
        private String apiKey;
        private int connectTimeout = 5000;
        private int readTimeout = 10000;
        
        // геттеры и сеттеры
    }
    
    public static class Retry {
        private int maxAttempts = 3;
        private long initialBackoff = 1000;
        private double backoffMultiplier = 2.0;
        
        // геттеры и сеттеры
    }
}

// Использование
@Service
public class PaymentService {
    private final PaymentProperties properties;
    
    public PaymentService(PaymentProperties properties) {
        this.properties = properties;
    }
    
    public void processPayment(Payment payment) {
        String gatewayUrl = properties.getGateway().getUrl();
        int maxRetries = properties.getRetry().getMaxAttempts();
        // ...
    }
}
