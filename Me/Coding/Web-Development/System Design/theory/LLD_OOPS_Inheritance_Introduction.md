# Inheritance

- Inheritance = child class acquires properties and behaviour of parent class
- Avoids rewriting common logic — define once in parent, reuse in all children
- Models **is-a** relationships

---
# Structure

- Parent class (base/superclass) → holds common data and behaviour
- Child class (derived/subclass) → inherits everything, adds or overrides what's specific to it

---
# What child gets from parent

- All public and protected fields and methods

> **Does NOT get**: constructors, destructors, private members (they exist but aren't directly accessible)

---
# Why it matters

- Reusability — common logic lives in one place
- Extensibility — add new car types without touching existing code
- Foundation for polymorphism — same interface, different behaviour per child

---
# Example

![[inheritance_lld_system_design.excalidraw|500]]

---
# UML Example

![[inheritance_uml_class_diagram.excalidraw|400]]

---
