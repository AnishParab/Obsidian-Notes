# Code
``` python
from dotenv import load_dotenv
import os
from openai import OpenAI
from openai.types.chat import ChatCompletionMessageParam

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("API Key not found")

client = OpenAI(
    api_key=api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

# Context Store
# Sends correct type to messages in chat completions
messages: list[ChatCompletionMessageParam] = [
    {
        "role": "system",
        "content": "You are a helpful AI Assistant",
    }
]


def ask_ai(user_input: str) -> str:
    global messages

    # Add user role
    messages.append(
        {
            "role": "user",
            "content": user_input,
        }
    )

    # Generate response using full context
    response = client.chat.completions.create(
        model="gemini-2.5-flash",
        messages=messages,
    )

    assistant_reply = response.choices[0].message.content
    if assistant_reply is None:
        raise ValueError("Reply is of type None")

    messages.append(
        {
            "role": "assistant",
            "content": assistant_reply,
        }
    )

    return assistant_reply


print(ask_ai("Explain how AI works in short"))
print("===================================================")
print(ask_ai("Explain it more simply"))
print("===================================================")
print(ask_ai("Summarize in one sentence"))
```

---
