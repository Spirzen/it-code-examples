public class Order {
    private final String id;
    private BigDecimal total;

    public Order(String id) {
        this.id = id;
        this.total = BigDecimal.ZERO;
    }

    public void addItem(BigDecimal price) {
        total = total.add(price);
    }
}
