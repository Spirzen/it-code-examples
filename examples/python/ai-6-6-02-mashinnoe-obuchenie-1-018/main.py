
import pandas as pd
import numpy as np

# Создаем датафрейм
data = {
    'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'age': [25, 30, 35, 28, 22],
    'salary': [50000, 60000, 75000, 55000, 45000],
    'department': ['IT', 'HR', 'IT', 'Marketing', 'IT']
}

df = pd.DataFrame(data)

# Основные операции
print("Первые 3 строки:")
print(df.head(3))

print("\nОписательная статистика:")
print(df.describe())

print("\nГруппировка по отделам:")
print(df.groupby('department')['salary'].mean())

# Фильтрация
it_employees = df[df['department'] == 'IT']
high_salary = df[df['salary'] > 55000]

# Добавление нового столбца
df['experience'] = [2, 5, 8, 3, 1]

# Сохранение в файл
df.to_csv('employees.csv', index=False)
