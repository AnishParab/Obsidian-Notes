# Key distinction

- Class = the blueprint (exists in code)
- Object = the instance (exists in memory at runtime)

---
# Object

- Everything in OOP is modelled as an **object** — a bundle of state + behaviour
- Has two aspects:
    - **Characteristics** (data/fields) — what it _is_
    - **Behaviour** (methods) — what it _does_
- Example — Car object:
    - Characteristics: `engine`, `brand`, `model`, `wheels`
    - Behaviour: `start()`, `stop()`, `gear_shift()`, `accelerate()`, `brake()`

---
# Class

- Blueprint for creating objects
- Defines what characteristics and behaviours _all_ objects of that type will have
- No memory allocated at class definition — only when object is instantiated

```
Car {
    engine, brand, model, wheels
    start(), stop(), gear_shift(), accelerate(), brake()
}

Owner {
    Car car   // Owner HAS-A Car — reuses the Car blueprint
    name, license
}
```

- `Owner` using `Car` inside it = **composition** — one class reusing another
- This is where reusability kicks in — define `Car` once, use it anywhere

---
