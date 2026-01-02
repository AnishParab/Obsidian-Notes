This Code is inspired from : [[Applied_AI_Thinking_Mechanism_COT_Prompting]]

---
# Real-Time Weather Agent
``` python
from openai import OpenAI
from dotenv import load_dotenv
import os
import requests
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
    You can also call a tool if required from a list of available tools.
    For every tool call wait for the observe step which is the output from the called tool.

    Rules:
    - Strictly follow the given JSON output format.
    - Only run one step at a time.
    - The sequence of steps is START (where user gives an input), 
      PLAN (That can be multiple times) and finally,
      OUTPUT (which is going to be displayed to the user).

    Output JSON format:
    { "step": "START" | "PLAN" | "OUTPUT" | "TOOL" | "OBSERVE",
      "content" : "string",
      "tool": "string",
      "input": "string",
    }

    Available Tools:
    - get_weather: Takes city name as an input string and return the weather information about the city.

    Example 1:
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

    Example 2:
    Q: What is the weather of Goa?
    A:
        START: { "step": "START", "content": "Hey, Can you tell me what is the weather of Goa?" }
        PLAN: { "step": "PLAN", "content": "Seems like user is interested in getting weather of Goa." }
        PLAN: { "step": "PLAN", "content": "Lets see if we have a tool from the list of available tools." }
        PLAN: { "step": "PLAN", "content": "Great, we have get_weather tool available for this query." }
        PLAN: { "step": "PLAN", "content": "I need to call get_wether for Goa as input for city." }
        PLAN: { "step": "TOOL", "tool": "get_weather", "input": "goa." }
        PLAN: { "step": "OBSERVE", "tool": "get_weather", "output": "The temperatur of Goa is Cloudy with 27 celsius." }
        PLAN: { "step": "PLAN", "content": "I got the weather information about goa." }
        OUTPUT: { "step": "OUTPUT", "content": "The current weather in goa is 27 celsius with some cloudy sky." }
"""

# To prevent ssl errors
session = requests.Session()


def get_weather(city: str):
    url = f"https://wttr.in/{city.lower()}?format=%C+%t"

    try:
        # timeout prevents ssl errors
        response = session.get(url, timeout=8)
        response.raise_for_status()
        return f"The weather in {city} is {response.text.strip()}"
    except Exception as e:
        return f"Weather unavailable for {city}: {e}"


# Map of all tools
available_tools = {
    "get_weather": get_weather,
}


def thinking_loop(message_history):
    tool_results = []

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
            tool_to_call = item.get("tool")
            tool_input = item.get("input")

            if step == "START":
                yield f"🔥 {content}"
                continue

            if step == "PLAN":
                yield f"🧠 {content}"
                continue

            if step == "TOOL":
                yield f"🛠 {tool_to_call}({tool_input})"
                tool_response = available_tools[tool_to_call](tool_input)

                tool_results.append(
                    {
                        "tool": tool_to_call,
                        "input": tool_input,
                        "output": tool_response,
                    }
                )

                message_history.append(
                    {
                        "role": "assistant",
                        "content": json.dumps(
                            {
                                "step": "OBSERVE",
                                "tool": tool_to_call,
                                "input": tool_input,
                                "output": tool_response,
                            }
                        ),
                    }
                )
                continue

            if step == "OUTPUT":
                yield f"😇 {content}"
                return


def main():
    message_history = []

    message_history.append(
        {"role": "system", "content": SYSTEM_PROMPT},
    )

    while True:
        user_input = input("> ").strip()

        if user_input.lower() in {"exit", "quit"}:
            break

        message_history.append(
            {"role": "user", "content": user_input},
        )

        for chunk in thinking_loop(message_history):
            print(chunk, flush=True)

        print()


main()
```

---
