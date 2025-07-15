# Custom Utility Classes — _Behind the Scenes_
At its core, **Tailwind CSS** is just a large collection of **pre-defined CSS rules** mapped to tiny, predictable class names.

**Examples:**
``` css
/* A utility class for flexbox layout */
.flex {
  display: flex;
}

/* A utility class to center items along the cross axis */
.items-center {
  align-items: center;
}
```

**Using in HTML:**
``` html
<div class="flex items-center">
  <p class="items-center">Hello There!</p>
</div>
```

Notice:
- The structure is clear and semantic.
- You instantly know what each element is doing **just by reading the class names**.

---
# How It Works (In a Nutshell)
- Every Tailwind utility (e.g., `flex`, `items-center`, `p-4`) is:
    - A **single CSS rule**.
    - Generated automatically during build (with the JIT compiler).
- You get a consistent design language **without writing separate CSS files**.

---
# Why This Helps
- **No naming headache**: Forget inventing clever BEM names (`.header__nav--active`).
- **Focus on layout & design**, not on architecture of CSS files.
- **Rapid prototyping**: You can build and adjust UI live, in the browser.

---
# Why Not Use Inline CSS Styles Then?

|                         | Inline Styles                     | Tailwind CSS                          |
| ----------------------- | --------------------------------- | ------------------------------------- |
| Reusability             | ❌ Not reusable                    | ✅ Reusable utility classes            |
| Media queries           | ❌ Cannot write media queries      | ✅ Supports responsive utilities       |
| Pseudo classes          | ❌ Cannot write `:hover`, `:focus` | ✅ Easily add `hover:bg-blue-500` etc. |
| Consistency             | ❌ Prone to repetition             | ✅ Forces consistent design            |
| Build-time optimization | ❌ None                            | ✅ Generates minimal CSS               |

---
# Advanced: Custom Utilities & Composition
When you see repeating utility patterns, you can extract them:
``` css
/* In your CSS file */
.btn {
  @apply px-4 py-2 rounded bg-blue-600 text-white hover:bg-blue-700;
}
```
This keeps your HTML clean while retaining the flexibility of utilities.

---
