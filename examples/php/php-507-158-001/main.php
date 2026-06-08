<?php
declare(strict_types=1);

class Order
{
    public function __construct(
        public readonly string $id,
        public readonly \DateTimeImmutable $createdAt,
        private readonly float $amount,
    ) {}

    public function total(): float
    {
        return $this->amount;
    }
}

$order = new Order('ord-1', new \DateTimeImmutable(), 99.5);
// $order->id = 'x';  // Error: Cannot modify readonly property
