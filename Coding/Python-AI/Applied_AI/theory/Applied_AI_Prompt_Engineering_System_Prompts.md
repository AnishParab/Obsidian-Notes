# System Prompts
A **system prompt** is **high-priority instruction context** that:
- Defines the model’s **role**
- Sets **constraints**
- Specifies **rules of behavior**
- Shapes **output style and reasoning boundaries**
- It provides **Behavioral determinism**, not statistical determinism

---
# Code: System Prompts
``` python
from dotenv import load_dotenv
import os
from openai import OpenAI

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

client = OpenAI(
    api_key=api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

response = client.chat.completions.create(
    model="gemini-3-flash-preview",
    messages=[
        {
            "role": "system",
            # System Prompts
            "content": """You are an expert in maths and only and only answer
            maths related questions. That if the query is not realated to maths
            , just say sorry and do not answer that.""",
        },
        {"role": "user", "content": "Can you teach me hoe to make a pizza?"},
    ],
)

print(response.choices[0].message)
```

---
