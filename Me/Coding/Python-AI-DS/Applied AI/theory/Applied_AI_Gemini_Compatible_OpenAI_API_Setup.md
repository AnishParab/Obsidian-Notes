> This will let you use **gemini's** model in **OpenAI's** API syntax.

---
# API Integration and Setup
``` bash
pip install openai
```

``` bash
pip install python-dotenv
```

### `.env`
``` text
GEMINI_API_KEY=your_api_key
```

> [Refer this](https://ai.google.dev/gemini-api/docs/openai)
``` python
from dotenv import load_dotenv
import os
from openai import OpenAI

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("API Key not found")

client = OpenAI(
    api_key=api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

response = client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Explain to me how AI works"},
    ],
)

print(response.choices[0].message)
```

---
