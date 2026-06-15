# Extract Web Pages

``` python
from tavily import TavilyClient

tavily_client = TavilyClient(api_key="tvly-YOUR_API_KEY")
response = tavily_client.extract("https://en.wikipedia.org/wiki/Artificial_intelligence")

print(response)
```

---
# API Credit Costs

- Basic Extract: Every 5 successfull url extracts = 1 API credit
- Advanced Extract: Every 5 successfull url extracts = 2 API credit

---
