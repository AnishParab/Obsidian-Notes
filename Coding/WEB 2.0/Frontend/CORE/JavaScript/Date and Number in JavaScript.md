# Date
- With **new** :
``` js
let now = new Date();
console.log(now); // Date object with current time
```

- Without **new** :
``` js
console.log(Date());
// e.g., "Sun Aug 10 2025 20:45:13 GMT+0000 (Coordinated Universal Time)"
```

- Date Constructor Variations :
``` js
new Date(); // current date/time
new Date(2025, 7, 10); // Aug 10, 2025 (month is 0-based)
new Date("2025-08-10T15:00:00Z"); // from string
new Date(1691692800000); // from milliseconds since epoch
```

- Useful methods :
``` js
let d = new Date();
d.getFullYear(); // 2025
d.getMonth();    // 0-11
d.getDate();     // 1-31
d.toISOString(); // "2025-08-10T15:00:00.000Z"
```

---
# Number
- The **`Number`** function handles numeric conversion and the Number object wrapper.

- Without **new** :
``` js
Number("42");   // 42
Number(true);   // 1
Number(false);  // 0
Number("3.14"); // 3.14
Number("");     // 0
Number(null);   // 0
Number(undefined); // NaN
```

- With **new** :
``` js
let numObj = new Number(42);
console.log(typeof numObj); // "object"
```

- Special Values :
``` js
Number.MAX_SAFE_INTEGER;  // 9007199254740991
Number.MIN_SAFE_INTEGER;  // -9007199254740991
Number.POSITIVE_INFINITY; // Infinity
Number.NEGATIVE_INFINITY; // -Infinity
Number.NaN;               // NaN
```

---
