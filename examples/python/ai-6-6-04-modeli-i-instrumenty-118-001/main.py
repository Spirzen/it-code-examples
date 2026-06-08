from openai import OpenAI

client = OpenAI()

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": "Кратко объясни TCP handshake."}],
    temperature=0.2,
    top_p=0.9,
    max_tokens=400,
    frequency_penalty=0.3,
    presence_penalty=0.2,
    stop=["\n\n---"],
)
print(response.choices[0].message.content)
