# Imperative → Declarative UI (Why React Exists)

## 1. Imperative Era (Manual Control)

- UI updated via step-by-step DOM commands
- Developer manually:
    - Find elements
    - Attach listeners
    - Mutate DOM
- **Problem**: state drift
    - JS state ≠ DOM state
- **Result**: fragile, tightly coupled code

---
## 2. React: Declarative Model

- UI is derived from state
- You update **state**, not the DOM

**Source of Truth**
- State drives UI
- No manual DOM mutations

**Core Model**
- `UI = f(state)`
- Same state → same UI

**Mechanisms**
- Virtual DOM snapshot
- Diff old vs new
- Apply minimal DOM changes
- Drift eliminated by design

---
## 3. Comparison

| Aspect      | Imperative (JS)   | Declarative (React) |
| ----------- | ----------------- | ------------------- |
| Focus       | How to change DOM | What UI should be   |
| State sync  | Manual            | Automatic           |
| Consistency | Fragile           | Guaranteed          |
| Updates     | Redundant         | Minimal             |

----
