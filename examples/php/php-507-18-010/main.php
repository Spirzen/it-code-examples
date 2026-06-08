class Base {
    protected static string $name = 'Base';

    public static function who(): string {
        return self::$name;
    }

    public static function who2(): string {
        return static::$name;
    }
}

class Child extends Base {
    protected static string $name = 'Child';
}

echo Base::who();   // → "Base"
echo Child::who();  // → "Base"   (self → Base)
echo Child::who2(); // → "Child"  (static → Child)
