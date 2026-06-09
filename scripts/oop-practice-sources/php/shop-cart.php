<?php

class Product
{
    public function __construct(
        public string $name,
        public int $price
    ) {}
}

class Cart
{
    /** @var list<Product> */
    public array $items = [];

    public function add(Product $product): void
    {
        $this->items[] = $product;
        echo "В корзину добавлено: {$product->name} ({$product->price} ₽)\n";
    }

    public function total(): int
    {
        return array_sum(array_map(fn(Product $p) => $p->price, $this->items));
    }
}

class Order
{
    /** @var list<Product> */
    public array $items;
    public int $total;

    public function __construct(Cart $cart)
    {
        $this->items = $cart->items;
        $this->total = $cart->total();
    }

    public function checkout(): void
    {
        echo "Оформление заказа...\n";
        foreach ($this->items as $item) {
            echo "  — {$item->name}: {$item->price} ₽\n";
        }
        echo "Итого: {$this->total} ₽\n";
        echo "Заказ оформлен!\n";
    }
}

$cart = new Cart();
$cart->add(new Product('Книга', 500));
$cart->add(new Product('Ручка', 50));
$order = new Order($cart);
$order->checkout();
