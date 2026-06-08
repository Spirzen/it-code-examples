// Опасный паттерн: синхронное логирование в горячем пути
public class OrderProcessor {
    private static final Logger logger = LoggerFactory.getLogger(OrderProcessor.class);
    
    public OrderResult processOrder(Order order) {
        logger.info("Начало обработки заказа: {}", order.toJson());
        
        // Валидация
        logger.debug("Проверка наличия товаров");
        for (OrderItem item : order.getItems()) {
            logger.debug("Проверка товара {}: {}", item.getSku(), item.getQuantity());
            inventoryService.checkAvailability(item);
        }
        
        // Расчёт стоимости
        logger.debug("Расчёт стоимости");
        PriceCalculation calc = pricingEngine.calculate(order);
        logger.debug("Промежуточный результат: {}", calc.toJson());
        
        // Применение скидок
        logger.debug("Применение скидок");
        DiscountResult discount = discountEngine.apply(order, calc);
        logger.debug("Скидки: {}", discount.toJson());
        
        // Финализация
        OrderResult result = orderRepository.save(order, calc, discount);
        logger.info("Заказ обработан: {}", result.toJson());
        
        return result;
    }
}
