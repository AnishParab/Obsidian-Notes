# PDF Mini Project
- Note that these codes work in retrieving the content,
**But**
- Page numbering sucks, which is a chunking and pypdf issue.

---
# Indexing Phase
``` python
"""
Indexing Phase in RAG Pipeline
"""

from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

# from langchain_openai import OpenAIEmbeddings
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_qdrant import QdrantVectorStore
import os
from dotenv import load_dotenv


load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

"""
Document Loading/Ingestion
"""
pdf_path = Path(__file__).parent / "node-js.pdf"

# Load this file in python program
loader = PyPDFLoader(file_path=pdf_path)
# Returns list of Document Objects
docs = loader.load()

"""
Text Chunking/Splitting
"""
# Split the docs into smaller chunks
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    # overlaps are another set of chunks overlapping the
    # previous ones for more context
    chunk_overlap=400,
)

chunks = text_splitter.split_documents(docs)

"""
Embedding Model
"""
embeddings = GoogleGenerativeAIEmbeddings(
    model="models/embedding-001",
)

"""
Vector Embeddings
"""
vector_store = QdrantVectorStore.from_documents(
    documents=chunks,
    embedding=embeddings,
    url="http://localhost:6333",
    collection_name="learning_rag",
)

print("Indexing of documents done.")
```

---
# Retrieval Phase
``` python
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_qdrant import QdrantVectorStore
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

openai_client = OpenAI(
    api_key=api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

# Embedding Model
embeddings = GoogleGenerativeAIEmbeddings(
    model="models/embedding-001"  # Gemini Embedding Model
)

vector_db = QdrantVectorStore.from_existing_collection(
    url="http://localhost:6333",
    collection_name="learning_rag",
    embedding=embeddings,
)

# Take user Input
user_query = input("Ask something: ")

# Similarity Search, returns Relevant Chunks
search_results = vector_db.similarity_search(query=user_query)

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

You should only ans the user based on the following context and navigate the
user to open the right page number to know more.

Context:
{context}
"""

response = openai_client.chat.completions.create(
    model="gemini-3-flash-preview",
    messages=[
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": user_query},
    ],
)

print(response.choices[0].message.content)
```

---
