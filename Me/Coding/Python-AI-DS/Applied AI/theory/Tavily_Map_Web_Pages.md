# Map Web Pages

``` python
from tavily import TavilyClient

tavily_client = TavilyClient(api_key="tvly-YOUR_API_KEY")
response = tavily_client.map("https://docs.tavily.com")

print(response)
```

---
# API Credit Costs

- Regulat Mapping: Every 10 successfull pages = 1 API credit
- Map with (`instructions`): Every 10 successfull pages = 2 API credit

---
