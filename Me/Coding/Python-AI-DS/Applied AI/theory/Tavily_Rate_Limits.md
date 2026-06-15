# Tavily Rate Limits

> Access to production keys requires either an active **Paid Plan** or **PAYGO** enabled. More information can be found [here](https://docs.tavily.com/guides/api-credits).
> When using the REST API, ensure you include your API key in the header to apply the correct rate limits.

- **Search API:**
    - Dev: 100 RPM
    - Prod: 1000 RPM
- **Crawl API:**
    - Dev/Prod: 100 RPM
- **Research API:**
    - Dev/Prod: 20 RPM
- **Usage API:**
    - Dev/Prod: 10 requests / 10 min
- **On limit exceed:**
    - Returns `429` with `retry-after` → wait before retry
- **Notes:**
    - Prod keys need paid/PAYGO
    - Always send API key in headers

---
