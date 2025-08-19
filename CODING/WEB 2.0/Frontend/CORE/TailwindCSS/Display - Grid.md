# Grid System
- Tailwind’s `grid` utilities let you create powerful **2D layouts** with precise control over **columns, rows, gaps, and item alignment**.

---
# Enabling Grid Layout
``` html
<div class="grid">
  <!-- Grid items here -->
</div>
```

---
# `grid-cols-*`: Number of Columns
| Class         | Columns              |
| ------------- | -------------------- |
| `grid-cols-1` | 1 column             |
| `grid-cols-2` | 2 columns            |
| `grid-cols-3` | 3 columns            |
| ...           | up to `grid-cols-12` |

``` html
<div class="grid grid-cols-3 gap-4">
  <div class="bg-blue-200">1</div>
  <div class="bg-blue-300">2</div>
  <div class="bg-blue-400">3</div>
</div>
```

---
# Column Width Shortcuts
| Class                                            | Description                         |
| ------------------------------------------------ | ----------------------------------- |
| `grid-cols-none`                                 | No grid columns                     |
| `grid-cols-auto`                                 | Auto size based on content          |
| `grid-cols-[repeat(auto-fit,minmax(200px,1fr))]` | Responsive column template (custom) |

---
# Gaps Between Rows & Columns
| Class     | Description                        |
| --------- | ---------------------------------- |
| `gap-4`   | Uniform gap between rows & columns |
| `gap-x-6` | Horizontal column gap only         |
| `gap-y-2` | Vertical row gap only              |

``` html
<div class="grid grid-cols-2 gap-x-8 gap-y-4">
  <div>1</div>
  <div>2</div>
  <div>3</div>
  <div>4</div>
</div>
```

---
# Grid Row Utilities
| Class         | Description             |
| ------------- | ----------------------- |
| `grid-rows-2` | Defines 2 rows          |
| `row-span-2`  | Span item across 2 rows |
| `row-start-2` | Start item at row 2     |

``` html
<div class="grid grid-cols-2 grid-rows-2 gap-2">
  <div class="row-span-2 bg-green-300">Tall Item</div>
  <div class="bg-yellow-200">Small</div>
  <div class="bg-yellow-300">Small</div>
</div>
```

---
# Aligning Items
## Align Items in Grid
| Class           | Description                     |
| --------------- | ------------------------------- |
| `items-start`   | Align items to top              |
| `items-center`  | Align items vertically centered |
| `items-end`     | Align items to bottom           |
| `items-stretch` | Default — stretch to fill       |

---
## Justify Items Horizontally
| Class             | Description           |
| ----------------- | --------------------- |
| `justify-start`   | Align to the left     |
| `justify-center`  | Centered horizontally |
| `justify-end`     | Align to the right    |
| `justify-between` | Even spacing between  |

---
# Responsive Grid Example
``` html
<div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4 p-4">
  <div class="bg-blue-200 p-4 rounded">Box 1</div>
  <div class="bg-blue-300 p-4 rounded">Box 2</div>
  <div class="bg-blue-400 p-4 rounded">Box 3</div>
  <div class="bg-blue-500 p-4 rounded">Box 4</div>
</div>
```

- 📱 1 column on mobile
- 💻 2 columns on `sm`
- 🖥 4 columns on `lg`

---
