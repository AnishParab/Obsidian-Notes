# What ?
The `box-sizing` property decides **how CSS calculates an element’s total width and height**.

---
# Default Behavior (`content-box`)
- **Width & height** apply **only to the content area**.
- Padding and border are **added on top** of that size → element becomes **bigger** than you expect.

Example :
``` css
width: 200px;
padding: 20px;
border: 5px solid;
```
- Final width = **200 + 40 (padding) + 10 (border) = 250px**.

---
# `border-box` behavior 
- **Width & height** include **content + padding + border**.
- Keeps the element’s total size consistent, even if you add padding or borders.

Example :
``` css
width: 200px;
padding: 20px;
border: 5px solid;
box-sizing: border-box;
```
- Final width = **200px total** (content shrinks to fit padding & border).

---
