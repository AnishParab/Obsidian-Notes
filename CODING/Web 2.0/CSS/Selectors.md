# What are Selectors
- **Selectors** in CSS are patterns used to **target HTML elements** for styling.

---
# Element
- Targets **all elements** of a specific type.
``` css
p {
  color: blue;
}
```
- Applies to all the `<p>` tags on the page.

---
# Id
- Targets a **single unique element** with a given `id`.
- Use `#`
- **High Specificity**.
``` html
<p id="main-text">Hello</p>
```

``` css
#main-text {
  font-weight: bold;
}
```

---
# Class
- Targets **one or more elements** that share the same class.
- Preferred over `id` for **reusability**.
- Use `.`
``` html
<p class="highlight">Text 1</p>
<p class="highlight">Text 2</p>
```

``` css
.highlight {
  background-color: yellow;
}
```

---
# Group
- Targets **multiple selectors** with the **same style rules**.
- Syntax: `selector1, selector2 { ... }`.
- Reduces repetition in your CSS.
``` css
h1, h2, p {
  font-family: Arial, sans-serif;
}
```

---
