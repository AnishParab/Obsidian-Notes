# Commenting
``` python
# This is a comment
print("Hello, World!")  # Print a string
```

---
# Multi-Line Comments
Python does not have true multi-line comments.
``` python
# This is a 
# Multi-Line Comment
print("Hello World")
```

---
# Docstrings
Use ` ``` ` or `"""` to describe functions, classes, and modules.
- These aren't comments.
- Python treats them like documentation.
- If you use tools like `help()` or _documentation generators_, they will pick this up.
``` python
def greet(name):
    """
    Greet the user by name.
    
    Parameters:
    name (str): The user's name
    """
    print(f"Hello, {name}!")
```

---


