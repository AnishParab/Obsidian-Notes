# What is `position` in CSS?

The `position` property defines **how an element is positioned** in the document flow — either relative to its **normal position**, its **parent**, or the **viewport**.

> Used with `top`, `right`, `bottom`, and `left` to control exact placement.

---
# Types of CSS Positioning

### `static` _(default)_
- The default position — elements flow normally in the document.
- You **cannot use `top/right/bottom/left`** with `static`.
``` html
<div class="static">I follow the normal flow.</div>

```

### `relative`
- Moves the element **relative to its original position**.
- **Space is still reserved** in the document flow.
``` html
<div class="relative top-2 left-4">Moved from original position</div>

```

### `absolute`
- Removes the element from normal flow.
- Positions it **relative to the nearest parent with `relative`, `absolute`, or `fixed`**.
- No space is reserved for the element.
``` html
<div class="relative">
  <div class="absolute top-0 right-0">Absolutely positioned inside parent</div>
</div>
```

### `fixed`
- Positions the element **relative to the viewport**.
- It **stays in place** even when scrolling.
``` html
<div class="fixed top-0 left-0">Always visible at top-left</div>

```
**Example** ---> For a Navbar, `top-0` and `w-full` is important. 

### `sticky`
- Behaves like `relative` **until a scroll threshold is passed**, then sticks to that position.
- Needs a parent with **enough height** and proper scroll context.
``` html
<div class="sticky top-0 bg-white">Sticky Header</div>

```

---