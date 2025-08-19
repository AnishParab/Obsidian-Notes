# Color Value Types

| Type          | Example                   | Use Case                                            |
| ------------- | ------------------------- | --------------------------------------------------- |
| Named colors  | `red`, `blue`, `green`    | Quick, readable, limited set of 140+ colors.        |
| Hexadecimal   | `#ff0000`                 | Compact, widely used in design handoffs.            |
| RGB           | `rgb(255, 0, 0)`          | Good for fine-tuned colors using RGB channels.      |
| RGBA          | `rgba(255, 0, 0, 0.5)`    | Adds transparency via alpha channel.                |
| HSL           | `hsl(0, 100%, 50%)`       | Easier to tweak hue, saturation, lightness.         |
| HSLA          | `hsla(0, 100%, 50%, 0.5)` | HSL with transparency.                              |
| Current Color | `currentColor`            | Inherits the element’s `color` value automatically. |

---
### 1. **Named Colors**
- Example: `red`, `blue`, `darkgreen`
- Human-readable, built-in list of 140+ names.
- **Pros:** Quick for prototyping, no need to remember codes.
- **Cons:** Limited range, not precise enough for brand colors.

---
### 2. **Hexadecimal (`#RRGGBB`)**
- Example: `#ff0000` (red), `#0f0` (green shorthand)
- Uses hex values (00–FF) for red, green, and blue channels.
- **Pros:** Standard in design tools, compact.
- **Cons:** Harder to tweak without a color picker.

---
### 3. **RGB (`rgb(r, g, b)`)**
- Example: `rgb(255, 0, 0)`
- Uses decimal values (0–255) for red, green, and blue.
- **Pros:** Easy to manipulate dynamically in JavaScript.
- **Cons:** Not as human-friendly for color adjustments.

---
### 4. **RGBA (`rgba(r, g, b, a)`)**
- Example: `rgba(255, 0, 0, 0.5)` (50% transparent red)
- Same as RGB but adds **alpha** (0–1) for transparency.
- **Pros:** Color transparency without affecting children.
- **Cons:** Still less intuitive than HSL for hue changes.

---
### 5. **HSL (`hsl(h, s%, l%)`)**
- Example: `hsl(0, 100%, 50%)` (pure red)
- Hue (0–360° color wheel), Saturation (0–100%), Lightness (0–100%).
- **Pros:** Very intuitive for theme systems and adjusting brightness/saturation.
- **Cons:** Slightly less common in older codebases.

---
### 6. **HSLA (`hsla(h, s%, l%, a)`)**
- Example: `hsla(0, 100%, 50%, 0.5)` (semi-transparent red)
- Same as HSL but with **alpha transparency**.
- **Pros:** Combines easy adjustability with transparency control.

---
### 7. **`currentColor`**
- Example:
``` css
border-color: currentColor;

```
- Uses the element’s `color` property automatically.
- **Pros:** Great for consistent theming (icons, borders, outlines match text).
- **Cons:** Dependent on `color` being set somewhere.

---
