# Adding / Removing Elements
``` js
let arr = [1, 2, 3];
arr.push(4);      // [1, 2, 3, 4]
arr.pop();        // [1, 2, 3]

arr.unshift(0);   // [0, 1, 2, 3]
arr.shift();      // [1, 2, 3]
```

> **`push()`** is faster than `unshift()` (adding to start forces reindexing).

---
# Splicing and Slicing
``` js
let arr = [1, 2, 3, 4, 5];

arr.splice(2, 1, 99); // Remove 1 elem at index 2, insert 99 → [1, 2, 99, 4, 5]

let sub = arr.slice(1, 3); // Copy elements → [2, 99]
```

---
# Searching
``` js
let arr = ["a", "b", "c"];
arr.indexOf("b");   // 1
arr.includes("c");  // true
```

---
# Combining & Joining
``` js
let arr1 = [1, 2];
let arr2 = [3, 4];
let merged = arr1.concat(arr2); // [1, 2, 3, 4]

["a", "b", "c"].join("-"); // "a-b-c"
```

---
