from openai import OpenAI

client = OpenAI()

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {
            "role": "system",
            "content": (
                "Ты помощник для школьников по информатике. "
                "Отвечай кратко, простым языком, без жаргона. "
                "Если не знаешь — скажи «не уверен»."
            ),
        },
        {
            "role": "user",
            "content": "Чем массив отличается от списка в Python?",
        },
    ],
    temperature=0.3,
)

print(response.choices[0].message.content)
