# `flex-wrap`
- Allows flex items to wrap onto multiple lines.

``` html
<div class="flex flex-wrap">...</div>

```

---
# `place-items-center`
- Shortcut for `justify-center items-center`

---
# `gap-*` vs `space-*`
| Utility     | Description                                | When to Use                   |
| ----------- | ------------------------------------------ | ----------------------------- |
| `gap-x-4`   | Horizontal gap between **grid/flex** items | Works on `flex` and `grid`    |
| `space-x-4` | Adds **margin between siblings only**      | Works only on direct children |
> `gap-*` is more consistent in **grid/flexbox layouts**; `space-*` applies actual margin.

---
# `flex-grow`, `flex-shrink`, `flex-auto`
Tailwind allows fine control over how flex items **expand or contract**.

| Class         | Description                               |
| ------------- | ----------------------------------------- |
| `flex-grow`   | Let item expand to fill remaining space   |
| `flex-shrink` | Allow item to shrink                      |
| `flex-none`   | Fixed size (won’t grow/shrink)            |
| `flex-1`      | Shortcut for `flex-grow + shrink + basis` |
| `basis-1/2`   | Set base size (e.g., 50% of parent)       |

``` html
<div class="flex">
  <div class="flex-1 bg-red-300 p-4">Expands</div>
  <div class="flex-none bg-green-300 p-4">Fixed</div>
</div>
```

---
# `self-*` (Per-item alignment)
Overrides the `items-*` setting **for a single child**.

| Class          | Description                       |
| -------------- | --------------------------------- |
| `self-auto`    | Default (inherits from container) |
| `self-start`   | Align to top                      |
| `self-center`  | Center vertically                 |
| `self-end`     | Align to bottom                   |
| `self-stretch` | Fill full height of container     |

``` html
<div class="flex items-center">
  <div class="self-start">Aligned Top</div>
  <div class="self-end">Aligned Bottom</div>
</div>
```

---
# `order-*` (Reorder flex items)
Tailwind supports reordering flex items visually.

| Class        | Description                    |
| ------------ | ------------------------------ |
| `order-1`    | This item appears 1st (lowest) |
| `order-2`    | Appears after `order-1`        |
| `order-last` | Push to end                    |

``` html
<div class="flex">
  <div class="order-2">Second</div>
  <div class="order-1">First</div>
</div>
```

---


