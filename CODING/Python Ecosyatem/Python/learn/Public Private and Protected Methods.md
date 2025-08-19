# Public Method
- No underscore before the method name.
- Fully accessible from anywhere inside/outside the class.

``` python
class Server:
	def start(self)
		print("Server started")

s = Server()
s.start()
```

---
# Protected Method
- _Single underscore_.
- Meant for internal use of sub-classes.
- Still accessible outside the class, but signals _Hndle with Care_.

``` python
class Server:
	def _restart(self):
		print("Server restarting please wait")

s = Server()
s._restart()  # ⚠️ Works, but not intended for outside use
```

---
# Private Method
- _Double Underscore_.
- _Name mangled_ to prevent accidental access.
- Cannot directly call from outside the class. Needs name mangling.

``` python
class Server:
    def __shutdown(self):
        print("Server shutting down (private method)")


s = Server()
# s.__shutdown()  # ❌ AttributeError

s._Server__shutdown()  # ✅ (name-mangled access, not recommended)
```

---




