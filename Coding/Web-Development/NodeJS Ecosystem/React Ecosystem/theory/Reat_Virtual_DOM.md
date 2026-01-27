# The Virtual DOM Workflow

React doesn't update the entire UI on every change. It follows a three-step process to ensure high-performance updates:

1. **Render:** Generates a lightweight JavaScript object representation of the UI (Virtual DOM).
2. **Diffing:** When state changes, React compares the new VDOM with a snapshot of the previous one.
3. **Reconciliation:** Only the differences (the "diff") are patched into the real Browser DOM.

> [!important] Performance Myth
> 
> The VDOM isn't "faster" than the browser DOM. Its real value is **providing a declarative API** while maintaining _sufficient_ performance through batching and minimal updates.

---
