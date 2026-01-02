# Gemini Studio
[Gemini](https://aistudio.google.com/)

- Create API key.
- Free tier available.

---
# API Integration and Setup
``` bash
pip install google-genai
```

``` bash
pip install python-dotenv
```

### `.env`
``` text
GEMINI_API_KEY=your_api_key
```

> **Refer this in docs.**
``` python
from dotenv import load_dotenv
import os
from google import genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(
	api_key=api_key
)

response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents="Explain how AI works in a few words",
)

print(response.text)
```

---
