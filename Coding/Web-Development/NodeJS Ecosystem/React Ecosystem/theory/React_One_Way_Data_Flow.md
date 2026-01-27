# The "Props Down, Events Up" Pattern

- In a React hierarchy, the relationship between a Parent and Child component is strictly regulated:

---
### 1. Data Flows Down (Props)

Parents pass data to their children via **Props**.

- **Read-Only:** Props are immutable. A child component cannot modify the props it receives.
- **Source of Truth:** If three components need the same piece of data, that data should live in their closest common ancestor (Lifting State Up).

---
### 2. Events Flow Up (Callbacks)

Since children cannot change their own props, they must "ask" the parent to change the state.

- **Communication:** The parent passes a **function** (callback) down as a prop.
- **Execution:** When a user interacts with the child (e.g., clicks a button), the child executes that function.
- **Update:** The parent updates its local state, which triggers a re-render, sending new props back down the chain.

---
# Why this matters for Engineering

| **Benefit**          | **Explanation**                                                                                                                                         |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Predictability**   | You always know where a state change originated. If a value is wrong, you only need to look "up" the component tree.                                    |
| **Easier Debugging** | Using tools like React DevTools, you can trace the data path. There are no "side-effects" where a child secretly changes a parent's variable.           |
| **Decoupling**       | Components become more modular. A `Button` component doesn't need to know _what_ it's changing; it just knows it needs to call a function when clicked. |

---
# The Contrast: Two-Way Binding

- In older frameworks (like AngularJS), data could flow both ways. If a child changed a value, it automatically updated the parent. While this required less code, it created "Side Effect Spaghetti," where changing a value in one corner of the app could unexpectedly break a distant, unrelated component.

---
