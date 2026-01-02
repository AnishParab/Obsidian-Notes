# `/queues` : Consumer/Processor

- `worker.py` - **To write the consumer/processor**
``` python
from openai import OpenAI
import os
from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_qdrant import QdrantVectorStore

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

openai_client = OpenAI(
    api_key=api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

embeddings = GoogleGenerativeAIEmbeddings(
    model="models/embedding-001",
)

vector_db = QdrantVectorStore.from_existing_collection(
    url="http://localhost:6333",
    collection_name="learning_rag",
    embedding=embeddings,
)


def process_query(query: str):
    print("Searching Chunks", query)
    search_results = vector_db.similarity_search(query=query)

    # Build context string safely
    context = "\n\n".join(
        [
            f"Page Content: {result.page_content}\n"
            f"Page Number: {result.metadata.get('page_label')}\n"
            f"File Location: {result.metadata.get('source')}"
            for result in search_results
        ]
    )

    SYSTEM_PROMPT = """
    You are helpful AI assistant who answers user query based on the available
    context retrieved from PDF file along with page_contents and page number.

    You should only ans the user based on the following context and navigate
    the user to open the right page number to know more.

    Context:
    {context}
    """

    response = openai_client.chat.completions.create(
        model="gemini-3-flash-preview",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": query},
        ],
    )

    return response.choices[0].message.content
```

---
# `/client` : Producer
- `__init__.py`
- `rq_client.py`

---
