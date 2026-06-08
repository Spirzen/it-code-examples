from openai import OpenAI

client = OpenAI()

stream = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": "Расскажи коротко, что такое TCP."}],
    stream=True,
)

for chunk in stream:
    part = chunk.choices[0].delta.content
    if part:
        print(part, end="", flush=True)
print()
