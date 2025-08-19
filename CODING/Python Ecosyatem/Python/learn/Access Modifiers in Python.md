# Public 
- Accessibility from anywhere.
``` python
class Server:
    def __init__(self):
        self.name = "nginx"  # public
```

- Access using :
``` python
s = Server()
print(s.name)  # ✅ Works fine
```

---
# Private
- Intended to be used only inside the class.
``` python
class Server:
    def __init__(self):
        self.__password = "root123"  # double underscore = private
```

- This gives error:
``` python
s = Server()
print(s.__password)  # ❌ AttributeError
```

But you can access it via _name mangling_.
``` python
print(s._Server__password)  # Not recommended but possible
```

---
# Protected
- Intended to be used when sub-classing.
``` python
class Server:
    def __init__(self):
        self._config = "default"  # single underscore = protected
```

- Access using:
``` python
s = Server()
print(s._config)  # ✅ Still accessible, but it's a “use at your own risk” situation
```

---






