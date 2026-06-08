class Order
{
    public function __construct(
        private readonly int $id,
        private string $status,
        private ?DateTimeImmutable $shippedAt = null
    ) {}

    public function setStatus(string $status): self
    {
        $this->status = $status;
        return $this;
    }
}
