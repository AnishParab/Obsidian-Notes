# Dark Mode Based on System Preferences
- Tailwind will automatically apply dark mode if the system theme is set to **dark**.
``` html
<div class="bg-white dark:bg-black text-black dark:text-white">
	Hello There!
</div>
```

---
# Dark Mode Toggle via Button (Manual Control)
### Step 1: Override the Dark Variant
Add this to your CSS (if using Tailwind CLI or PostCSS):
``` css
@import "tailwindcss";

@custom-variant dark (&:where(.dark, .dark *));
```
- This ensures that the `.dark` class on the root element enables dark mode.

### Step 2: HTML Example
``` html
<div class="m-10 rounded-lg bg-white px-6 py-8 shadow-xl ring-1 ring-slate-900/5 dark:bg-black">
  <h3 class="text-base font-medium tracking-tight text-slate-900 dark:text-white">
    Writes Upside-Down
  </h3>
  <p class="mt-2 text-sm text-slate-500 dark:text-blue-100">
    The Zero Gravity Pen can be used to write in any orientation, including upside-down. It even works in outer space.
  </p>

  <button
    id="toggleDark"
    class="mt-8 px-4 py-2 text-sm font-medium text-blue-900 bg-blue-100 rounded-md"
  >
    Toggle Dark Mode
  </button>
</div>
```

### Step 3: JavaScript Logic
``` html
<script>
  document.addEventListener("DOMContentLoaded", () => {
    const toggleDark = document.getElementById('toggleDark');
    toggleDark.addEventListener('click', () => {
      document.documentElement.classList.toggle('dark');
    });
  });
</script>
```

- `document.documentElement` → Refers to `<html>` tag  
- Adds or removes `dark` class dynamically.

---
# Alternative: Using Data Attributes
- Instead of adding a `.dark` class, you can use a **data attribute**.
``` css
@import "tailwindcss";

@custom-variant dark (&:where([data-theme=dark], [data-theme=dark] *));
```

- Then Toggle Like This
``` html
document.documentElement.setAttribute('data-theme', 'dark');
// or remove it for light mode
```

---
