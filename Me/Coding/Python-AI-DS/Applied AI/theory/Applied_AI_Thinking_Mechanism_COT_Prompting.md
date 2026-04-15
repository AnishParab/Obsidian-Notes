# Code
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

# Explicit COT Prompting
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


def thinking_loop(message_history):
    while True:
        response = client.chat.completions.create(
            model="gemini-3-flash-preview",
            # Stores a List JSON Objects instead of string in raw_result, [{"step": "START", "content": "something"}]
            response_format={"type": "json_object"},
            messages=message_history,
        )

        raw_result = response.choices[0].message.content
        if raw_result is None:
            raise ValueError("Model returned no content")

        message_history.append(
            {"role": "assistant", "content": raw_result},
        )

        parsed_result = json.loads(raw_result)

        for item in parsed_result:
            step = item.get("step")
            content = item.get("content")

            if step == "START":
                yield f"🔥 {content}"
                continue

            if step == "PLAN":
                yield f"🧠 {content}"
                continue

            if step == "OUTPUT":
                yield f"😇 {content}"
                return


def main():
    message_history = []

    message_history.append(
        {"role": "system", "content": SYSTEM_PROMPT},
    )

    user_input = input("> ")

    message_history.append(
        {"role": "user", "content": user_input},
    )

    for chunk in thinking_loop(message_history):
        print(chunk, flush=True)


main()
```

---
