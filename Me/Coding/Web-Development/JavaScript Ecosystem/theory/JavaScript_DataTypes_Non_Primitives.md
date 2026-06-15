# Non-Primitives - Stored by Reference

- Stored by reference — variable holds a memory address, not the value.

``` js
object      // {}, [], functions, Date, Map, Set
```

---
### Expanded

``` js
// Object
{ key: "value" }

// Array
[1, 2, 3]                  // index-based, dynamic size

// Function
function fn() {}           // callable object

// Date
new Date()

// Map
new Map()                  // key-value, any key type, insertion order

// Set
new Set()                  // unique values only

// WeakMap / WeakSet
new WeakMap()              // keys must be objects, garbage-collectible

// RegExp
/pattern/gi

// Promise
new Promise((res, rej) => {})
```

---
