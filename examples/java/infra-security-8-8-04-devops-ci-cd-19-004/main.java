public class OrderProcessor {
    private static final Logger logger = LoggerFactory.getLogger(OrderProcessor.class);
    private static final Logger detailedLogger = LoggerFactory.getLogger("orders.detailed");
    
    public OrderResult processOrder(Order order) {
        long startTime = System.nanoTime();
        String traceId = MDC.get("traceId");
        
        try {
            OrderResult result = doProcessOrder(order);
            long durationMs = (System.nanoTime() - startTime) / 1_000_000;
            
            // Базовый лог всегда
            logger.info("Заказ {} обработан за {} мс", order.getId(), durationMs);
            
            // Подробный лог только для медленных заказов
            if (durationMs > SLOW_ORDER_THRESHOLD_MS) {
                detailedLogger.warn(
                    "Медленный заказ: id={}, duration={}ms, items={}, total={}",
                    order.getId(), durationMs,
                    order.getItems().size(), result.getTotalAmount()
                );
            }
            
            return result;
        } catch (Exception e) {
            // Полный контекст только при ошибках
            detailedLogger.error(
                "Ошибка обработки заказа: id={}, error={}, order={}",
                order.getId(), e.getMessage(), order.toJson(),
                e
            );
            throw e;
        }
    }
}
