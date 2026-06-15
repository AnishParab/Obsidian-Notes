# POST Request

``` python
from fastapi import FastAPI

app = FastAPI()

@app.post("/items")
def create_item():
    return {"message": "Item created"}
```

---
