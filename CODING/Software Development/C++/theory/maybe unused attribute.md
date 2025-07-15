# Unused Initialized Variables Warning
``` cpp
int main()
{
    int x { 5 }; // variable x defined

    // but not used anywhere

    return 0;
}
```
This gives a warning.

---
# `[[maybe_unused]]` attribute
``` cpp
int main()
{
    [[maybe_unused]] int x { 5 }; // Don't complain if x is unused

    return 0;
}
```

---
