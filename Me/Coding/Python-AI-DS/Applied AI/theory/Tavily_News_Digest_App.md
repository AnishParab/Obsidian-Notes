# Pre-requisites

- It needs a LLM model API key:
[[Applied_AI_Google_Gemini_Compatible_OpenAI_API_Setup]]

- Setup tavily.

---
# Simple RAG Example

![[tavily.excalidraw|400]]

---
## Code

##### Define few examples we are interested in
``` python
topics = [
	"trump",
	"epstein",
	"war"
]
```

##### Travily News Search
``` python
context = []

for topic in topics:
	search_responses = tavily_client.search(topic, topic="news", time_range="day")
	
	context.append({
		"topic": topic,
		"results": [
			{ "url": result["url"], "title": result["title"], "content": result["content"] } for result in search_responses["results"]
		]
	})
```

- `topic, topic="news", time_range="day"` - limitations applied for optimized search results.

##### Daily News Digest using LLM through LangChain
- This searches results as context for the LLM and generates out daily digest.
``` python
from langchain_openai import ChatOpenAI
from datetime import datetime

gpt_4o = ChatOpenAI(api_key=OPENAI_API_KEY, model="gpt-4o", temperature=0.0)

prompt = """
You are a Journalist agent.

- Generate a daily news digest. Today's date is {date}.
- Use only the following sources to get accurate information for each topic and write a short article about it:
{context}.
"""

formatted_prompt = prompt.format(context=context, date=datetime.now().strftime("%Y-%m-%d"))

gpt_4o_response = gpt_4o.invoke(formatted_prompt)

print(gpt_4o_response.content)
```

---
# Intermediate RAG Example

![[tavily_intermediate_rag_example.excalidraw|500]]
1. The results aren't very detailed for some of the chosen topics. This is because we're not extracting the full content from each source.
2. The output doesn't have an explicitly defined structure. Across different runs of the program, you might get an output with a different structure.

---
## Code

##### Travily News Search
``` python
context = []

for topic in topics:
	search_query = f"Today's latest news about {topic}"

	search_response = tavily_client.search(topic, topic="news", time_range="day")

	context.append({
		"topic": topic,
		"sources": [
			{ "url": result["url"], "title": result["title"] } for result in search_response["results"]
		]
	})
```

##### Full content extraction using Tavily Extract
``` python
extracted_results = []

for topic in context:
    urls = [source["url"] for source in topic["sources"]]

    extract_response = tavily_client.extract(urls)

    # Map successful results
    for extracted_result in extract_response["results"]:
        for source in topic["sources"]:
            if source["url"] == extracted_result["url"]:
                source["content"] = extracted_result["raw_content"]

    # Remove failed results (avoid modifying list while iterating)
    failed_urls = {res["url"] for res in extract_response["failed_results"]}
    topic["sources"] = [
        source for source in topic["sources"]
        if source["url"] not in failed_urls
    ]

    extracted_results.append(topic)
```

##### Defining the Ouput structure with Pydantic
``` python
from pydantic import BaseModel, Field
from typing import List


class TopicSection(BaseModel):
    title: str = Field(..., description="Section title")
    article: str = Field(..., description="Generated summary/content")
    sources: List[str] = Field(..., description="List of source URLs")


class DailyNewsDigest(BaseModel):
    sections: List[TopicSection]
```

##### Daily News Digest using LLM through LangChain
``` python
from datetime import datetime
import json

prompt = """
You are a Journalist agent.

- Generate a daily news digest. Today's date is {date}.
- Use only the following sources to get accurate information for each topic and write a short article about it:
{context}

- Return structured output with:
  - title
  - article
  - sources (list of URLs used)
"""

formatted_prompt = prompt.format(
    context=json.dumps(extracted_results, indent=2),
    date=datetime.now().strftime("%Y-%m-%d")
)

response = gpt_4o.with_structured_output(DailyNewsDigest).invoke(formatted_prompt)

for section in response.sections:
    print(f"Topic: {section.title}")
    print(f"Content: {section.article}")
    print(f"Sources: {section.sources}")
    print()
```

---
