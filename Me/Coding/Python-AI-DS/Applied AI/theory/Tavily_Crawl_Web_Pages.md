# Crawl Web Pages

``` python
from tavily import TavilyClient

tavily_client = TavilyClient(api_key="tvly-YOUR_API_KEY")
response = tavily_client.crawl("https://docs.tavily.com", instructions="Find all pages on the Python SDK")

print(response)
```

---
# API Credit Costs

- Crawl Cost = Mapping Cost + Extraction Cost

---