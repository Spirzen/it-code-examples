public class StructuredLogger {
    private final ObjectMapper objectMapper = new ObjectMapper();
    
    public void logOrderEvent(Order order, String eventType) {
        Map<String, Object> logEntry = new HashMap<>();
        logEntry.put("eventType", eventType);
        logEntry.put("timestamp", Instant.now().toString());
        logEntry.put("orderId", order.getId());
        logEntry.put("userId", order.getUserId());
        logEntry.put("totalAmount", order.getTotalAmount());
        logEntry.put("status", order.getStatus());
        
        logger.info(objectMapper.writeValueAsString(logEntry));
    }
}
