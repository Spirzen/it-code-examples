import pandas as pd

df = pd.DataFrame({
    "dept": ["IT", "HR", "IT", "Sales", "IT", "HR"],
    "name": ["Аня", "Боря", "Вера", "Глеб", "Дина", "Егор"],
    "salary": [120000, 90000, 130000, 110000, 125000, 85000],
})

result = (
    df.query("salary >= 90000")
    .groupby("dept", as_index=False)
    .agg(avg_salary=("salary", "mean"), headcount=("name", "count"))
    .sort_values("avg_salary", ascending=False)
)

print(result)
