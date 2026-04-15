# Methods in a Class

- Method = function defined inside a class, operates on the object's data

> Difference from a regular function: always receives the object itself as the first argument

---
# Code

``` python
class Chai:
    def brew():
        print("Brewing chai...")


tea1 = Chai
tea1.brew()   # This works fine but no use

tea2 = Chai()
tea2.brew()   # TypeError: Should take self argument
```

---
# Conclusion

Hence we need to take `self` as an argument.
[[Python_Self_Argument_Implicit_Explicit_Passing]]

---
