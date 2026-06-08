from sympy import symbols, Eq, solve

def solve_and_print(equation, variable):
    """equation — Eq(..); variable — символ, например x."""
    roots = solve(equation, variable)
    print("Уравнение:", equation)
    print("Корни:", roots)
    for r in roots:
        left = equation.lhs.subs(variable, r)
        right = equation.rhs.subs(variable, r)
        print(f"  x = {r}: {left} = {right} ?", left == right)

x = symbols("x")
solve_and_print(Eq(x**2 - 9, 0), x)
