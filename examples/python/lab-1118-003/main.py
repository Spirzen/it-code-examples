from sympy import symbols, Eq, solve, expand, factor

x = symbols("x")

# ax² + bx + c — знаки минус пишем явно
expr = x**2 - 5*x + 6
equation = Eq(expr, 0)

roots = solve(equation, x)

print("Многочлен:", expr)
print("Разложение на множители:", factor(expr))
print("Корни:", roots)

# Проверка каждого корня
for r in roots:
    print(f"  При x = {r} значение многочлена = {expr.subs(x, r)}")
