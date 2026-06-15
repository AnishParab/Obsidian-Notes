# Project Tracking

- You can optionally attach a Project ID to your API requests to organize and track usage by project. This is useful when a single API key is used across multiple projects or applications.To attach a project to your request, add the `X-Project-ID` header:

```
curl -X POST https://api.tavily.com/search \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer tvly-YOUR_API_KEY" \
  -H "X-Project-ID: your-project-id" \
  -d '{"query": "Who is Leo Messi?"}'
```

**Key features:**
- An API key can be associated with multiple projects
- Filter requests by project in the [/logs endpoint](https://docs.tavily.com/documentation/api-reference/endpoint/usage) and platform usage dashboard
- Helps organize and track where requests originate from

---
