---

---
# JavaScript (JS)
- JavaScript is the **core language of the web**, designed to make web pages dynamic and interactive.
- It has evolved from a simple scripting language to a powerful, multi-paradigm language suitable for full-stack development.

---
## Language Characteristics
- **Client-Side Execution**  
    - Runs in the browser (e.g., Chrome, Firefox) to manipulate DOM, handle events, etc.
    
- **High-Level & Interpreted**  
    - JS abstracts low-level memory and hardware details.
    - Code is interpreted line-by-line (though modern engines JIT-compile it for speed).
    
- **Single-Threaded + Event Loop**  
    - JavaScript uses a single-threaded concurrency model.
    - The event loop handle's asynchronous tasks (e.g., HTTP calls, timers).
    
- **Dynamically Typed**  
    - Types are determined at runtime.
    - Variables can change types dynamically (use `typeof` to check).
    
- **Multi-Paradigm**  
    Supports:
    - **Object-Oriented Programming (OOP)** (prototypes, ES6 classes)
    - **Functional Programming** (first-class functions, closures, immutability)
    - **Procedural Programming**

---
## Core Features
- **First-Class Functions**  
    Functions can be:
    - Stored in variables
    - Passed as arguments
    - Returned from other functions  
        Enables higher-order programming and callbacks.
- **Closures**  
    Functions remember the scope in which they were defined, even when executed outside that scope. Useful for data encapsulation.
- **Asynchronous Programming**  
    Enables non-blocking I/O via:
    - **Callbacks**
    - **Promises**
    - **`async/await`**  
        Managed via the **event loop** and **callback queue**.
- **Event-Driven**  
    JS listens to browser events (click, input, HTTP responses) and reacts accordingly.
- **Runs in the Browser (default)**  
    Executed by engines like **V8** (Chrome), **SpiderMonkey** (Firefox), **Chakra** (Edge), etc.
    

---
## Memory Model
- JS has **automatic garbage collection**.
- Uses **heap memory** for objects and **stack memory** for primitives and function calls.

---
# Node.js
**Node.js** is a **JavaScript runtime built on Chrome’s V8 engine** that allows you to run JavaScript on the server side.

---
##  What it Offers
- **Server-Side JS Execution**  
    Enables backend programming using JavaScript (outside the browser).
- **Non-Blocking I/O Model**  
    Ideal for high-performance and real-time systems (like chat servers, APIs, etc.).
- **Event-Driven Architecture**  
    Uses the **event loop** and **libuv** to handle concurrent requests efficiently.
- **Built with C++ and V8**  
    V8 compiles JS into machine code. Node's core is written in C++ to interact with OS features.

---
## Built-In Modules
Node provides rich built-in modules for:
- File System: `fs`
- Networking: `net`, `http`, `https`
- OS Interaction: `os`, `child_process`
- Utilities: `path`, `url`, `crypto`, `events`

Also supports **NPM (Node Package Manager)** to use and share packages.

---
## Use Cases
- Building REST/GraphQL APIs
- Real-time applications (e.g., chat, collaboration tools)
- Command-line tools
- Web servers, proxies, and microservices

---

# ECMAScript (ES)
**ECMAScript (ES)** is the **standardized specification** that JavaScript follows. It defines the language syntax, semantics, and features.

---
## ES Versions (Major Milestones)
- **ES5 (2009)**  
    Strict mode, JSON support, `Array.forEach`, getters/setters# JavaScript (JS)
JavaScript is the **core language of the web**, designed to make web pages dynamic and interactive. It has evolved from a simple scripting language to a powerful, multi-paradigm language suitable for full-stack development.

---
## Language Characteristics
- **Client-Side Execution**  
    Runs in the browser (e.g., Chrome, Firefox) to manipulate DOM, handle events, etc.
    
- **High-Level & Interpreted**  
    JS abstracts low-level memory and hardware details. Code is interpreted line-by-line (though modern engines JIT-compile it for speed).
    
- **Single-Threaded + Event Loop**  
    JavaScript uses a single-threaded concurrency model with an event loop to handle asynchronous tasks (e.g., HTTP calls, timers).
    
- **Dynamically Typed**  
    Types are determined at runtime. Variables can change types dynamically (use `typeof` to check).
    
- **Multi-Paradigm**  
    Supports:
    - **Object-Oriented Programming (OOP)** (prototypes, ES6 classes)
    - **Functional Programming** (first-class functions, closures, immutability)
    - **Procedural Programming**

---
## Core Features
- **First-Class Functions**  
    Functions can be:
    - Stored in variables
    - Passed as arguments
    - Returned from other functions  
        Enables higher-order programming and callbacks.
- **Closures**  
    Functions remember the scope in which they were defined, even when executed outside that scope. Useful for data encapsulation.
- **Asynchronous Programming**  
    Enables non-blocking I/O via:
    - **Callbacks**
    - **Promises**
    - **`async/await`**  
        Managed via the **event loop** and **callback queue**.
- **Event-Driven**  
    JS listens to browser events (click, input, HTTP responses) and reacts accordingly.
- **Runs in the Browser (default)**  
    Executed by engines like **V8** (Chrome), **SpiderMonkey** (Firefox), **Chakra** (Edge), etc.
    

---
## Memory Model
- JS has **automatic garbage collection**.
- Uses **heap memory** for objects and **stack memory** for primitives and function calls.

---
# Node.js
**Node.js** is a **JavaScript runtime built on Chrome’s V8 engine** that allows you to run JavaScript on the server side.

---
##  What it Offers
- **Server-Side JS Execution**  
    Enables backend programming using JavaScript (outside the browser).
- **Non-Blocking I/O Model**  
    Ideal for high-performance and real-time systems (like chat servers, APIs, etc.).
- **Event-Driven Architecture**  
    Uses the **event loop** and **libuv** to handle concurrent requests efficiently.
- **Built with C++ and V8**  
    V8 compiles JS into machine code. Node's core is written in C++ to interact with OS features.

---
## Built-In Modules
Node provides rich built-in modules for:
- File System: `fs`
- Networking: `net`, `http`, `https`
- OS Interaction: `os`, `child_process`
- Utilities: `path`, `url`, `crypto`, `events`

Also supports **NPM (Node Package Manager)** to use and share packages.

---
## Use Cases
- Building REST/GraphQL APIs
- Real-time applications (e.g., chat, collaboration tools)
- Command-line tools
- Web servers, proxies, and microservices

---

# ECMAScript (ES)
**ECMAScript (ES)** is the **standardized specification** that JavaScript follows. It defines the language syntax, semantics, and features.

---
## ES Versions (Major Milestones)
- **ES5 (2009)**  
    Strict mode, JSON support, `Array.forEach`, getters/setters
- **ES6 / ES2015** – Major Upgrade
    - `let`, `const`
    - Arrow Functions `() => {}`
    - Classes `class Foo {}`
    - Modules `import/export`
    - Template Literals `` `Hello ${name}` ``
    - Promises
    - Destructuring
    - Spread/Rest Operators
- **ES7+ (ES2016 → Now)**
    - `async/await` (ES2017)
    - Optional chaining `obj?.key` (ES2020)
    - Nullish coalescing `??`
    - Top-level `await` (ES2022)
    - New built-ins: `Map`, `Set`, `BigInt`, etc.

---

## ECMAScript ≠ JavaScript
- ECMAScript is the **specification** (standard).
- JavaScript is the **implementation** of ECMAScript (with browser/Node APIs on top).

---

## Tooling & Compatibility
Use **transpilers** like:
- **Babel** – Convert modern JS to older ES5 for browser compatibility
- **TypeScript** – Adds static types, compiles to JS
- **ESLint/Prettier** – Linting & formatting

---

- **ES6 / ES2015** – Major Upgrade
    - `let`, `const`
    - Arrow Functions `() => {}`
    - Classes `class Foo {}`
    - Modules `import/export`
    - Template Literals `` `Hello ${name}` ``
    - Promises
    - Destructuring
    - Spread/Rest Operators
- **ES7+ (ES2016 → Now)**
    - `async/await` (ES2017)
    - Optional chaining `obj?.key` (ES2020)
    - Nullish coalescing `??`
    - Top-level `await` (ES2022)
    - New built-ins: `Map`, `Set`, `BigInt`, etc.

---

## ECMAScript ≠ JavaScript
- ECMAScript is the **specification** (standard).
- JavaScript is the **implementation** of ECMAScript (with browser/Node APIs on top).

---

## Tooling & Compatibility
Use **transpilers** like:
- **Babel** – Convert modern JS to older ES5 for browser compatibility
- **TypeScript** – Adds static types, compiles to JS
- **ESLint/Prettier** – Linting & formatting

---
