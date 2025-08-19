# **Example :** Base Layer
``` css
@layer base {
  h1 {
    @apply text-4xl font-bold text-gray-800;
  }
  body {
    @apply bg-gray-50 text-gray-900;
  }
}
```

---
# **Example :** Reusable Component
``` css
@layer components {
  .btn-primary {
    @apply bg-blue-600 text-white py-2 px-4 rounded-md hover:bg-blue-700;
  }
}
```

``` html
<button class="btn-primary">Submit</button>

```

---
# **Example :** Custom Utility
``` css
@layer utilities {
  .bg-glass {
    backdrop-filter: blur(10px);
    background-color: rgba(255, 255, 255, 0.2);
  }
}
```

``` html
<div class="bg-glass p-4 rounded-xl">Frosted Glass</div>

```

---
