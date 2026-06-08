public class OrderValidator {
    private final InventoryService inventory;
    
    public ValidationResult validate(Order order) {
        var errors = new ArrayList<String>();
        
        if (order.getItems().isEmpty()) 
            errors.add("Order must contain at least one item");
        
        for (var item : order.getItems()) {
            var stock = inventory.getStock(item.productId());
            if (stock < item.quantity()) 
                errors.add("Insufficient stock for " + item.productId());
        }
        
        return new ValidationResult(errors.isEmpty(), errors);
    }
}
