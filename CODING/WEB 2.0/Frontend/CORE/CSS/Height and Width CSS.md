# Height and Width

| Property     | Use Case                                                  |
| ------------ | --------------------------------------------------------- |
| `width`      | Defines the horizontal size of an element’s content area. |
| `height`     | Defines the vertical size of an element’s content area.   |
| `min-width`  | Sets the smallest possible width for an element.          |
| `max-width`  | Sets the largest possible width for an element.           |
| `min-height` | Sets the smallest possible height for an element.         |
| `max-height` | Sets the largest possible height for an element.          |

---
# Why `height` & `width` don’t work on `<span>` by default
- **`<span>` is an inline element** by default.
- Inline elements **do not respect height and width** properties — their size depends on their text/content.
- They only respect **horizontal padding** and **margin**; vertical padding/margin won’t push other elements away.

---
# Make `<span>` accept height & width
Set `display` to :
``` css
display: inline-block; /* keeps inline flow but allows height & width */

```

or

``` css
display: block; /* breaks onto a new line, full width by default */

```

---
