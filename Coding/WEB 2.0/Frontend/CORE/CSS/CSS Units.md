# CSS Units

| Unit   | Best Used For                                 | Why/When to Use                                                                           |
| ------ | --------------------------------------------- | ----------------------------------------------------------------------------------------- |
| `px`   | Borders, icons, small fixed UI elements       | Precise and consistent size, unaffected by parent or root font-size.                      |
| `em`   | Typography that scales with **parent**        | Flexible but can compound if nested (be careful).                                         |
| `rem`  | Typography, spacing, layouts                  | Consistent scaling based on **root font-size** (commonly `16px`). Best for accessibility. |
| `%`    | Widths, heights, font-size relative to parent | Great for fluid layouts; adapts to parent container.                                      |
| `vw`   | Full-width sections, responsive font sizes    | Scales with viewport width for fluid designs.                                             |
| `vh`   | Full-height sections (hero banners, modals)   | Fills the screen height regardless of content.                                            |
| `vmin` | Responsive squares or circles                 | Adapts to the smaller viewport dimension.                                                 |
| `vmax` | Responsive backgrounds or hero sections       | Adapts to the larger viewport dimension.                                                  |

---
