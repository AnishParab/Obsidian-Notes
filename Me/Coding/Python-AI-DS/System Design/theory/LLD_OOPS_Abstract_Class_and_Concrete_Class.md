# Two-Class Pattern

- Two-class pattern to model real-world entities cleanly
- **Abstract class** = the interface (pedals/buttons/steering wheel)
- **Concrete class** = the actual implementation (what happens under the hood)

---
# Abstract Class

- Defines _what_ methods must exist — **no implementation**
- Cannot be instantiated — blueprint only
- Child class must implement all abstract methods, or it's also abstract

> Tells the outside world _what_ the object can do, not _how_

---
# Concrete Class

- Inherits the abstract class
- Provides **full implementation** of every abstract method
- Can be instantiated
- Represents the actual working object

---
# Real World Example

**Real-world mapping (Car)**
- `Car` (abstract) = pedals, buttons, steering wheel — the user-facing interface
- `SportsCar(Car)` (concrete) = engine, gearbox, actual mechanics — the implementation
- You drive via `Car`'s interface without knowing what `SportsCar` does internally

**Why two classes**
- Separation of _what_ vs _how_
- Swap `SportsCar` for `ElectricCar` — calling code doesn't change
- Enforces a contract — every car type _must_ implement `startEngine`, `brake`, etc.

---
