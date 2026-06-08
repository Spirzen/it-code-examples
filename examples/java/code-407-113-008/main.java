// Java (хороший пример)
interface Discount {
    double apply(double amount);
}

class SeasonalDiscount implements Discount {
    public double apply(double amount) {
        return amount * 0.9;
    }
}

class VipDiscount implements Discount {
    public double apply(double amount) {
        return amount * 0.8;
    }
}

public class OrderCalculator {
    public double calculateTotal(List<Item> items, Discount discount) {
        double total = items.stream().mapToDouble(Item::getPrice).sum();
        return discount.apply(total);
    }
}
