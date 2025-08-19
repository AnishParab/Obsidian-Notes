---

---
# `<script>` Tag in HTML

The `<script>` tag is used to embed or reference **JavaScript** code inside an HTML document.

### Inline and External JS
``` html
<!-- Inline JavaScript -->
<script>
  // Your JavaScript code here
</script>

<!-- External JavaScript File -->
<script src="script.js"></script>
```
- If `src` is used, the inner script block is ignored.

---
## Placement of `<script>` tag in HTML

### **In the `<head>` tag**
``` html
<head>
  <script src="script.js"></script>
</head>
```
- **Loads before DOM is constructed.**
- May block rendering unless `async` or `defer` is used.
- **Not ideal for performance** without deferral.

---
### **At the end of `<body>` tag**
``` html
<body>
  <!-- Page content -->
  <script src="script.js"></script>
</body>
```
- DOM is parsed **before** the script executes.
- Safer to manipulate DOM without `DOMContentLoaded`.
- Most common pattern if `defer` is not used.

---
# Attributes of `<script>` Tag
## `src`
- Specifies the **source** of an external script.
``` html
<script src="/assets/js/app.js"></script>

```
- **Blocks parsing** until the script is downloaded and executed (unless `async`/`defer` is used).

---
## `async` vs `defer`

| Feature                   | `async`                         | `defer`                       |
| ------------------------- | ------------------------------- | ----------------------------- |
| **Downloads in parallel** | ✅ Yes                           | ✅ Yes                         |
| **Execution order**       | ❌ No guarantee                  | ✅ Preserves order             |
| **Execution timing**      | As soon as downloaded           | After DOM parsing is complete |
| **HTML parsing pause**    | Yes (during execution)          | No                            |
| **Use case**              | Independent scripts (analytics) | Dependent, ordered scripts    |

#### **Diagram**
![[defer_async.excalidraw|1000]]

---
##  `type="module"`
- Enables **ES6 module syntax** (`import` / `export`) and scoped script execution.
``` html
<script type="module" src="main.js"></script>

```
- In `main.js`:
``` js
import { greet } from './utils.js';
greet();
```
#### **Benefits:**
- Automatically **deferred** (no need to add `defer`).
- Supports modern **JavaScript modules**.
- Module-scoped: variables don't pollute global scope.

---
## `nomodule`
- Used with `type="module"` to provide fallback for older browsers.
``` html
<script src="main.legacy.js" nomodule></script>
<script type="module" src="main.js"></script>
```
- Older browsers ignore `type="module"` and run `nomodule` script.
- Modern browsers **ignore `nomodule` scripts** if they understand modules.

---
# Best Practices
1. Use `defer` for multiple scripts to maintain execution order.
2. Use `async` for third-party or independent scripts (e.g., ads, analytics).
3. Avoid placing non-deferred `<script>` in `<head>` unless absolutely necessary.
4. Prefer `type="module"` for modern development with ES6 features.
5. Avoid mixing inline and external scripts with the same `<script>` tag.

---

