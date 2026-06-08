package com.example.demo;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;

import static org.junit.jupiter.api.Assertions.*;

class CalculatorTest {

    private final Calculator calc = new Calculator();

    @Test
    @DisplayName("сложение двух чисел")
    void adds() {
        assertEquals(5, calc.add(2, 3));
    }

    @ParameterizedTest
    @CsvSource({
        "0, 0, 0",
        "1, 2, 3",
        "-1, 1, 0"
    })
    void addsParameterized(int a, int b, int expected) {
        assertEquals(expected, calc.add(a, b));
    }

    @Test
    void throwsOnOverflow() {
        assertThrows(ArithmeticException.class, () -> calc.divide(1, 0));
    }
}
