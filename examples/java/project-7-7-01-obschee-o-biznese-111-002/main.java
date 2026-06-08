public class OrderCalculator {
    public BigDecimal calculateTotal(Order order, Customer customer) {
        BigDecimal baseAmount = order.getItems().stream()
            .map(item -> item.getPrice().multiply(BigDecimal.valueOf(item.getQuantity())))
            .reduce(BigDecimal.ZERO, BigDecimal::add);
        
        BigDecimal promoDiscount = applyPromoCodeDiscount(baseAmount, order.getPromoCode());
        BigDecimal volumeDiscount = applyVolumeDiscount(baseAmount.subtract(promoDiscount), order.getTotalItems());
        BigDecimal loyaltyDiscount = applyLoyaltyDiscount(
            baseAmount.subtract(promoDiscount).subtract(volumeDiscount), 
            customer.getLoyaltyLevel()
        );
        
        BigDecimal subtotal = baseAmount.subtract(promoDiscount)
                                        .subtract(volumeDiscount)
                                        .subtract(loyaltyDiscount);
        BigDecimal shippingCost = calculateShippingCost(order.getDeliveryAddress(), order.getTotalWeight(), subtotal);
        BigDecimal tax = calculateTax(subtotal.add(shippingCost), order.getDeliveryAddress().getRegion());
        
        return subtotal.add(shippingCost).add(tax);
    }
}
