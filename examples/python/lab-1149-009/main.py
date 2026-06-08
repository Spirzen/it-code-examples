import os
import sys
from openai import OpenAI

def ask(prompt: str, system: str = "Ты полезный помощник. Отвечай на русском.") -> str:
    client = OpenAI()
    response = client.chat.completions.create(
        model=os.environ.get("OPENAI_MODEL", "gpt-4o-mini"),
        messages=[
            {"role": "system", "content": system},
            {"role": "user", "content": prompt},
        ],
        temperature=0.3,
    )
    return response.choices[0].message.content

if __name__ == "__main__":
    if not os.environ.get("OPENAI_API_KEY"):
        sys.exit("Задайте переменную OPENAI_API_KEY")
    text = ask("Объясни, что такое API, в трёх предложениях.")
    print(text)
