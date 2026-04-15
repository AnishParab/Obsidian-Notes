# RAG
- **RAG (Retrieval-Augmented Generation)** addresses a core limitation of agentic systems: **LLMs do not have reliable access to up-to-date, proprietary, or long-tail knowledge, and they hallucinate when forced to answer anyway**.

---
# Problems RAG solves

1. **Knowledge cutoff & staleness**  
    Base models are frozen at training time. RAG injects _current_ information at runtime.
2. **Hallucinations under uncertainty**  
    When the model lacks facts, it guesses. Retrieval grounds generation in sourced documents, reducing fabricated answers.
3. **Lack of private / domain knowledge**  
    Agents often need internal docs, tickets, logs, specs. RAG lets them query these without retraining.
4. **Poor reasoning over large corpora**  
    Agents can’t “remember” millions of tokens. RAG narrows context to the _relevant slices_.
5. **Tool misuse in agents**  
    Without grounding, agents choose wrong tools or plans. Retrieved evidence constrains decisions and improves action selection.

---
# Why this matters specifically for **Agentic AI**

- **Planning:** Agents retrieve policies, constraints, or prior runs before deciding next steps.
- **Execution:** Agents fetch task-specific facts (APIs, configs) right before acting.
- **Verification:** Agents compare outputs against retrieved sources to self-check.
- **Iteration:** Retrieval enables reflect-and-revise loops with evidence.

---
