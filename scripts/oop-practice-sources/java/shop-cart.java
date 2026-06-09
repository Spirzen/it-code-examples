import java.util.ArrayList;

class Product {
    String name;
    int price;

    Product(String name, int price) {
        this.name = name;
        this.price = price;
    }
}

class Cart {
    ArrayList<Product> items = new ArrayList<>();

    void add(Product product) {
        items.add(product);
        System.out.println("В корзину добавлено: " + product.name + " (" + product.price + " ₽)");
    }

    int total() {
        int sum = 0;
        for (Product p : items) sum += p.price;
        return sum;
    }
}

class Order {
    ArrayList<Product> items;
    int total;

    Order(Cart cart) {
        this.items = new ArrayList<>(cart.items);
        this.total = cart.total();
    }

    void checkout() {
        System.out.println("Оформление заказа...");
        for (Product item : items) {
            System.out.println("  — " + item.name + ": " + item.price + " ₽");
        }
        System.out.println("Итого: " + total + " ₽");
        System.out.println("Заказ оформлен!");
    }
}

public class Main {
    public static void main(String[] args) {
        Cart cart = new Cart();
        cart.add(new Product("Книга", 500));
        cart.add(new Product("Ручка", 50));
        Order order = new Order(cart);
        order.checkout();
    }
}
