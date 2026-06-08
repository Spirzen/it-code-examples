
import java.util.*;

public class OrderProcessor {
    public Map<String, Object> processOrder(String orderId) {
        validateOrder(orderId);
        return calculateAndSave(orderId);
    }

    private Map<String, Object> calculateAndSave(String orderId) {
        // реализация
        return Map.of("status", "processed");
    }

    private void validateOrder(String orderId) { /* ... */ }
}
