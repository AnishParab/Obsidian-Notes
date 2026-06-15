# Props Down, Events Up

## Core Rule

- **Data flows down**
- **Actions flow up**

---
## 1. Props (Downward)

- Parent → Child
- Read-only
- Child cannot mutate props
- Shared data lives in closest common parent

---
## 2. Events (Upward)

- Parent passes callback to child
- Child calls callback on interaction
- Parent updates state
- New props flow down

---
## Engineering Value

- **Predictable state changes**
- **Easy debugging** (trace upward)
- **Loose coupling** (child triggers action, not logic)

---
## Contrast: Two-Way Binding

- Data flows both directions
- Less boilerplate
- Harder to reason about
- Side effects spread across tree

---
## Summary

- React enforces one-way data flow
- Fewer hidden mutations
- Higher reliability at scale

---
