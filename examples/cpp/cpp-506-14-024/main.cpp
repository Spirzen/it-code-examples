#include <iostream>
#include <string>
#include <vector>

class Product {
public:
    std::string name;
    int price;

    Product(const std::string& name, int price) : name(name), price(price) {}
};

class Cart {
public:
    std::vector<Product> items;

    void add(const Product& product) {
        items.push_back(product);
        std::cout << "В корзину добавлено: " << product.name << " (" << product.price << " ₽)" << std::endl;
    }

    int total() const {
        int sum = 0;
        for (const auto& p : items) sum += p.price;
        return sum;
    }
};

class Order {
public:
    std::vector<Product> items;
    int total;

    explicit Order(const Cart& cart) : items(cart.items), total(cart.total()) {}

    void checkout() const {
        std::cout << "Оформление заказа..." << std::endl;
        for (const auto& item : items) {
            std::cout << "  — " << item.name << ": " << item.price << " ₽" << std::endl;
        }
        std::cout << "Итого: " << total << " ₽" << std::endl;
        std::cout << "Заказ оформлен!" << std::endl;
    }
};

int main() {
    Cart cart;
    cart.add(Product("Книга", 500));
    cart.add(Product("Ручка", 50));
    Order order(cart);
    order.checkout();
    return 0;
}
