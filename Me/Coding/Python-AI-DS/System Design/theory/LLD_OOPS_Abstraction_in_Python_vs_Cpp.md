# C++ Quirks (for future mind-mapping)

| C++                          | Python                    | Why                                                                                            |
| ---------------------------- | ------------------------- | ---------------------------------------------------------------------------------------------- |
| `virtual void f() = 0`       | `@abstractmethod`         | Pure virtual = must override                                                                   |
| `virtual void f()`           | just `def f()`            | Virtual = runtime dispatch; Python does this always                                            |
| `class Car` (no parent)      | `class Car(ABC)`          | ABC makes the class abstract and enforceable                                                   |
| `Car* ptr = new SportsCar()` | `ptr = SportsCar()`       | C++ needs pointer to base type for polymorphic dispatch; Python references are already dynamic |
| `delete myCar`               | nothing                   | Manual vs garbage collected memory                                                             |
| `virtual ~Car() {}`          | `__del__` (rarely needed) | Ensures child destructor runs on base pointer delete                                           |

---
# The C++ mental model

- C++ is statically dispatched by default — `virtual` opts a method into runtime dispatch
- Without `virtual`, calling via base pointer calls the _base_ method, not the child's — silent wrong behaviour
- Python has no static dispatch — every method call is always dynamic, no keyword needed

---
# Python gotcha

- `ABC` + `@abstractmethod` both required for enforcement
- Forget either one → Python lets you instantiate the "abstract" class silently

---
