# Code

``` js
console.log("hello")       // standard output
console.error("err")       // stderr, red in devtools
console.warn("warn")       // yellow warning
console.table([{a:1}])     // tabular data
console.dir(obj)           // interactive object tree
console.time("label")      // start timer
console.timeEnd("label")   // stop + print elapsed
alert("hi")                // browser only — blocking popup
document.write("hi")       // browser only — writes to DOM (avoid)
process.stdout.write("hi") // Node.js only — no newline
```

---
