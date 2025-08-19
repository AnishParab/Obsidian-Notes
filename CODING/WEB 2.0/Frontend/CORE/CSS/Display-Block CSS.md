# What is `display: block`?
- A **CSS display value** that makes an element behave like a **block-level element**.
- The element **takes up the full width** available and **starts on a new line**.

---
# Common Block Elements
| Tag                     | Example Use        |
| ----------------------- | ------------------ |
| `<div>`                 | Layout containers  |
| `<p>`                   | Paragraphs         |
| `<h1>`–`<h6>`           | Headings           |
| `<section>`             | Page sections      |
| `<header>` / `<footer>` | Page header/footer |
| `<ul>`, `<ol>`          | Lists              |

---
# Key Characteristics of Block Elements

| Behavior               | Description                                        |
| ---------------------- | -------------------------------------------------- |
| **Full width**         | Expands to fill parent container width by default. |
| **New line**           | Always starts on a new line.                       |
| **Supports box model** | Can set `width`, `height`, `margin`, `padding`.    |
| **Stacks vertically**  | Flows from top to bottom in normal document flow.  |

---
# Example
``` css
div {
  display: block;
  background: lightblue;
}
```

---
