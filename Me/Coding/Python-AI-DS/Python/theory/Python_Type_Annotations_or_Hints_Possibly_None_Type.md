# Example

You can declare that a value could have a type like `str`, but it could also be `None`.

``` python
def say_hi(name: str | None = None):
    if name is not None:
        print(f"Hey {name}!")
    else:
        print("Hello World")
```

---
