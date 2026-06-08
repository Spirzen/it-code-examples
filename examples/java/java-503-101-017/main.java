public BigDecimal calculateTax(Order order) {
    // Базовая ставка налога зависит от типа товара
    BigDecimal baseRate = getBaseTaxRate(order.getProductType());
    
    // Для товаров первой необходимости применяется пониженная ставка
    if (isEssentialGood(order.getProductType())) {
        baseRate = baseRate.multiply(ESSENTIAL_GOODS_DISCOUNT);
    }
    
    // Региональные надбавки применяются только для физических лиц
    if (order.getCustomerType() == CustomerType.INDIVIDUAL) {
        BigDecimal regionalSurcharge = getRegionalSurcharge(order.getRegion());
        baseRate = baseRate.add(regionalSurcharge);
    }
    
    // Максимальная ставка налога ограничена законодательством
    if (baseRate.compareTo(MAX_TAX_RATE) > 0) {
        baseRate = MAX_TAX_RATE;
    }
    
    return order.getTotalAmount().multiply(baseRate);
}
