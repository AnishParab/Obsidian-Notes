# Difference Between Margin and Padding
``` lua
+-------------------------------+  ← margin (outside)
|   +-----------------------+   |  ← padding (inside)
|   |   Content goes here   |   |
|   +-----------------------+   |
+-------------------------------+
```

- **Margin** → creates space _outside_ the border.
- **Padding** → creates space _inside_ the border, between content and border.

---
# Margin
- Prefix: `m` (margin on all sides)
- Shorthands:
    - `mt-` → margin-top
    - `mb-` → margin-bottom
    - `ml-` → margin-left
    - `mr-` → margin-right
    - `mx-` → margin on horizontal axis (left & right)
    - `my-` → margin on vertical axis (top & bottom)

``` html
<div class="m-4">Margin on all sides</div>
<div class="mt-2 mb-4">Custom top & bottom margins</div>
<div class="mx-auto">Horizontally center using auto margins</div>
```

---
# Padding
- Prefix: `p` (padding on all sides)
- Shorthands:
    - `pt-` → padding-top
    - `pb-` → padding-bottom
    - `pl-` → padding-left
    - `pr-` → padding-right
    - `px-` → padding on horizontal axis
    - `py-` → padding on vertical axis

``` html
<div class="p-6">Padding on all sides</div>
<div class="px-4 py-2">Padding horizontally & vertically</div>
<div class="pl-8">Padding only on the left</div>
```

---
# Arbitrary Values
If you need a custom value not in the default scale:
``` html
<div class="mt-[13px]">Custom top margin</div>
<div class="p-[3.25rem]">Custom padding</div>
```

---
