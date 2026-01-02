# Few-Shot Prompting

> You actually give some examples along with the instructions.

> Helps increasing accuracy of the code.

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

# Few-Shot Prompting
SYSTEM_PROMPT = """
You should only and only answer the coding related questions. Do not answer anything else.
Your name is Jarvis. If user asks something other than coding, just say sorry.

Examples:
Q: Can you explain the a+b whole square ?
A: Sorry, I can only help with Coding related questions.

Q: Hey, Write a code in python for adding two numbers.
A: def add(a, b):
        return a+b
"""

response = client.chat.completions.create(
    model="gemini-3-flash-preview",
    messages=[
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": "Give me a cheescake recipe."},
    ],
)

print(response.choices[0].message.content)
```

**Output**:
``` text
Sorry, I can only help with Coding related questions.
```

---
