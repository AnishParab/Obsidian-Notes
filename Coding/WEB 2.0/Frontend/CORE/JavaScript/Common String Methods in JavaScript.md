> All methods return **new strings** (immutability).

---
# Accessing Characters
``` js
let str = "JavaScript";
str[0];        // "J"
str.charAt(1); // "a"
str.charCodeAt(1); // 97 (UTF-16 code)
str.at(-1);    // "t" (ES2022, supports negative index)
```

---
# Searching Characters
``` js
let str = "Hello world";
str.indexOf("o");       // 4 (first match)
str.lastIndexOf("o");   // 7 (last match)
str.includes("world");  // true
str.startsWith("He");   // true
str.endsWith("ld");     // true
```

---
# Extracting
``` js
let str = "JavaScript";
str.slice(0, 4);     // "Java"
str.substring(0, 4); // "Java" (negative indexes = 0)
str.substr(4, 6);    // "Script" (deprecated)
```

---
# Modifying
``` js
let str = "  Hello World  ";
str.trim();          // "Hello World"
str.trimStart();     // "Hello World  "
str.trimEnd();       // "  Hello World"
str.toUpperCase();   // "HELLO WORLD"
str.toLowerCase();   // "hello world"
str.replace("World", "JS");           // "Hello JS"
str.replaceAll("l", "_");             // "He__o Wor_d" (ES2021)
```

---
# Splitting and Joining
``` js
let str = "apple,banana,grape";
let arr = str.split(","); // ["apple", "banana", "grape"]
arr.join(" - ");          // "apple - banana - grape"
```

---
# Repeating
``` js
"ha".repeat(3); // "hahaha"

```

---
# Padding
``` js
"5".padStart(3, "0"); // "005"
"5".padEnd(3, ".");   // "5.."
```

---
# Matching with Regex
``` js
let str = "The rain in SPAIN";
str.match(/ain/g);       // ["ain", "ain"]
str.matchAll(/ain/g);    // Iterator of matches
str.search(/spain/i);    // 12
str.replace(/\s/g, "_"); // "The_rain_in_SPAIN"
```

---
