
import datetime

# Получение текущей даты и времени
now = datetime.datetime.now()
print(f"Текущая дата и время: {now}")

# Извлечение отдельных компонентов
year = now.year
month = now.month
day = now.day
hour = now.hour
minute = now.minute
second = now.second

print(f"Год: {year}, Месяц: {month}, День: {day}")
print(f"Время: {hour}:{minute}:{second}")

# Создание объекта даты вручную
birthday = datetime.date(1994, 11, 24)
print(f"Дата рождения: {birthday}")

# Вычисление разницы во времени
today = datetime.date.today()
days_until_birthday = (birthday.replace(year=today.year) - today).days

if days_until_birthday < 0:
    next_birthday = birthday.replace(year=today.year + 1)
    days_left = (next_birthday - today).days
    print(f"До следующего дня рождения осталось дней: {days_left}")
else:
    print(f"До дня рождения осталось дней: {days_until_birthday}")

# Форматирование даты
formatted_date = now.strftime("%d.%m.%Y %H:%M")
print(f"Отформатированная дата: {formatted_date}")
