> For heavy string concatenation, **template literals** or `Array.join()` can be faster.

---
# Example
``` js
function tag(strings, ...values) {
    console.log(strings); // ["Hello ", ", you are ", "!"]
    console.log(values);  // ["Alice", 30]
}
let name = "Alice";
let age = 30;
tag`Hello ${name}, you are ${age}!`;
```

---
# Explanation
``` js
tag`Hello ${name}, you are ${age}!`;

```

- JavaScript **does NOT** just produce a string.
- Instead it calls :
``` js
tag(["Hello ", ", you are ", "!"], "Alice", 30);

```

- `strings` = `["Hello ", ", you are ", "!"]` (an array of literal text chunks)
- `...values` = `["Alice", 30]` (the dynamic expressions)

---
