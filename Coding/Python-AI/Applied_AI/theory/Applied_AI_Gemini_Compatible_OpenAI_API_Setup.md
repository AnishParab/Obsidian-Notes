> This will let you use **gemini's** model in **OpenAI's** API syntax.

---
# Code
[Refer this](https://ai.google.dev/gemini-api/docs/openai)

``` python
from openai import OpenAI

client = OpenAI(
    api_key="PASTE_YOUR_GEMINI_API_KEY",
	base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

response = client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[
        {   "role": "system",
            "content": "You are a helpful assistant."
        },
        {
            "role": "user",
            "content": "Explain to me how AI works"
        }
    ]
)

print(response.choices[0].message)
```

---
