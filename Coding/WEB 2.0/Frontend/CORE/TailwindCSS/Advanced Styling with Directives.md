# What are Directives ?
These are **Tailwind-specific directives** that allow you to:
- Organize your CSS layers (`base`, `components`, `utilities`)
- Write reusable and clean CSS
- Extend Tailwind's behavior
- Add custom variants/utilities
- Use Tailwind inside traditional CSS workflows

---
# `@import` Directive
- Used to bring Tailwind into your CSS file.
``` css
@import "tailwindcss";

```
OR
``` css
@import "tailwindcss/base";
@import "tailwindcss/components";
@import "tailwindcss/utilities";
```

---
# `@layer` Directive
- Defines which _layer_ (base, components, utilities) your styles belong to.
### `base` 
- Applies global resets and HTML element styles.
``` css
@layer base {
  h1 {
    font-size: 2rem;
    color: green;
  }
}
```

### `components`
- Reusable UI patterns like cards, buttons.
``` css
@layer components {
  .card {
    @apply p-6 bg-white rounded-lg shadow-lg;
  }
}
```

### `utilities`
- Custom atomic classes.
``` css
@layer utilities {
  .content-auto {
    content-visibility: auto;
  }
}
```

---
# `@apply` Directive
- Lets you use Tailwind utility classes _inside_ your custom CSS.
``` css
.button {
  @apply bg-blue-500 text-white py-2 px-4 rounded-lg hover:bg-blue-600;
}
```
Great for:
- Avoiding repetition
- Making semantic class names
- Keeping HTML clean

---
# `@custom-variant` Directive
- Defines a **custom variant**, like `dark:` or `hover:` but personalized.
``` css
@custom-variant fancy (&:where(.fancy, .fancy *));

```

``` html
<div class="fancy:bg-pink-200">Hello!</div>

```

> **NOTE :** Needs PostCSS plugin setup `tailwindcss/plugin`

---
# `@theme` Directive
- Access values from your Tailwind config inside custom CSS.
``` css
.title {
  color: theme('colors.primary');
  padding: theme('spacing.4');
}
```
- Use this for dynamic styles linked to your design tokens.

---
# `@variants` Directive
- (Deprecated in newer versions)
Used earlier to define custom variants (now replaced by plugins or `@custom-variant`).

---
# `@utilities` / `@components` / `@base`
- Same as `@layer`, older naming style.
- Modern recommendation: use `@layer`.
``` css
@utilities {
  .my-shadow {
    box-shadow: 0 2px 10px rgba(0,0,0,0.3);
  }
}
```

---
# `@source`
Used internally by Tailwind plugins. You rarely need this.

---
# `@reference`
A draft CSS spec (not widely supported); not needed in Tailwind as of now.

---
