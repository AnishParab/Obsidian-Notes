# PDF Project
- Here the page number problem is solved which was not solved in
[[Applied_AI_LanChain_PDF_Mini_Project]]

---
# Indexing Code
``` python
"""
Indexing Phase in RAG Pipeline
Fix: Preserve page integrity and mark page numbers as approximate
"""

from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_qdrant import QdrantVectorStore
from dotenv import load_dotenv

load_dotenv()

"""
Document Loading (page-level)
Each Document corresponds to exactly ONE PDF page
"""
pdf_path = Path(__file__).parent / "node-js.pdf"
loader = PyPDFLoader(file_path=pdf_path)
docs = loader.load()  # docs[i] == page i (logical PDF page)

"""
Page-safe Chunking
- Do NOT allow chunks to cross page boundaries
- chunk_overlap = 0 to avoid page bleed
"""
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=0,  # IMPORTANT: prevents cross-page contamination
    separators=["\n\n"],  # soft split inside same page
)

chunks = []

for doc in docs:
    page_chunks = text_splitter.split_documents([doc])

    for chunk in page_chunks:
        # Preserve original page label
        page_label = doc.metadata.get("page_label")

        # Explicitly mark page as approximate
        chunk.metadata["approx_page"] = page_label
        chunk.metadata["page_range"] = f"{page_label}±1"

        chunks.append(chunk)

"""
Embeddings
"""
embeddings = GoogleGenerativeAIEmbeddings(
    model="models/embedding-001",
)

"""
Vector Store
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
# Retrieval Code
``` python
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_qdrant import QdrantVectorStore
from dotenv import load_dotenv
from openai import OpenAI
import os

load_dotenv()

"""
Embedding model
"""
embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")

"""
Qdrant connection
"""
vector_db = QdrantVectorStore.from_existing_collection(
    url="http://localhost:6333",
    collection_name="learning_rag",
    embedding=embeddings,
)

"""
User query
"""
user_query = input("Ask something: ")

"""
Similarity search
"""
search_results = vector_db.similarity_search(query=user_query, k=4)

"""
Context assembly
- Uses approx_page and page_range instead of absolute page numbers
"""
context = "\n\n".join(
    [
        f"Page Content:\n{result.page_content}\n\n"
        f"Approximate Page: {result.metadata.get('approx_page')}\n"
        f"Page Range: {result.metadata.get('page_range')}\n"
        f"Source File: {result.metadata.get('source')}"
        for result in search_results
    ]
)

"""
System prompt
- Explicitly warns about approximation
"""
SYSTEM_PROMPT = f"""
You are a helpful AI assistant.

The page numbers are approximate because the document was chunked.
Guide the user to the nearest page range, not an exact page.

Answer ONLY using the context below.
If the answer is not present, say you do not know.

Context:
{context}
"""

"""
LLM call
"""
openai_client = OpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

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
