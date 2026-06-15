# Create Research Talk

``` python
from tavily import TavilyClient

tavily_client = TavilyClient(api_key="tvly-YOUR_API_KEY")
response = tavily_client.research("What are the latest developments in AI?")

print(response)
```

---
# API Credit Costs

- Uses dynamic pricing with minimum and maximum credit consumption.
- `model=mini` or `model=pro`.

| Request Cost Boundaries | model=pro   | model=mini  |
| ----------------------- | ----------- | ----------- |
| Per-request minimum     | 15 credits  | 4 credits   |
| Per-request maximum     | 250 credits | 110 credits |

---
