``` python
from typing import Annotated


def say_hello(name: Annotated[str, "this is just metadata"]) -> str:
    return f"Hello {name}"
```

---
- To provide **FastAPI** with additional metadata about how you want your application to behave.

---


