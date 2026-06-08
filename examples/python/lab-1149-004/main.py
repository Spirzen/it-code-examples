import json
from openai import OpenAI

client = OpenAI()

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {
            "role": "system",
            "content": "Отвечай только валидным JSON по запросу пользователя.",
        },
        {
            "role": "user",
            "content": (
                'Верни объект: {"city": "..", "country": "..", "fun_fact": ".."} '
                "для города Казань."
            ),
        },
    ],
    response_format={"type": "json_object"},
    temperature=0.2,
)

raw = response.choices[0].message.content
data = json.loads(raw)
print(data["city"], data["fun_fact"])
