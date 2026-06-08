import re

text = "Почты: dev@example.com, admin@test.org"

emails = re.findall(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", text)
print("Найденные email:", emails)

masked_text = re.sub(r"\b\d{4}\b", "####", "Код подтверждения: 1234")
print(masked_text)

log = "ERROR 2024-05-25 disk full"
m = re.search(r"^(?P<level>\w+)\s+(?P<date>\d{4}-\d{2}-\d{2})\s+(?P<msg>.+)$", log)
if m:
    print(m.group("level"), m.group("date"), m.group("msg"))
