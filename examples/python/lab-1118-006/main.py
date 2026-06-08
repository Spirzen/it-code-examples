from sympy import symbols, diff, solve, Eq

x = symbols("x")

f = x**3 - 3*x**2 + 2
f1 = diff(f, x)
f2 = diff(f, x, 2)

critical = solve(Eq(f1, 0), x)

print("f'(x) =", f1)
print("f'(x) = 0 при x =", critical)
print()
for c in critical:
    val_f2 = f2.subs(x, c)
    kind = "минимум?" if val_f2 > 0 else ("максимум?" if val_f2 < 0 else "нужен доп. тест")
    print(f"  x = {c}, f'' = {val_f2} → {kind}")
