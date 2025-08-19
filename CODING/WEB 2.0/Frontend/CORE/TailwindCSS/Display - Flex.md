# Flexbox Utilities
##  `flex`
- Enables flexbox on the container.
- Children become **flex items**.

## `flex-row` _(default)_
- Items are laid out **horizontally** (left to right).

## `flex-col`
- Items are laid out **vertically** (top to bottom).

---
# `justify-*` — **Horizontal Alignment**
| Class             | Description                    |
| ----------------- | ------------------------------ |
| `justify-start`   | Align items to the left        |
| `justify-center`  | Center items horizontally      |
| `justify-end`     | Align items to the right       |
| `justify-between` | Equal spacing between items    |
| `justify-around`  | Equal spacing around each item |
| `justify-evenly`  | Even spacing including edges   |

---
# `items-*` — **Vertical Alignment**
| Class            | Description                  |
| ---------------- | ---------------------------- |
| `items-start`    | Align to top of container    |
| `items-center`   | Vertically center items      |
| `items-end`      | Align to bottom of container |
| `items-stretch`  | Stretch items to fill height |
| `items-baseline` | Align items by text baseline |

---
# Spacing Between Flex/Grid Items
## `space-x-*` → Horizontal spacing between children
``` html
<div class="flex space-x-6">
  <div>Item 1</div>
  <div>Item 2</div>
</div>
```

## `space-y-*` → Vertical spacing between children
``` html
<div class="flex flex-col space-y-4">
  <div>Item 1</div>
  <div>Item 2</div>
</div>
```

> Works only on **direct children**, not nested elements.

---
