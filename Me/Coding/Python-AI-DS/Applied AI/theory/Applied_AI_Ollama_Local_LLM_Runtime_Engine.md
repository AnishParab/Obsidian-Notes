[Ollama](https://ollama.com/)

---
# What is **Ollama** (Local LLM Runtime Engine)
- **Ollama** is a **local LLM runtime engine** that lets you **download, run, and manage large language models on your own machine** (CPU or GPU) with minimal setup. It abstracts model loading, quantization, hardware acceleration, and serving behind a simple CLI and HTTP API.

---
# Core Idea
> _“Docker-like experience, but for LLMs running locally.”_
- You pull a model, run it, and interact with it—without cloud APIs.

---
# What Ollama Provides

**1. Local Model Execution**
- Runs models entirely **offline**
- Supports CPU, Metal (macOS), CUDA/ROCm (platform-dependent)

**2. Model Management**
- `ollama pull llama2`
- `ollama run mistral`
- Versioned models with reproducible configs

**3. Runtime Abstraction**
- Handles:
    - Quantization (Q4/Q5/Q8)
    - Memory mapping
    - Threading
    - GPU offloading
- You don’t manage GGUF details manually

**4. Simple Interfaces**
- **CLI** for quick use
- **HTTP API** for apps, agents, editors, and scripts

---
# Ollama vs Alternatives (High-Level)

| Tool       | Role                               |
| ---------- | ---------------------------------- |
| Ollama     | Local **LLM runtime + manager**    |
| LM Studio  | GUI-focused local inference        |
| llama.cpp  | Low-level inference engine         |
| vLLM       | High-throughput server (GPU-heavy) |
| OpenAI API | Cloud-hosted inference             |

- Ollama internally leverages optimized inference backends (e.g., llama.cpp-style runtimes) but exposes a **much higher-level UX**.

---
# When to Use Ollama

Use it when:
- You want **local inference**
- You are building **agents, RAG, dev tools**
- You want **API-compatible local LLMs**
- You want fast iteration without cloud dependency

Avoid it when:
- You need **large-scale serving**
- You need **training or fine-tuning**
- You rely on **cutting-edge proprietary models**

---
