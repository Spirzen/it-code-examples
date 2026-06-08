from openai import OpenAI, AuthenticationError, RateLimitError

client = OpenAI()

try:
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": "Привет"}],
    )
    print(response.choices[0].message.content)
except AuthenticationError:
    print("Неверный API key — проверьте OPENAI_API_KEY")
except RateLimitError:
    print("Слишком много запросов — подождите минуту")
