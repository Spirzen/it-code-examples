
import pandas as pd

# Загрузка данных из файла
data = pd.read_csv('titanic.csv')

# Просмотр первых пяти строк
print(data.head())

# Подсчет среднего возраста пассажиров
average_age = data['Age'].mean()

# Фильтрация — только пассажиры первого класса
first_class = data[data['Pclass'] == 1]

print(f"Средний возраст: {average_age}")
print(f"Пассажиров первого класса: {len(first_class)}")
