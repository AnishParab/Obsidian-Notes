# Data Transfer Between Components
- React uses **top-down data flow**, meaning data is passed from **parent --> child**.
- Use **props**, short for properties.
- Props are _read only_, meaning child components cannot modify them.

---
# Why use Props?
- Cleanest way of data transfer.
- A code without props looks like this:
``` jsx
function Greet({ name, age }) {
  return <h3>{name} is {age} years old</h3>;
}
```
- Here, instead of `props.name` or `props.age`, _name_ and _age_ are passed singularly.

---
# One-Way Data Flow
- Props always flow from parent --> child.
- Data flow from child --> parent requires **callbacks**.

---
