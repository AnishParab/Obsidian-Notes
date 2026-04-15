# Synchronous RAG (Sync)
### What it means
Each stage runs **sequentially**. The system **waits** for one step to finish before starting the next.
### Typical flow
```
User Query
 → Embed query
 → Vector search
 → Rerank (optional)
 → LLM generation
 → Response
```
### Characteristics
- Single request → single execution path
- Blocking I/O (network, disk, model calls)
- Easy to reason about and debug
### When sync is a good choice
- Learning RAG
- CLI tools
- Low traffic
- Deterministic pipelines
- Offline evaluation / experiments
### Downsides
- Poor latency under load
- Wasted time during I/O waits
- Cannot parallelize retrieval or tool calls

---
# Asynchronous RAG (Async)
### What it means
Stages **overlap in time**. While one step waits (network, DB, LLM), others continue.
### Typical async flow
```
User Query
 → Embed query (await)
 → Parallel vector searches (await gather)
 → Parallel rerank / filters
 → Stream LLM tokens
```
### Characteristics
- Non-blocking I/O
- Concurrency (not parallel CPU)
- Event-loop driven (async/await)
### Where async shines in RAG
- Vector DB calls (Qdrant, Pinecone)
- LLM API calls
- Multi-retriever setups
- Streaming responses
- Agentic RAG (tool calling loops)
### Downsides
- More complex code
- Harder debugging
- Requires async-compatible libraries everywhere

---
