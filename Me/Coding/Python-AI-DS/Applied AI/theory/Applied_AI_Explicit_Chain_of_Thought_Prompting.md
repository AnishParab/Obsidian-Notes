# Chain of Thought Models (COT)
- These are models which think before they act.
- For example **deepSeek**, **gpt-o3** models.
- This makes the model more accurate but slow.

---
# Code: Explicit COT Prompting

``` python
from dotenv import load_dotenv
import os
from openai import OpenAI
import json

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

client = OpenAI(
    api_key=api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

# COT Prompting
SYSTEM_PROMPT = """
    You're an expert AI Assistance in resolving user queries using Chain of Thought.
    You work on START, PLAN and OUTPUT steps.
    You need to first PLAN what needs to be done. The PLAN can be of multiple steps.
    Once you think enough PLAN has been done, finally you can give OUTPUT.

    Rules:
    - Strictly follow the given JSON output format.
    - Only run one step at a time.
    - The sequence of steps is START (where user gives an input), 
      PLAN (That can be multiple times) and finally,
      OUTPUT (which is going to be displayed to the user).

    Output JSON format:
    { "step": "START" | "PLAN" | "OUTPUT",
      "content" : "string"
    }

    Example:
    Q: Hey, can solve 2 + 3 * 5 / 10
    A:
        START: { "step": "START", "content": "Hey, Can you solve 2 + 3 * 5 / 10" }
        PLAN: { "step": "PLAN", "content": "Seems like user is interested in a maths problem." }
        PLAN: { "step": "PLAN", "content": "Looking at the problem we should solve this using BODMAS method." }
        PLAN: { "step": "PLAN", "content": "Yes, BODMAS method is the correct thing to be done here." }
        PLAN: { "step": "PLAN", "content": "First we must multiply 3 by 5 which is 15." }
        PLAN: { "step": "PLAN", "content": "Now the new equation is 2 + 15 / 10." }
        PLAN: { "step": "PLAN", "content": "We must now perform 15 / 10 which is 1.5." }
        PLAN: { "step": "PLAN", "content": "Now the new eqaution is 2 + 1.5." }
        PLAN: { "step": "PLAN", "content": "You get 3.5 by adding 2 and 1.5" }
        PLAN: { "step": "PLAN", "content": "You are finally left with 3.5 as answer." }
        OUTPUT: { "step": "OUTPUT", "content": "Your answer is 3.5" }
"""

response = client.chat.completions.create(
    model="gemini-3-flash-preview",
    # Response Formats
    response_format={"type": "json_object"},
    messages=[
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": "write a code for binary search in python."},
        # Manually keep appending messages to the History
        {
            "role": "assistant",
            "content": json.dumps(
                {
                    "step": "START",
                    "content": "write a code for binary search in python.",
                }
            ),
        },
    ],
)

print(response.choices[0].message.content)
```

---
