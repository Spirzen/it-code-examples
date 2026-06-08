from typing import overload, Union

class FlexibleCalculator:
    @overload
    def add(self, a: int, b: int) -> int: ...
    
    @overload
    def add(self, a: str, b: str) -> str: ...
    
    def add(self, a, b):
        return a + b

calc = FlexibleCalculator()
print(calc.add(2, 3))      # 5
print(calc.add("a", "b"))  # ab
