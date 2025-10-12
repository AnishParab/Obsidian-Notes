- Also called as **uniform initialization** or **brace initialization**.

---
``` cpp
int width { 5 };    // direct-list-initialization of initial value 5 into variable width (preferred)
int height = { 6 }; // copy-list-initialization of initial value 6 into variable height (rarely used)
```

---
# Benefits of List-Initialization
## It disallows narrowing conversions
``` cpp
int main()
{
    // An integer can only hold non-fractional values.
    // Initializing an int with fractional value 4.5 requires the compiler to convert 4.5 to a value an int can hold.
    // Such a conversion is a narrowing conversion, since the fractional part of the value will be lost.

    int w1 { 4.5 }; // compile error: list-init does not allow narrowing conversion

    int w2 = 4.5;   // compiles: w2 copy-initialized to value 4
    int w3 (4.5);   // compiles: w3 direct-initialized to value 4

    return 0;
}
```

## Supports initialization with a list of values
Done in this chapter:
[[Initializing Multiple Variables]]

---
# Value-Initialization / Zero-Initialization
**To be used when the object's value is temporary and will be replaced.**
**Best practice is to initialize your variable upon creation**
``` cpp
int width {}; // value-initialization / zero-initialization to value 0
```
- Note that value initialization may not always be zero initialization.
- For class types, value-initialization (and default-initialization) may instead initialize the object to predefined default values, which may be non-zero.

**Default Initialization:** Variable is left with an indeterminate value.
``` cpp
int width;
```

---

