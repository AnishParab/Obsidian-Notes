# Zero-Shot Prompting
**Definition:**  
- You give **only the task**, with **no examples**.

**Pros**
- Short prompts
- Fast and cheap

**Cons**
- Less reliable on complex or ambiguous tasks

---
# Code
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

# Zero-Shot Prompting
SYSTEM_PROMPT = "You should only and only answer the coding related questions. Do not answer anything else. Your name is Jarvis. If user asks something other than coding, just say sorry"

response = client.chat.completions.create(
    model="gemini-3-flash-preview",
    messages=[
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": "Can you teach me a cheesecake recipe?"},
    ],
)

print(response.choices[0].message.content)
```

**Output**:
``` text
sorry
```

---
