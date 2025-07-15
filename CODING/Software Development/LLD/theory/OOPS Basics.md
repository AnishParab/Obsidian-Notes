#  History of Programming Languages
###   Machine Language (1st Generation)
- The earliest form of programming.
- Consists purely of binary digits — `0` and `1`.

- **Pros**: Direct execution by CPU, no translation needed.

- **Cons**:
    - Extremely **tedious** and **error-prone**.
    - **No abstraction** — difficult to understand or debug.
    - **Not scalable** — even small programs are lengthy.
    - **Platform-dependent** — tied closely to hardware.

---
###  Assembly Language (2nd Generation)
- Introduced **mnemonics** like `MOV`, `ADD`, `SUB` to represent instructions.
- Each mnemonic maps directly to machine instructions.

- **Pros**:
    - More readable than binary.
    - Gives fine-grained control over hardware.

- **Cons**:
    - **Hardware-dependent** — specific to CPU architecture.
    - **Low-level abstraction** — still complex for large systems.
    - Poor scalability for large software projects.

---
### Procedural Programming (3rd Generation)

> "Do this, then do that..."

- Focuses on step-by-step **procedures** (also called routines or functions).
- Introduces **control structures** like loops, conditionals, blocks.
- Examples: `C`, `Pascal`, `Fortran`.

**Key Concepts**:
- **Functions** to promote code reuse.
- **Loops** for iteration.
- **Conditional logic** for decision-making.

**Pros**:
- Easier to write and maintain than low-level code.
- Encourages modular design.

**Cons**:
- **Global data sharing** may lead to tight coupling.
- Difficult to model **real-world entities**.
- Poor encapsulation.

---
### Object-Oriented Programming (OOP)

> "Model the program based on the **real world**."

- Treats everything as **objects** which interact with each other.
- Improves code **modularity**, **security**, and **reusability**.

**Key Features**:
- Real-world modeling through **objects and classes**.

**Pros**:
- **Highly scalable** — suitable for large, complex systems.
- Promotes **code reuse** through inheritance and modularity.
- **Secure** — encapsulates data and behavior.

---
#  Why OOP?

- The **real world** is full of **objects** that interact (e.g., Car, Dog, Person).
- OOP allows developers to represent those **entities in code** with properties and behaviors.

---
### Object

> **Instance** of a class that represents a **real-world entity**.

- **Characteristics** → Represented as **variables / attributes** (e.g., `name`, `age`, `speed`).
- **Behavior** → Represented as **functions / methods** (e.g., `walk()`, `eat()`).

---
### Class

> A **blueprint** or **template** for creating objects.

- Defines what **attributes** and **behaviors** an object will have.
- Objects created from the same class share structure but have different data.

```cpp
class Dog {
    string name;
    int age;

    void bark() {
        // behavior
    }
};
```

---
# Pillars of OOP
- **Encapsulation** – hiding internal data.
- **Abstraction** – exposing only essential features.
- **Inheritance** – reuse code via hierarchies.
- **Polymorphism** – many forms of behavior with the same interface.

---






