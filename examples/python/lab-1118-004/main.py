from sympy import symbols, Eq, solve, discriminant, sqrt

x = symbols("x")

a, b, c = 1, -4, 3
expr = a*x**2 + b*x + c

D = discriminant(expr, x)
roots = solve(Eq(expr, 0), x)

print("Уравнение:", Eq(expr, 0))
print("D =", D)
print("√D =", sqrt(D))
print("Корни:", roots)
