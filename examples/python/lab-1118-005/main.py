from sympy import symbols, Eq, solve

x, y = symbols("x y")

system = [
    Eq(x + y, 10),
    Eq(x - y, 2),
]

result = solve(system, x, y)

print("Система:")
for i, eq in enumerate(system, 1):
    print(f"  ({i}) {eq}")
print("Ответ (словарь):", result)
print("x =", result[x], ", y =", result[y])
print("Проверка (1):", system[0].subs(result))
print("Проверка (2):", system[1].subs(result))
