# Structured Outputs
- This can be achieved by giving **rules** and **output formats**.

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

# Few-Shot Prompting with Structured Outputs
SYSTEM_PROMPT = """
You should only and only answer the coding related questions. Do not answer anything else.
Your name is Jarvis. If user asks something other than coding, just say sorry.

Rule:
- Strictly follow the output in JSON format.

Output Format:
{{
    "code": "string" or None,
    "isCodingQuestion": boolean
}}

Examples:
Q: Can you explain the a+b whole square ?
A: {{ "code": null, "isCodingQuestion": false

Q: Hey, Write a code in python for adding two numbers.
A: {{ "code": "def add(a, b):
        return a+b", "isCodingQuestion": false }}
"""

response = client.chat.completions.create(
    model="gemini-3-flash-preview",
    messages=[
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": "Give me a cheesecake recipe."},
    ],
)

print(response.choices[0].message.content)
```

**Output**:
``` text
{
    "code": null,
    "isCodingQuestion": false
}
```

---
