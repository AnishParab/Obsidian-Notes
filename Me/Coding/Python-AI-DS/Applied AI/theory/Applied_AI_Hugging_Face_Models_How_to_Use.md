# How to use Hugging Face Models

- Here are the ways, Hugging Face Models can be used.

---
### Transformers

1. **`pipeline()`**
    - High-level abstraction
    - Handles:
        - tokenizer
        - model loading
        - preprocessing
        - decoding
    - Best for:
        - quick inference
        - prototyping
2. **`AutoTokenizer + AutoModelForCausalLM`**
    - Low-level manual control
    - You handle:
        - tokenization
        - tensors
        - generation
        - decoding
    - Best for:
        - fine-tuning
        - optimization
        - production systems

---
### Inference

1. **Inference Providers**
	- Hosted APIs for running AI models remotely
	- No local GPU/model setup required
	- Send prompt → receive output
2. **HuggingChat**
	- Chat interface by Hugging Face
	- Similar to ChatGPT
	- Uses open-source models

---
### Notebooks

1. **Google Colab**
2. **Kaggle**

---
### Local Apps

- Run AI models on your own machine
- More privacy and control
- Requires local CPU/GPU resources

1. **`vLLM`**
	- High-performance LLM inference engine
	- Optimized for fast GPU serving
	- Used in production APIs
2. **`SGLang`**
	- Framework for structured LLM inference
	- Optimizes multi-step generation workflows
	- Used for agents and advanced pipelines
3. **`Docker_Model_Runner`**
	- Runs models inside Docker containers
	- Ensures reproducible deployments
	- Isolates dependencies

> **Inference Engines** are opimized and used for Productions, rather than *transformers*

---
