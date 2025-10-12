# Summary
Initialization gives a variable an initial value at the point when it is created. Assignment gives a variable a value at some point after the variable is created.

---
# Variable Assignment

## Copy Assignment
``` cpp
int width; // define an integer variable named width
width = 5; // assignment of value 5 into variable width

// variable width now has value 5

width = 7; // change value stored in variable width to 7

// variable width now has value 7
```

---
# Assignment Operator
- `=`

---
# Variable Initialization
- Instead of using two steps (as done in the above case), we can initialize a variable in a single step.
``` cpp
#include <iostream>

int main()
{
    int width { 5 };    // define variable width and initialize with initial value 5
    std::cout << width; // prints 5

    return 0;
}
```

---
# 5 Forms of Initialization
``` cpp
int a;         // default-initialization (no initializer)

// Traditional initialization forms:
int b = 5;     // copy-initialization (initial value after equals sign)
int c ( 6 );   // direct-initialization (initial value in parenthesis)

// Modern initialization forms (preferred):
int d { 7 };   // direct-list-initialization (initial value in braces)
int e {};      // value-initialization (empty braces)
```

---







