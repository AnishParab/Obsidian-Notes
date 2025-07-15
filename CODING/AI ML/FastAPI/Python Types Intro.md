# Type Annotations / Type Hints
## Why to use?
This helps you use **LSP** and **code hints** more efficiently.

- These are type hints in python.
``` python
name: str
age: int
```

---
# Standard Type Hints
- `int`
- `float`
- `bool`
- `bytes`

---
# Generic Types with Type Parameters
- `dict`
- `list`
- `set`
- `tuple`
- `Union`
- `Optional`

**Use the standard typing module `typing`**
``` python
from typing import List, Dict, Tuple, Optional, Union, Any, Callable

# List
def process_items(items: list[str]):
    for item in items:
        print(item)

# Tuple and Set
def process_items(items_t: tuple[int, int, str], items_s: set[bytes]):
    return items_t, items_s

# Dict
def process_items(prices: dict[str, float]):
    for item_name, item_price in prices.items():
        print(item_name)
        print(item_price)
```

### Union
You can declare that a variable can be any of _several types_.
``` python
def process_item(item: int | str):
    print(item)
```

### Possibly `none`, Use Optional
``` python
from typing import Optional


def say_hi(name: Optional[str] = None):
    if name is not None:
        print(f"Hey {name}!")
    else:
        print("Hello World")
```
- `Optional[Something]` is actually a shortcut for `Union[Something, None]`, they are equivalent.
**NOTE :- If you are using Python version below 3.10, avoid using Optional.**

---
# Classes as Types
``` python
class Person:
    def __init__(self, name: str):
        self.name = name


def get_person_name(one_person: Person):
    return one_person.name
```

---






