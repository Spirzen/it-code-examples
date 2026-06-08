class Order extends Model
{
    protected $state;

    public function setState(OrderState $state)
    {
        $this->state = $state;
        $this->status = get_class($state);
        $this->save();
    }

    public function pay()
    {
        $this->state->pay($this);
    }
}
