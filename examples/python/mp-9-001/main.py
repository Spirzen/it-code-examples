from scipy.optimize import linprog

# min -Z  =>  c = [-3, -2]
c = [-3, -2]
A_ub = [
    [2, 1],
    [1, 2],
]
b_ub = [8, 8]
bounds = [(0, None), (0, None)]

res = linprog(c, A_ub=A_ub, b_ub=b_ub, bounds=bounds, method="highs")

if res.success:
    x1, x2 = res.x
    z = -res.fun  # вернули max
    print(x1, x2, z)  # ожидаем ~2.666..., 2.666..., 13.333...
else:
    print(res.message)
