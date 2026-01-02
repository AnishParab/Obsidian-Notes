# Why LangChain ?
- LangChain provides you a lot of utility toools used in AI.

---
# LangChain
- **LangChain** is a Python (and JS) framework for building applications around large language models by **composing LLM calls with external data, tools, and control flow**.

---
# Core ideas
- **Chains**: Sequential pipelines that connect prompts, models, and post-processing.
- **Retrievers**: Standardized interfaces to fetch context from vector databases (e.g., Qdrant) for RAG.
- **Agents**: LLM-driven decision loops that choose tools/actions dynamically.
- **Memory**: Mechanisms to persist conversation or task state across turns.

---
# Why it’s used
- Speeds up **RAG prototyping** (ingestion → retrieval → generation).
- Provides **abstractions** for tools, prompts, and model providers.
- Integrates cleanly with vector stores, APIs, and frameworks like FastAPI.

---
# Trade-offs
- Abstractions can add **overhead** and hide performance details.
- Rapid API changes require version pinning and careful upgrades.

---
# Typical use
- Document Q&A, chatbots with tools, agentic workflows, and evaluation pipelines.

---
