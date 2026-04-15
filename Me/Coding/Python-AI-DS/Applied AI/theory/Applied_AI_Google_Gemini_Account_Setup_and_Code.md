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

# Load environment variables
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("GEMINI_API_KEY not found in environment")

# Create Gemini client
client = genai.Client(api_key=api_key)

# Generate content
response = client.models.generate_content(
    model="gemini-2.5-flash", contents="Explain how AI works"
)

# Print the generated text
print(response.text)
```

---
