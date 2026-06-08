class User implements JsonSerializable {
    public function __construct(
        public int $id,
        public string $name,
        public array $roles
    ) {}

    public function jsonSerialize(): array {
        return [
            'id' => $this->id,
            'name' => $this->name,
            'roles' => $this->roles
        ];
    }
}
