# Imperative v/s Declarative

- Imperative: manually find elements, attach listeners, mutate DOM → state drift (JS state ≠ DOM state) → fragile, tightly coupled
- Declarative: update state, React derives the UI

Core model: `UI = f(state)` — same state → same UI

| Aspect      | Imperative        | Declarative (React) |
| ----------- | ----------------- | ------------------- |
| Focus       | How to change DOM | What UI should be   |
| State sync  | Manual            | Automatic           |
| Consistency | Fragile           | Guaranteed          |
| Updates     | Redundant         | Minimal             |

- Virtual DOM: snapshot → diff → minimal patch → drift eliminated by design

---
