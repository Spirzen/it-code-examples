public class OrderCalculator
{
    public decimal CalculateTotal(Order order, Customer customer)
    {
        decimal baseAmount = order.Items.Sum(item => item.Price * item.Quantity);
        
        decimal promoDiscount = ApplyPromoCodeDiscount(baseAmount, order.PromoCode);
        decimal volumeDiscount = ApplyVolumeDiscount(baseAmount - promoDiscount, order.TotalItems);
        decimal loyaltyDiscount = ApplyLoyaltyDiscount(baseAmount - promoDiscount - volumeDiscount, customer.LoyaltyLevel);
        
        decimal subtotal = baseAmount - promoDiscount - volumeDiscount - loyaltyDiscount;
        decimal shippingCost = CalculateShippingCost(order.DeliveryAddress, order.TotalWeight, subtotal);
        decimal tax = CalculateTax(subtotal + shippingCost, order.DeliveryAddress.Region);
        
        return subtotal + shippingCost + tax;
    }
}
