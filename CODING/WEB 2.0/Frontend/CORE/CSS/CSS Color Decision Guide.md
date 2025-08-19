# Color Decision Guide

| Format                          | Best Used For                                               | Why/When to Choose                                                                           |
| ------------------------------- | ----------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| **Named Colors**                | Quick prototypes, simple UI                                 | Easy to read (`red`, `blue`), but limited palette.                                           |
| **Hex (`#RRGGBB`)**             | Design-to-code handoffs, brand colors                       | Common in design tools (Figma, Photoshop). Compact, but less human-readable for adjustments. |
| **RGB (`rgb(r, g, b)`)**        | Digital screens, programmatic color changes                 | Explicitly defines red/green/blue channels (0–255). Easy for JavaScript manipulation.        |
| **RGBA (`rgba(r, g, b, a)`)**   | When you need transparency on just the color                | Alpha channel controls opacity **of the color only**, not the whole element.                 |
| **HSL (`hsl(h, s%, l%)`)**      | Theme systems, color tweaking                               | More intuitive to adjust hue, saturation, and lightness separately.                          |
| **HSLA (`hsla(h, s%, l%, a)`)** | Transparent themes or layered UI                            | Combines HSL’s adjustability with alpha transparency.                                        |
| **`currentColor`**              | Icons, borders, or decorations that should match text color | Automatically inherits the element’s `color` property.                                       |

---
