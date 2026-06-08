class Point {
    public float $x;
    public float $y;

    public function __construct(float $x, float $y) {
        $this->x = $x;
        $this->y = $y;
    }

    public function distanceToOrigin(): float {
        return sqrt($this->x ** 2 + $this->y ** 2);
    }
}

$p = new Point(3.0, 4.0);
