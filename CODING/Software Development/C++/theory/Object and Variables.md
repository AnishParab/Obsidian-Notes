# Summary
- We use objects to access memory.
- A named object is called as a variable.
- Each variable has an identifier, a type and a value.
- A variable’s type is used to determine how the value in memory should be interpreted.
- Variables are actually created at runtime, when memory is allocated for their use.

---
# Data and Values
- In computing, **data** is any information that can be moved, processed, or stored by a computer.
- In programming, a single piece of data is called a **value** (sometimes called a **data value**).

---
# Key Insight
- Values placed in single-quotes are interpreted by the compiler as character values.  
- Values placed in double-quotes are interpreted by the compiler as text values.  
- Numeric values are not quoted.

---
# Literals
Values that are placed directly into the source code are called **literals**.
``` cpp
#include <iostream> // for std::cout

int main()
{
    std::cout << 5;       // print the literal number `5`
    std::cout << -6.7;    // print the literal number `-6.7`
    std::cout << 'H';     // print the literal character `H`
    std::cout << "Hello"; // print the literal text `Hello`

    return 0;
}
```
Literals are read-only values, so their values can’t be modified

---
# Random Access Memory
- When we run a program, the operating system loads the program into RAM. Any data that is hardcoded into the program itself (e.g. text such as “Hello, world!”) is loaded at this point.
- Common uses for this memory are to store values entered by the user, to store data read in from a file or network, or to store values calculated while the program is running

---
# Objects
- In C++, direct memory access is discouraged, don't deal with memory registers and make your life miserable.
- An **object** represents a region of storage (typically RAM or a CPU register).

---
# Variables
- An object with a name is called a **variable**.

- **Defining** a variable:
``` cpp
int x; // define a variable named x (of type int)
```
At **compile-time** (when the program is being compiled), when encountering this statement, the compiler makes a note to itself that we want a variable with the name `x`, and that the variable has the data type `int`

**NOTE:** A variable is only defined at _compile time_.

---
# Variable Creation
**NOTE:** A variable is created at _run time_.

- At **runtime** (when the program is loaded into memory and run), each object is given an actual storage location (such as RAM, or a CPU register) that it can use to store values.
- he process of reserving storage for an object’s use is called **allocation**.
- Once allocation has occurred, the object has been created and can be used.

---


