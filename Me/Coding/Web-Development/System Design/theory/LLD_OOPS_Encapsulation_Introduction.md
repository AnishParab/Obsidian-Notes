# Encapsulation

> Encapsulation = bundling data + behaviour together, then restricting access to that data

- Solves two problems in one pillar:
    - _Organisation:_ characteristics and behaviour live together in one unit (the class)
    - _Security:_ not everything inside should be accessible to the outside world

---
# Two rules of Encapsulation

- Data and methods that operate on that data belong in the same object
- Object controls what gets exposed — not everything is public

---
# Real-world analogy

- A car's speed is not a dial you set directly from outside
- You interact via `accelerate()` and `brake()` — the object controls its own state
- Setting `currentSpeed = 500` directly is exactly what encapsulation prevents

---
# What it gives you

- Data protection — internal state can't be corrupted by outside code
- Control — you decide what's readable, what's writable, what's neither
- Maintainability — internals can change without breaking outside code

---
# How it's enforced in code

- Access modifiers: `private`, `public`, `protected`
- Getters — controlled read access
- Setters — controlled write access (with validation if needed)

---
