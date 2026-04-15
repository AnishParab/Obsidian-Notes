# What is an Agent ?
- An **Agent** in **Agentic AI** is an autonomous software entity that can **perceive**, **reason**, **decide**, and **act** toward achieving a goal—often over multiple steps and with minimal human intervention.

![Image](https://diabsolut.com/wp-content/uploads/2025/07/Canva-IterativeProcessAgenticAI-450x360.png)


![Image](https://www.promptingguide.ai/_next/image?q=75&url=%2F_next%2Fstatic%2Fmedia%2Fagent-framework.ad7f5098.png&w=1920)

---
# Core Definition
An AI agent is not just a model that responds to prompts. It is a system that:
- Maintains **state** (memory/context)
- Makes **decisions** based on goals
- **Plans** actions
- **Executes** those actions using tools or APIs
- **Observes outcomes** and adapts

This creates a continuous **sense → think → act → learn** loop.

---
# Key Components of an AI Agent
1. **Goal**
    - Explicit objective (e.g., “Fix failing tests”, “Book cheapest flight”)
2. **Perception**
    - Reads inputs from environment (text, files, APIs, system state)
3. **Reasoning / Planning**
    - Breaks goals into steps
    - Chooses next best action
    - Often powered by an LLM + planner
4. **Action / Tools**
    - Executes code
    - Calls APIs
    - Uses databases, browsers, shells, etc.
5. **Memory**
    - Short-term: conversation or task context
    - Long-term: vector DB, files, logs
6. **Feedback Loop**
    - Evaluates results
    - Adjusts plan if something fails

---
# Simple Mental Model

```
Goal
  ↓
Observe → Think → Act
   ↑        ↓
   └─── Learn / Update Memory
```

---
# How an Agent Differs from a Normal LLM

| Aspect               | LLM     | AI Agent     |
| -------------------- | ------- | ------------ |
| Responds once        | ✅       | ❌            |
| Maintains state      | ❌       | ✅            |
| Uses tools           | Limited | Core feature |
| Multi-step planning  | ❌       | ✅            |
| Autonomous execution | ❌       | ✅            |

---
# Types of Agents
- **Reactive agents** – respond immediately, no planning
- **Planning agents** – decompose goals into steps
- **Tool-using agents** – execute real actions
- **Multi-agent systems** – agents collaborate or compete

---
