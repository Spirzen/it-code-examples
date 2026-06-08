interface DiscountStrategy {
    double apply(double amount);
}

class NoDiscountStrategy implements DiscountStrategy {
    @Override
    public double apply(double amount) {
        return amount;
    }
}

class VipDiscountStrategy implements DiscountStrategy {
    @Override
    public double apply(double amount) {
        return amount * 0.85;
    }
}

class CheckoutService {
    private DiscountStrategy strategy;

    CheckoutService(DiscountStrategy strategy) {
        this.strategy = strategy;
    }

    void setStrategy(DiscountStrategy strategy) {
        this.strategy = strategy;
    }

    double total(double amount) {
        return strategy.apply(amount);
    }
}
