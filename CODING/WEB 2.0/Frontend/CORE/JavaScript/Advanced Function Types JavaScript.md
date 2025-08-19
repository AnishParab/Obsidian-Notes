# Anonymous Functions
- Functions without a name. Often used as callbacks.
``` js
setTimeout(function() {
  console.log("Hello after 1s");
}, 1000);
```

---
# Immediately Invoked Function Expression (IIFE)
- Function that runs immediately after definition.

> Useful for avoiding **global scope pollution**.

``` js
(function() {
  console.log("I run instantly!");
})();
```

---
# Higher-Order Functions
- Functions that take other functions as arguments or return them.
``` js
function apply(fn, x) {
  return fn(x);
}

const square = (n) => n * n;
console.log(apply(square, 5)); // 25
```

---
# Callback Functions
- Passed as argument to another function.
``` js
function fetchData(callback) {
  setTimeout(() => {
    callback("Data received!");
  }, 1000);
}

fetchData((msg) => console.log(msg));
```

---
# Closures
- A function that **remembers variables** from its outer scope.
``` js
function counter() {
  let count = 0;
  return function() {
    count++;
    return count;
  };
}

const inc = counter();
console.log(inc()); // 1
console.log(inc()); // 2
```

---
