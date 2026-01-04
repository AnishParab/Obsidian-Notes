# Code
``` python
from dotenv import load_dotenv
import os
from openai import OpenAI
from openai.types.chat import ChatCompletionMessageParam

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

client = OpenAI(
    api_key=api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

messages: list[ChatCompletionMessageParam] = [
    {
        "role": "system",
        "content": "I am a helpful AI assiatant",
    }
]


def chat_loop():
    print("CLI chatbot started. Type 'quit' or 'exit' to stop.\n")

    while True:
        user_input = input("> ").strip()

        if user_input.lower() in {"exit", "quit"}:
            print("Goodbye.")
            break

        messages.append(
            {
                "role": "user",
                "content": user_input,
            }
        )

        response = client.chat.completions.create(
            model="gemini-3-flash-preview",
            messages=messages,
        )

        assistant_reply = response.choices[0].message.content
        if assistant_reply is None:
            raise ValueError("Assistant didn't reply.")

        # Maintaining assiatant context
        messages.append(
            {
                "role": "assistant",
                "content": assistant_reply,
            }
        )

        print(f"\n{assistant_reply}\n")


if __name__ == "__main__":
    chat_loop()
```

---
