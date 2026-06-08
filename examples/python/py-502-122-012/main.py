
import csv

rows = [
    ["name", "age", "city"],
    ["Анна", 28, "Москва"],
    ["Иван", 35, "Казань"]
]

with open("users.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerows(rows)

with open("users.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(f"{row['name']} живет в городе {row['city']}")
