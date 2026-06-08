// Временный отладочный лог, забытый в продакшене
public class PaymentGateway {
    private static final Logger logger = LoggerFactory.getLogger(PaymentGateway.class);
    
    public PaymentResult processPayment(PaymentRequest request) {
        // TODO: удалить после расследования инцидента INC-4521
        logger.info("DEBUG PAYMENT REQUEST: {}", objectMapper.writeValueAsString(request));
        
        String rawResponse = httpClient.post(paymentUrl, request.toXml());
        
        // TODO: удалить после расследования инцидента INC-4521
        logger.info("DEBUG PAYMENT RESPONSE: {}", rawResponse);
        logger.info("DEBUG PAYMENT HEADERS: {}", lastResponseHeaders);
        
        return parseResponse(rawResponse);
    }
}
