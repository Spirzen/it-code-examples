from sympy import symbols, Eq, solve, diff

# 1. Объявляем букву (неизвестную)
x = symbols("x")

# 2. Записываем выражение или уравнение
expr = x**2 + 2*x + 1          # многочлен
equation = Eq(expr, 0)         # уравнение «expr = 0»

# 3. Считаем то, что нужно в задаче
roots = solve(equation, x)
proizvodnaya = diff(expr, x)

# 4. Показываем результат (в .py без print экран пустой)
print("Уравнение:", equation)
print("Корни:", roots)
print("Производная:", proizvodnaya)
