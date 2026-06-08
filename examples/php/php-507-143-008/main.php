class PaymentManager
{
    protected $strategies = [];

    public function addStrategy($name, PaymentStrategy $strategy)
    {
        $this->strategies[$name] = $strategy;
    }

    public function execute($name, $amount)
    {
        if (isset($this->strategies[$name])) {
            return $this->strategies[$name]->pay($amount);
        }
        throw new Exception('Strategy not found');
    }
}
