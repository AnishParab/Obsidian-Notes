# Search the Web

``` python
from tavily import TavilyClient

tavily_client = TavilyClient(api_key="tvly-YOUR_API_KEY")
response = tavily_client.search("Who is Leo Messi?")

print(response)
```

---
# API Credit Costs

- Basic Search: 1 request = 1 API credit
- Advanced Search: 1 request = 2 API credit

---
