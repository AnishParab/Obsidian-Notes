# Metadata Annotations

``` python
from typing import Annotated

def say_hello(name: Annotated[str, "this is just metadata"]) -> str:
	return f"Hello {name}"
```

- The first parameter you pass to `Annotated` is the actual type. The rest, is just metadata for other tools.

---
