from openai import OpenAI

client = OpenAI()

history = [
    {"role": "system", "content": "Ты консультант по выбору первого языка программирования."},
    {"role": "user", "content": "Мне 14 лет, хочу делать игры."},
]

r1 = client.chat.completions.create(model="gpt-4o-mini", messages=history)
reply1 = r1.choices[0].message.content
print("1:", reply1)

history.append({"role": "assistant", "content": reply1})
history.append({"role": "user", "content": "А если ещё интересна веб-разработка?"})

r2 = client.chat.completions.create(model="gpt-4o-mini", messages=history)
print("2:", r2.choices[0].message.content)
