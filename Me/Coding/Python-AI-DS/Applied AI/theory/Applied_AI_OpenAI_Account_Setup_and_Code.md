# OpenAI
[OpenAI](https://platform.openai.com/docs/overview)

- Add credits to your account.
- Make a new API key.

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
OPENAI_API_KEY=your_api_key
```

> **Refer this in docs**
``` python
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()

response = client.responses.create(
    model="gpt-5.2",
    input="Write a short bedtime story about a unicorn."
)

print(response.output_text)
```

---
