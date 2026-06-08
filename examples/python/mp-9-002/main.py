from ortools.linear_solver import pywraplp

solver = pywraplp.Solver.CreateSolver("GLOP")
x1 = solver.NumVar(0, solver.infinity(), "x1")
x2 = solver.NumVar(0, solver.infinity(), "x2")
solver.Add(2 * x1 + x2 <= 8)
solver.Add(x1 + 2 * x2 <= 8)
solver.Maximize(3 * x1 + 2 * x2)
status = solver.Solve()
if status == pywraplp.Solver.OPTIMAL:
    print(x1.solution_value(), x2.solution_value(), solver.Objective().Value())
