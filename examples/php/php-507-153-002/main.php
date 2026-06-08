class Email {
    private function __construct(private string $address) {}

    public static function fromString(string $address): self {
        if (!filter_var($address, FILTER_VALIDATE_EMAIL)) {
            throw new InvalidArgumentException('Invalid email');
        }
        return new self($address);
    }

    public function toString(): string {
        return $this->address;
    }
}
