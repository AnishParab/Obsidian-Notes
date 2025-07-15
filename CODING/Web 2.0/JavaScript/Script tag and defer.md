This tag in HTML, is used to embed or reference Javascript code.

---
# Usage
``` html
<script> 
  // Inline JS code here
</script>
```
OR
``` html
<script src="script.js"></script>
```

---
# Placement in HTML
### In the `<head>`
``` html
<head>
  <script src="script.js"></script>
</head>
```
- Loads Early.
- Might be a bottleneck if it's not async deferred.

### At the end of `<body>`
``` html
<body>
  <!-- content -->
  <script src="script.js"></script>
</body>
```
- Common pattern.
- DOM is loaded before JS runs.
- Can't interact with `<head>` elements immediately.

---
# `src` attribute
Source of external JS file.
``` html
<script src="/assets/js/app.js"></script>
```
Loads external JS file. Blocks HTML parsing unless `async` or `defer` is used.

---
# `defer` VS `async`
``` html
<script src="main.js" defer></script>
<script src="main.js" async></script>
```
#### without any attributes
- Html Parsing ---> Parsing Stopped ---> Script Data Fetched ---> Script Executed ---> Parsing Resumed.
#### async
- Html Parsing ---> Pauses while execution ---> Resumes after execution---> Html parsing complete
- Data Fetching asynchronously while parsing ---> Once done, it executes
#### defer
- Html Parsing ---> Html Parsing Complete
- Data Fetching asynchronously while parsing ---> After parsing completion, script is executed

## When to use what
-  `async` does not guarantee the order of execution of scripts, but `differ` does.

---
# Attribute `type="module"`
This allows to use **ES6 import/export** syntax.
``` html
<script type="module" src="main.js"></script>
```
In `main.js`
``` js
import { sayHi } from './utils.js';

sayHi();
```
#### Benefits
- Module scoped variables (not global).
- Support for `import/export`.
- `defer` behavior by  default.

---
# Attribute `nomodule`
For legacy browser support.
``` html
<script src="main.legacy.js" nomodule></script>
<script type="module" src="main.js"></script>
```
1. `main.legacy.js`  ---> For older browsers.

---
# Best Practices
1. Multiple scripts with order ---> Use `defer` not `async`
2. Third-party analytics or ads ---> Use `async`

---
