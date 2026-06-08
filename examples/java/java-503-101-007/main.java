// Плохо: длинный метод со сложной логикой
public void processOrder(Order order) {
    if (order == null) {
        throw new IllegalArgumentException("Order cannot be null");
    }
    
    if (order.getItems().isEmpty()) {
        throw new OrderValidationException("Order must have items");
    }
    
    BigDecimal total = BigDecimal.ZERO;
    for (OrderItem item : order.getItems()) {
        if (item.getQuantity() <= 0) {
            throw new OrderValidationException("Invalid quantity for item " + item.getId());
        }
        Product product = productRepository.findById(item.getProductId())
            .orElseThrow(() -> new ProductNotFoundException(item.getProductId()));
        if (product.getStock() < item.getQuantity()) {
            throw new InsufficientStockException(product.getId(), product.getStock(), item.getQuantity());
        }
        BigDecimal itemTotal = product.getPrice().multiply(BigDecimal.valueOf(item.getQuantity()));
        total = total.add(itemTotal);
    }
    
    if (order.getDiscountCode() != null) {
        Discount discount = discountRepository.findByCode(order.getDiscountCode());
        if (discount != null && discount.isValid() && total.compareTo(discount.getMinOrderAmount()) >= 0) {
            BigDecimal discountAmount = total.multiply(discount.getPercentage()).divide(BigDecimal.valueOf(100));
            total = total.subtract(discountAmount);
            order.setDiscountAmount(discountAmount);
        }
    }
    
    order.setTotal(total);
    order.setStatus(OrderStatus.PROCESSING);
    orderRepository.save(order);
    
    inventoryService.reserveStock(order.getItems());
    notificationService.sendOrderConfirmation(order.getCustomerEmail(), order.getId());
}

// Хорошо: декомпозированный метод
public void processOrder(Order order) {
    validateOrder(order);
    calculateOrderTotal(order);
    applyDiscountIfApplicable(order);
    updateOrderStatus(order);
    reserveInventory(order);
    sendConfirmation(order);
}

private void validateOrder(Order order) {
    if (order == null) {
        throw new IllegalArgumentException("Order cannot be null");
    }
    if (order.getItems().isEmpty()) {
        throw new OrderValidationException("Order must have items");
    }
    validateOrderItems(order.getItems());
}

private void validateOrderItems(List<OrderItem> items) {
    for (OrderItem item : items) {
        validateOrderItem(item);
        checkProductAvailability(item);
    }
}
// ... остальные методы
