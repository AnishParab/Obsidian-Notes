# What I did
From the code in:
[[Applied_AI_Structured_Outputs_with_Pydantic]],

> I just added a new `available_tools` called as `run_cmd`.

---
# Code
``` python
from openai import OpenAI
from dotenv import load_dotenv
import os
import requests
import json
from pydantic import BaseModel, Field
from typing import Optional

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

client = OpenAI(
    api_key=api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)


def run_cmd(cmd: str):
    result = os.system(cmd)
    return result


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
    - get_weather(city: str): Takes city name as an input string and return the weather information about the city.
    - run_cmd(cmd: str): Takes a system linux commad as a string and executes the command on users system and returns the output from that command. 

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


class OutputFormat(BaseModel):
    step: str = Field(
        ...,
        description="The ID of the step. Example: START, PLAN, OUTPUT, TOOL, OBSERVE",
    )
    content: Optional[str] = Field(
        None,
        description="The optional string content for the step",
    )
    tool: Optional[str] = Field(
        None,
        description="The ID of the tool to call",
    )
    input: Optional[str] = Field(
        None,
        description="The input params for the tool",
    )


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
    "run_cmd": run_cmd,
}


def thinking_loop(message_history):
    tool_results = []

    while True:
        response = client.chat.completions.parse(
            model="gemini-3-flash-preview",
            response_format=OutputFormat,
            messages=message_history,
        )

        raw_result = response.choices[0].message.content
        if raw_result is None:
            raise ValueError("Model returned no content")

        message_history.append(
            {"role": "assistant", "content": raw_result},
        )

        parsed_result = response.choices[0].message.parsed
        if parsed_result is None:
            raise RuntimeError("Model returned no parsed output")

        step = parsed_result.step
        content = parsed_result.content
        tool_to_call = parsed_result.tool
        tool_input = parsed_result.input

        if step == "START":
            if content:
                yield f"🔥 {content}"
            continue

        if step == "PLAN":
            if content:
                yield f"🧠 {content}"
            continue

        if step == "TOOL":
            if tool_to_call is None or tool_input is None:
                raise RuntimeError("TOOL step missing tool or input")

            yield f"🛠 {tool_to_call}({tool_input})"

            tool_fn = available_tools.get(tool_to_call)
            if tool_fn is None:
                raise RuntimeError(f"Unknown tool: {tool_to_call}")

            tool_response = tool_fn(tool_input)

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

        if step == "OBSERVE":
            continue

        if step == "OUTPUT":
            if content:
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
