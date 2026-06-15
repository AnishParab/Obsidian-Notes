# Pillars of OOPS

### Abstraction

- Hide complexity, expose only what's necessary
- _Why:_ caller shouldn't need to know internals to use something
- Example: you drive a car without knowing how the engine works

---
### Encapsulation

- Bundle data + methods together, restrict direct access to data
- _Why:_ protect object state from unintended modification
- Example: bank account balance isn't a public variable you set directly

---
**NOTE**
Abstraction and Encapsulation are often confused — quick distinction:
    - Abstraction = hide _complexity_ (what you don't need to see)
    - Encapsulation = hide _data_ (what you shouldn't touch directly)

---
### Inheritance

- Child class acquires properties and behaviour of parent class
- _Why:_ reuse existing code, establish is-a relationships
- Example: `SportsCar` is-a `Car`

---
### Polymorphism

- Same interface, different behaviour depending on the object
- _Why:_ write one piece of calling code that works for many types
- Example: `car.accelerate()` works whether it's a `SportsCar` or `ElectricCar`

---
