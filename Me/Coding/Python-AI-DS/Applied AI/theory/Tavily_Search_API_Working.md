# Problems in Web-scraping

- Traditional search APIs such as Google, Serp and Bing retrieve search results based on a user query
- These results are not always relevant.
- Hence scraping these websites for relevant information and optimizing the content for the LLM to not hit the context limits is a task.

---
# How does the Seach API work ?

- Tavily aggregates up to 20 sources per call
- Uses AI to rank and filter the most relevant content, and supports custom context and token limits for RAG.
- It can also return a concise answer for agent use, helping reduce hallucinations with accurate, task-focused information.

---
