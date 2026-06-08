from sympy import symbols, Eq, solve

x = symbols("x")

# Уравнение: левая часть, правая часть
equation = Eq(2*x + 3, 11)

# solve(что_равно_нулю_или_Eq, по_какой_букве)
solution = solve(equation, x)

print("Уравнение:", equation)
print("Список корней:", solution)
print("x =", solution[0])
print("Проверка (подставили x):", equation.subs(x, solution[0]))
