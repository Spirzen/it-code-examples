class Shape {
    public function getArea(): float {
        return 0.0;
    }
}

class Rectangle extends Shape {
    private float $width;
    private float $height;

    public function __construct(float $width, float $height) {
        $this->width = $width;
        $this->height = $height;
    }

    // Ковариантность: float → float (допустимо, тип не сужен)
    public function getArea(): float {
        return $this->width * $this->height;
    }
}
