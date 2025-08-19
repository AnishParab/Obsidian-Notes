# Min & Max Width/Height Utilities
### **Min Width (`min-w-`)**
| Class           | Description                         |
| --------------- | ----------------------------------- |
| `min-w-0`       | No minimum width                    |
| `min-w-full`    | 100% width                          |
| `min-w-min`     | Fit to content (min size)           |
| `min-w-max`     | Fit to content (max size)           |
| `min-w-[value]` | Custom width (e.g. `min-w-[200px]`) |

``` html
<div class="min-w-[300px] bg-gray-100">Minimum 300px wide</div>

```

---
### **Max Width (`max-w-`)**
| Class               | Description                       |
| ------------------- | --------------------------------- |
| `max-w-none`        | No max width                      |
| `max-w-full`        | Max width = 100% of parent        |
| `max-w-sm`          | ~24rem (384px)                    |
| `max-w-md`          | ~28rem (448px)                    |
| `max-w-lg`          | ~32rem (512px)                    |
| `max-w-xl`          | ~36rem (576px)                    |
| `max-w-2xl` → `7xl` | Larger sizes (~640px → 80rem)     |
| `max-w-screen-sm`   | Match screen breakpoint (`640px`) |
| `max-w-[value]`     | Custom size (`max-w-[80ch]`)      |

``` html
<div class="max-w-lg mx-auto">Centered, limited to 512px max</div>

```

---
### **Min Height (`min-h-`)** and **Max Height (`max-h-`)**
| Class                      | Description                    |
| -------------------------- | ------------------------------ |
| `min-h-0`                  | No min height                  |
| `min-h-full`               | 100% height                    |
| `min-h-screen`             | 100vh (entire viewport height) |
| `max-h-0` → `max-h-screen` | From `0` to full screen        |
| `min-h-[value]`            | Custom: `min-h-[40px]`         |

``` html
<div class="min-h-screen flex items-center justify-center">
  Full height center
</div>
```

---
# Combine with Responsive Prefixes
``` html
<div class="max-w-sm sm:max-w-md md:max-w-xl lg:max-w-2xl">
  Responsive container
</div>
```

---
