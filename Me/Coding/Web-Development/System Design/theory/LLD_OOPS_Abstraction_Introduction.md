# Abstraction

- Abstraction = expose **what** a thing does, hide **how** it does it
- User operates the car via pedals/buttons — doesn't know what's under the hood
- In code: abstract class = the interface (pedals), concrete class = the implementation (engine internals)

---
# Why this matters

- Caller only knows the abstract interface — implementation can swap out freely
- Swap `SportsCar` for `ElectricCar` and the calling code doesn't change
- This is the foundation of polymorphism

---
