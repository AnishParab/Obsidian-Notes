# Ways to Add CSS
- Inline
- Internal
- External

**Priority Order**:
``` csS
Inline → Internal → External 
```

---
# Inline-CSS
- Written **directly on the element** using the `style` attribute.
- **Highest priority**, but **bad practice** due to:
    - Poor maintainability
    - Lack of separation between content and style
``` html
<p style="color: red;">This is inline CSS</p>
```

---
# Internal-CSS
- Written inside a `<style>` tag **within the HTML `<head>`**.
- Good for **single-page** applications or small projects.
- Still not scalable for larger sites.
``` html
<head>
  <style>
    p {
      color: green;
    }
  </style>
</head>
```

---
# External-CSS
- CSS is stored in a **separate `.css` file** and linked using the `<link>` tag.
- Best practice for **clean architecture** and **scalability**.
``` html
<!-- index.html -->
<link rel="stylesheet" href="styles.css">
```

``` css
/* styles.css */
p {
  color: blue;
}
```

---
