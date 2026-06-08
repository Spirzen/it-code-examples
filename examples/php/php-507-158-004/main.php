enum Role: string
{
    case Admin = 'admin';
    case Editor = 'editor';
    case Guest = 'guest';

    public function label(): string
    {
        return match ($this) {
            self::Admin => 'Администратор',
            self::Editor => 'Редактор',
            self::Guest => 'Гость',
        };
    }

    public function canPublish(): bool
    {
        return $this === self::Admin || $this === self::Editor;
    }
}
