# What ?
The **universal selector** (`*`) targets **all elements** on the page, regardless of type.

---
# Syntax
``` css
* {
  margin: 0;
  padding: 0;
}
```

---
# Use-Case
| Use Case            | Why                                                               |
| ------------------- | ----------------------------------------------------------------- |
| **CSS Reset**       | Remove default browser styles (user agent stylesheets).           |
| **Global Styling**  | Apply base styles like `box-sizing: border-box;` to all elements. |
| **Quick Debugging** | Temporarily add borders or backgrounds to see element layout.     |

---
# Notes
- It matches **every element** in the DOM, including pseudo-elements like `::before` and `::after`.
- Can be combined with other selectors (e.g., `*.className`).
- **Performance Tip:** Avoid heavy styles in `*` for large pages — it affects rendering speed.

---
