# One-shot prompting
**Definition:**  
You give **one example** to show the expected behavior.

**Pros**
- Better formatting consistency
- Improved accuracy vs zero-shot

**Cons**
- Still limited guidance

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

# One-Shot Prompting
SYSTEM_PROMPT = """
You should only and only answer the coding related questions. Do not answer anything else.
Your name is Jarvis. If user asks something other than coding, just say sorry.

Examples:
Q: Can you explain the a+b whole square ?
A: Sorry, I can only help with Coding related questions.
"""

response = client.chat.completions.create(
    model="gemini-3-flash-preview",
    messages=[
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": "Give me a cheesecake recipe"},
    ],
)

print(response.choices[0].message.content)
```

**Output**:
``` text
Sorry, I can only help with Coding related questions.
```

---
