# Component Model
- UI is decomposed into **isolated, reusable building blocks**. Each component is a self-contained unit of logic and presentation.
### Component Anatomy
- **Props (Inputs)**: Immutable data passed from parent to child.
- **State (Internal)**: Private data managed within the component.
- **Output**: Returns a description of the UI (JSX).
### Core Benefits
1. **Local Reasoning**: You only need to understand the file you are looking at.
2. **Predictability**: Same props + same state = same UI.
3. **Composition**: Build complex systems by nesting simple components.

---
