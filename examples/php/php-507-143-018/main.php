interface OrderState
{
    public function pay(Order $order);
    public function ship(Order $order);
}

class PendingState implements OrderState
{
    public function pay(Order $order)
    {
        $order->setState(new PaidState());
    }

    public function ship(Order $order)
    {
        throw new Exception('Cannot ship unpaid order');
    }
}
