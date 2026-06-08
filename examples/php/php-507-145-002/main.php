/**
 * @dataProvider additionProvider
 */
public function test_addition_provider(int $a, int $b, int $expected): void
{
    $this->assertSame($expected, (new Calculator())->add($a, $b));
}

public static function additionProvider(): array
{
    return [
        'нули' => [0, 0, 0],
        'отрицательное и положительное' => [-1, 1, 0],
        'большие числа' => [100, 200, 300],
    ];
}
