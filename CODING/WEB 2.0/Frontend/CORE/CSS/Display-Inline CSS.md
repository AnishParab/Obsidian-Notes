# What is `display: inline`?
- A **CSS display value** where an element flows **in line with surrounding text/content**.
- **Does not** start on a new line.
- **Ignores** `width` and `height` properties (but still respects horizontal padding/margin).
- **Ignores** custom **margins**.

---
# Common Inline Elements

| Tag        | Example Use          |
| ---------- | -------------------- |
| `<span>`   | Styling part of text |
| `<a>`      | Hyperlinks           |
| `<strong>` | Bold text            |
| `<em>`     | Italic text          |
| `<label>`  | Form labels          |
| `<abbr>`   | Abbreviations        |

---
# Key Characteristics of Inline Elements
| Behavior                                 | Description                                           |
| ---------------------------------------- | ----------------------------------------------------- |
| **Flows with text**                      | Positioned alongside other inline elements.           |
| **No forced line break**                 | Continues on the same line until wrapping naturally.  |
| **Width/height ignored**                 | Cannot explicitly set `width`/`height`.               |
| **Respects padding/margin (horizontal)** | Vertical padding/margin has minimal effect on layout. |

---
# Example
``` css
span {
  display: inline;
  background: yellow;
}
```

---
