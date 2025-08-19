# Syntax
- Tailwind uses `display-*` classes to control **element layout behavior**.

---
# Display Types

### `block`
- The element **takes up full width** of its container.
- Starts on a new line.
``` html
<div class="block">Block Element</div>

```

### `inline`
- Behaves like text (sits inline with other content).
- **Width & height can’t be set** directly.
``` html
<span class="inline">Inline Text</span>

```

### `inline-block`
- Behaves like `inline`, **but allows width and height**.
``` html
<span class="inline-block w-32 h-10 bg-blue-200">Boxy Inline</span>

```

### `flex`
- Turns an element into a **flex container**.
- Required for using all `justify-*`, `items-*`, and `flex-col` utilities.
``` html
<div class="flex">Flex container</div>

```

### `grid`
- Enables CSS **grid layout** system.
- Use with `grid-cols-*`, `gap-*`, etc.
``` html
<div class="grid grid-cols-3 gap-4">Grid layout</div>

```

---
