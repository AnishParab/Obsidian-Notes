# **Important Note**
> To style something for mobile, you need to use the unprefixed version of a utility, not the `sm: ` prefixed version.

> `sm:grid-cols-3` ---> **This just means that smaller and above screens ko 3 grid column lagta hai.**

---
# Responsive Prefixes
| Prefix | Breakpoint     | Min Width |
| ------ | -------------- | --------- |
| `sm:`  | Small devices  | `640px`   |
| `md:`  | Medium devices | `768px`   |
| `lg:`  | Large devices  | `1024px`  |
| `xl:`  | Extra large    | `1280px`  |
| `2xl:` | 2x extra large | `1536px`  |

---
# **Example**
``` html
<div class="sm:mt-4 md:px-6 lg:mb-8">
  <!-- Adjusts margin and padding based on screen size -->
</div>
```

---
# **Example**
``` html
<div class="text-base sm:text-lg md:text-xl lg:text-2xl">
  Responsive Text
</div>
```
###  What Happens Here:
- `text-base`: applied **on all screens**
- `sm:text-lg`: overrides on ≥640px
- `md:text-xl`: overrides on ≥768px
- `lg:text-2xl`: overrides on ≥1024px

---