package com.example

import spock.lang.Specification
import spock.lang.Unroll

class CalcSpec extends Specification {

    def calc = new Calc()

    def "сложение двух чисел"() {
        given:
        def a = 2
        def b = 3

        when:
        def result = calc.add(a, b)

        then:
        result == 5
    }

    @Unroll
    def "деление #a / #b = #expected"() {
        expect:
        calc.divide(a, b) == expected

        where:
        a | b | expected
        10| 2 | 5
        9 | 3 | 3
    }

    def "деление на ноль бросает исключение"() {
        when:
        calc.divide(1, 0)

        then:
        thrown(ArithmeticException)
    }
}
