**Pre-requisites**
[[LLD_OOPS_Abstraction_Introduction]]
[[LLD_OOPS_Abstraction_Abstract_Class_and_Concrete_Class]]

---
# Abstract Class

``` python
from abc import ABC, abstractmethod

class Dog(ABC):
    @abstractmethod
    def speak(self):
        pass

    @abstractmethod
    def fetch(self):
        pass
```

- `Dog` cannot be instantiated — it's a contract
- Any class inheriting `Dog` must implement `speak` and `fetch`

**Hence**
``` python
d = Dog()  # TypeError — can't instantiate abstract class
```

---
# Concrete Class

``` python
class Labrador(Dog):
	# Concrete method
	# Cannot be instantiated if not implemented
    def speak(self):
        print("Woof!")

	# Concrete method
	# Cannot be instantiated if not implemented
    def fetch(self):
        print("Fetching the ball!")

d = Labrador()
d.speak()   # Woof!
d.fetch()   # Fetching the ball!
```

---
