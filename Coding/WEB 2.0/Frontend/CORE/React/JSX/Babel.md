# What is Babel
**Babel** is a **JavaScript compiler/transpiler** that converts **modern JavaScript (ES6+ and JSX)** into **backward-compatible JavaScript** so that it can run in older browsers or environments.

- JSX is not valid JS that all the browsers can understand.
- **Babel** transforms the code into something old browsers can understand.
- Tools like vite, webpack, next.js integrate babel behind the scenes.

---
# Functionalities
#### Transpilation
- Transforming source code from one version of a language to another (e.g., ES6 → ES5).

#### Abstract Syntax Tree
- It parses code into an **AST (Abstract Syntax Tree)**, transforms it, and then generates compatible output.

---
# How Babel Works
Babel’s pipeline generally has three main stages:  
- **Parse** – Convert source code into an Abstract Syntax Tree (AST).  
- **Transform** – Apply plugins & presets to modify the AST (e.g., transform arrow functions to function expressions).  
- **Generate** – Convert the transformed AST back into code.

---
