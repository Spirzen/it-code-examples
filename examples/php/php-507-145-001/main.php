<?php

namespace Tests;

use App\Calculator;
use PHPUnit\Framework\TestCase;

final class CalculatorTest extends TestCase
{
    public function test_adds_two_integers(): void
    {
        $calc = new Calculator();
        $this->assertSame(5, $calc->add(2, 3));
    }
}
