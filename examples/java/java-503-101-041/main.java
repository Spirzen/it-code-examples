public class Order {
    private final OrderId id;
    private final CustomerId customerId;
    private final List<OrderItem> items;
    private OrderStatus status;
    
    public void addItem(Product product, int quantity) {
        validateCanModify();
        items.add(new OrderItem(product.getId(), product.getPrice(), quantity));
    }
    
    public void removeItem(OrderItemId itemId) {
        validateCanModify();
        items.removeIf(item -> item.getId().equals(itemId));
    }
    
    public void submit() {
        validateCanSubmit();
        this.status = OrderStatus.SUBMITTED;
        registerEvent(new OrderSubmittedEvent(id, customerId, calculateTotal()));
    }
    
    private void validateCanModify() {
        if (status != OrderStatus.DRAFT) {
            throw new OrderModificationException("Cannot modify submitted order");
        }
    }
}
