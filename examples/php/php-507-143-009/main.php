class SendShipmentNotification
{
    public function handle($event)
    {
        $event->order->user->notify(new ShipmentStatus($event->order));
    }
}

class UpdateInventory
{
    public function handle($event)
    {
        $event->order->items->each(function ($item) {
            $item->decrement('quantity');
        });
    }
}
