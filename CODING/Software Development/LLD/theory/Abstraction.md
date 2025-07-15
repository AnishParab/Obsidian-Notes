**Abstraction** hides unnecessary details from a client, and showcase only what is necessary.

---
# Code
**Example :- Car**
``` cpp
#include<iostream>
#include<string>

using namespace std;

class Car {
	public:
		virtual void startEngine() = 0;
		virtual void shiftGear(int gear) = 0;
		virtual void accelerate() = 0;
		virtual void brake() = 0;
		virtual void stopEngine() = 0;
		virtual ~Car() {}
};

class SportsCar : public Car {};

int main() {}
```

---
# Virtual Functions in C++ (Basics)
A **virtual function** is a member function in the **base class** that you expect to be **overridden** in derived classes. It ensures that the **correct function is called for an object**, regardless of the **type of reference or pointer used to call the function**.

### Under the Hood
- Each class with virtual functions gets a **vtable** (virtual table) – a table of function pointers.
- Every object of such class has a hidden pointer called **vptr** that points to the vtable of its actual class.
- When a virtual function is called through a base class pointer, the vptr ensures the **correct overridden method** in the derived class is called.

---












